CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    usn VARCHAR(20) UNIQUE NOT NULL,
    section VARCHAR(10),
    semester INT NOT NULL,
    batch INT NOT NULL
);
SHOW DATABASES;
CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    semester INT NOT NULL
);
CREATE TABLE marks (
    mark_id INT AUTO_INCREMENT PRIMARY KEY,
    usn VARCHAR(20),
    subject_id INT,
    cie_marks INT,
    see_marks INT,
    total_marks INT GENERATED ALWAYS AS (cie_marks + see_marks) STORED,
    FOREIGN KEY (usn) REFERENCES students(usn),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);
CREATE TABLE results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    usn VARCHAR(20),  -- Foreign Key to students
    total INT,
    percent FLOAT,
    sgpa FLOAT,
    result_status VARCHAR(10),
    file_name VARCHAR(255),
    FOREIGN KEY (usn) REFERENCES students(usn)  -- Linking to students table
);
SHOW TABLES;
DESC students;
DESC results;
DESC subjects;
DESC marks;
