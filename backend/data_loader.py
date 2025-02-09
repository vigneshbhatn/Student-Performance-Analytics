import pandas as pd
import mysql.connector
from mysql.connector import Error
import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vignesh2704",
            database="student_data"
        )
        logger.info("Successfully connected to database")
        return connection
    except Error as e:
        logger.error(f"Error connecting to database: {e}")
        raise

def load_students(df, cursor):
    try:
        # Insert unique students
        sql = """
        INSERT INTO students (usn, student_name, section, batch)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            student_name = VALUES(student_name),
            section = VALUES(section),
            batch = VALUES(batch)
        """
        
        for _, row in df.iterrows():
            values = (
                row['USN'],
                row['Student Name'],
                row['Section'],
                row['Batch']
            )
            cursor.execute(sql, values)
            
        logger.info("Successfully loaded students")
    except Error as e:
        logger.error(f"Error loading students: {e}")
        raise

def load_student_semesters(df, cursor):
    try:
        sql = """
        INSERT INTO student_semester (usn, semester)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE semester = VALUES(semester)
        """
        
        # Get unique combinations of USN and semester
        unique_combinations = df[['USN', 'Semester']].drop_duplicates()
        
        for _, row in unique_combinations.iterrows():
            values = (row['USN'], row['Semester'])
            cursor.execute(sql, values)
            
        logger.info("Successfully loaded student semesters")
    except Error as e:
        logger.error(f"Error loading student semesters: {e}")
        raise

def get_subject_columns(df):
    # Get all columns that contain (CIE)
    return [col for col in df.columns if '(CIE)' in col]

def load_subjects(df, cursor):
    try:
        subject_id_map = {}
        sql = """
        INSERT INTO subjects (subject_code, subject_name)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE subject_name = VALUES(subject_name)
        """
        
        # Get subject columns and extract subject names
        subject_columns = get_subject_columns(df)
        
        for col in subject_columns:
            subject_name = col.split('(')[0].strip()
            cursor.execute(sql, (subject_name, subject_name))
            
            # Get the subject_id
            cursor.execute("SELECT subject_id FROM subjects WHERE subject_code = %s", (subject_name,))
            subject_id = cursor.fetchone()[0]
            subject_id_map[subject_name] = subject_id
            
        logger.info("Successfully loaded subjects")
        return subject_id_map
    except Error as e:
        logger.error(f"Error loading subjects: {e}")
        raise

def load_subject_marks(df, cursor, subject_id_map):
    try:
        sql = """
        INSERT INTO subject_marks 
            (usn, subject_id, semester, cie_marks, see_marks, total_marks)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            cie_marks = VALUES(cie_marks),
            see_marks = VALUES(see_marks),
            total_marks = VALUES(total_marks)
        """
        
        for _, row in df.iterrows():
            for subject_name in subject_id_map.keys():
                cie_col = f"{subject_name} (CIE)"
                see_col = f"{subject_name} (SEE)"
                total_col = f"{subject_name} (Total)"
                
                if cie_col in df.columns and pd.notna(row[cie_col]):
                    values = (
                        row['USN'],
                        subject_id_map[subject_name],
                        row['Semester'],
                        float(row[cie_col]) if pd.notna(row[cie_col]) else None,
                        float(row[see_col]) if pd.notna(row[see_col]) else None,
                        float(row[total_col]) if pd.notna(row[total_col]) else None
                    )
                    cursor.execute(sql, values)
                    
        logger.info("Successfully loaded subject marks")
    except Error as e:
        logger.error(f"Error loading subject marks: {e}")
        raise

def clean_numeric_value(value):
    """Clean numeric values by removing unwanted characters"""
    if pd.isna(value):
        return None
    
    # If it's already a number, return as float
    if isinstance(value, (int, float)):
        return float(value)
    
    # If it's a string, clean it
    if isinstance(value, str):
        # Remove unwanted characters like '-', spaces, etc.
        cleaned = value.strip().rstrip('-').rstrip()
        return float(cleaned) if cleaned else None
    
    return None

def load_overall_results(df, cursor):
    try:
        sql = """
        INSERT INTO overall_results 
            (usn, semester, total_marks, percentage, sgpa, result_status, file_name)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            total_marks = VALUES(total_marks),
            percentage = VALUES(percentage),
            sgpa = VALUES(sgpa),
            result_status = VALUES(result_status),
            file_name = VALUES(file_name)
        """
        
        for _, row in df.iterrows():
            try:
                values = (
                    row['USN'],
                    row['Semester'],
                    clean_numeric_value(row['Total']),
                    clean_numeric_value(row['Percent']),
                    clean_numeric_value(row['SGPA']),
                    row['Result'],
                    row['File_Name']
                )
                cursor.execute(sql, values)
            except Exception as e:
                logger.error(f"Error processing row for USN {row['USN']}: {e}")
                logger.error(f"Problematic values - Total: {row['Total']}, Percent: {row['Percent']}, SGPA: {row['SGPA']}")
                continue
            
        logger.info("Successfully loaded overall results")
    except Error as e:
        logger.error(f"Error loading overall results: {e}")
        raise

def main():
    file_path = r"C:\Users\Vignesh\Documents\GitHub\Student-Performance-Analytics\data\combined_output.csv"
    
    try:
        # Read CSV file
        df = pd.read_csv(file_path)
        logger.info(f"Successfully read CSV file: {file_path}")
        
        # Connect to database
        connection = connect_to_db()
        cursor = connection.cursor()
        
        # Load data in correct order
        load_students(df, cursor)
        load_student_semesters(df, cursor)
        subject_id_map = load_subjects(df, cursor)
        load_subject_marks(df, cursor, subject_id_map)
        load_overall_results(df, cursor)
        
        # Commit changes and close connection
        connection.commit()
        logger.info("Successfully committed all changes")
        
    except Exception as e:
        logger.error(f"Error in main process: {e}")
        if 'connection' in locals():
            connection.rollback()
        raise
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
            logger.info("Database connection closed")

if __name__ == "__main__":
    main()