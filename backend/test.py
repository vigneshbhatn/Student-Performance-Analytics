import mysql.connector
import pandas as pd

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="vignesh2704",
        database="student_performance"
    )

def insert_student(cursor, usn, name, section, semester, batch):
    sql = """INSERT INTO students (usn, student_name, section, semester, batch) 
             VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE student_name=VALUES(student_name)"""
    cursor.execute(sql, (usn, name, section, semester, batch))

def insert_subject(cursor, subject_name):
    sql = "INSERT INTO subjects (subject_name) VALUES (%s) ON DUPLICATE KEY UPDATE subject_name=VALUES(subject_name)"
    cursor.execute(sql, (subject_name,))

def get_subject_id(cursor, subject_name):
    sql = "SELECT subject_id FROM subjects WHERE subject_name=%s"
    cursor.execute(sql, (subject_name,))
    result = cursor.fetchone()
    return result[0] if result else None

def insert_marks(cursor, usn, subject_id, cie_marks, see_marks):
    sql = """INSERT INTO marks (usn, subject_id, cie_marks, see_marks) 
             VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql, (usn, subject_id, cie_marks, see_marks))

def insert_results(cursor, usn, total, percent, sgpa, result_status, file_name):
    sql = """INSERT INTO results (usn, total, percent, sgpa, result_status, file_name) 
             VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (usn, total, percent, sgpa, result_status, file_name))

def process_csv(file_path):
    conn = connect_db()
    cursor = conn.cursor()
    df = pd.read_csv(file_path)
    
    for _, row in df.iterrows():
        usn = row['USN']
        name = row['Student Name']
        section = row['Section']
        semester = row['Semester'] if pd.notna(row['Semester']) else 1  # Use 1 if missing
        batch = row['Batch']

        insert_student(cursor, usn, name, section, int(semester), batch)

        for col in df.columns:
            if '(CIE)' in col:
                subject_name = col.split('(')[0].strip()  # Extract subject name

                insert_subject(cursor, subject_name)  # Ensure subject exists
                subject_id = get_subject_id(cursor, subject_name)  # Fetch subject ID

                cie_marks = row[col]
                see_marks = row.get(col.replace('CIE', 'SEE'), 0)  # Avoid KeyError

                insert_marks(cursor, usn, subject_id, cie_marks, see_marks)  # ✅ No total_marks

    # ✅ Ensure 'Total', 'Percent', 'SGPA', 'Result', 'File_Name' exist before inserting
        total = row.get('Total', 0)
        percent = row.get('Percent', 0)
        sgpa = row.get('SGPA', 0)
        result = row.get('Result', 'Unknown')
        file_name = row.get('File_Name', 'Unknown')

        insert_results(cursor, usn, total, percent, sgpa, result, file_name)

    conn.commit()
    cursor.close()
    conn.close()

# Run the script
process_csv(r"C:\Users\Vignesh\Documents\GitHub\Student-Performance-Analytics\data\combined_output.csv")
