CREATE DATABASE IF NOT EXISTS student_data
USE student_data

DROP TABLE IF EXISTS subject_marks;
DROP TABLE IF EXISTS overall_results;
DROP TABLE IF EXISTS student_semester;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS subjects;

CREATE TABLE students (
    usn VARCHAR(20) PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    section VARCHAR(10),
    batch VARCHAR(20)
);

-- Create student_semester table to track multiple semesters
CREATE TABLE student_semester (
    student_semester_id INT AUTO_INCREMENT PRIMARY KEY,
    usn VARCHAR(20),
    semester INT,
    FOREIGN KEY (usn) REFERENCES students(usn),
    UNIQUE KEY unique_student_semester (usn, semester)
);

-- Create subjects table
CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_code VARCHAR(20) NOT NULL,
    subject_name VARCHAR(100) NOT NULL,
    UNIQUE KEY unique_subject (subject_code)
);

-- Create subject_marks table with semester
CREATE TABLE subject_marks (
    mark_id INT AUTO_INCREMENT PRIMARY KEY,
    usn VARCHAR(20),
    subject_id INT,
    semester INT,  -- Added semester here
    cie_marks DECIMAL(5,2),
    see_marks DECIMAL(5,2),
    total_marks DECIMAL(5,2),
    FOREIGN KEY (usn) REFERENCES students(usn),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    UNIQUE KEY unique_student_subject_sem (usn, subject_id, semester)
);

-- Create overall_results table with semester
CREATE TABLE overall_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    usn VARCHAR(20),
    semester INT,  -- Added semester here
    total_marks DECIMAL(5,2),
    percentage DECIMAL(5,2),
    sgpa DECIMAL(3,2),
    result_status VARCHAR(20),
    file_name VARCHAR(255),
    FOREIGN KEY (usn) REFERENCES students(usn),
    UNIQUE KEY unique_student_result_sem (usn, semester)
);

SELECT * FROM subjects;
SELECT * FROM students;
SELECT * FROM subject_marks;
SELECT * FROM overall_results;
SELECT * FROM student_semester;

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE students;
TRUNCATE TABLE subjects;
TRUNCATE TABLE subject_marks;
TRUNCATE TABLE student_semester;
TRUNCATE TABLE overall_results;
SET FOREIGN_KEY_CHECKS = 1;
