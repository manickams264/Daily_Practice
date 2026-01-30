CREATE DATABASE First_DB;
USE First_DB;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT,
    city VARCHAR(50),
    join_date DATE
);

INSERT INTO students VALUES
(1, 'Arun', 'arun@gmail.com', 21, 'Coimbatore', '2023-06-10'),
(2, 'Divya', 'divya@gmail.com', 22, 'Chennai', '2023-07-15'),
(3, 'Karthik', 'karthik@gmail.com', 20, 'Madurai', '2023-08-01'),
(4, 'Meena', 'meena@gmail.com', 23, 'Salem', '2023-05-20');

SELECT * FROM students;

CREATE TABLE courses (
	course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    duration_months INT,
    fee DECIMAL(8,2)
);

INSERT INTO courses VALUES
(101, 'Python', 3, 12000),
(102, 'SQL', 2, 8000),
(103, 'Web Development', 4, 20000);

SELECT * FROM courses;

CREATE TABLE enrollments (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enroll_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO enrollments VALUES
(1, 1, 101, '2023-06-15'),
(2, 1, 102, '2023-06-20'),
(3, 2, 103, '2023-07-18'),
(4, 3, 101, '2023-08-05'),
(5, 4, 102, '2023-05-25');

SELECT * FROM enrollments;

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    student_id INT,
    amount DECIMAL(8,2),
    payment_date DATE,
    payment_mode VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

INSERT INTO payments VALUES
(1, 1, 12000, '2023-06-16', 'UPI'),
(2, 2, 20000, '2023-07-20', 'Card'),
(3, 4, 8000, '2023-05-26', 'Cash');

SELECT * FROM payments;

-- DDL Practice

CREATE TABLE instructors (
	instructor_id INT PRIMARY KEY,
    name VARCHAR(30),
    specialization VARCHAR(25),
    experience_years INT
);

ALTER TABLE students ADD COLUMN phone_number VARCHAR(10);

-- UPDATE comes under DML

UPDATE students SET phone_number = '9876543218' WHERE student_id = 1;
UPDATE students SET phone_number = '8765432109' WHERE student_id = 2;
UPDATE students SET phone_number = '6543217896' WHERE student_id = 3;
UPDATE students SET phone_number = '6382245584' WHERE student_id = 4;

SELECT * FROM students;

ALTER TABLE students RENAME COLUMN city TO location;

ALTER TABLE payments MODIFY payment_mode VARCHAR(30);

DROP TABLE payments;

TRUNCATE TABLE enrollments;

RENAME TABLE courses TO course_details;

ALTER TABLE course_details MODIFY course_name VARCHAR(30) NOT NULL;

-- DML Practice

INSERT INTO students VALUES (5, 'Arunaesh', 'arunaesh@gmail.com', 21, 'Tirupur', '2023-05-09', '7654321899');

INSERT INTO course_details VALUES
(104, 'AIML', 6, 30000),
(105, 'Data Science', 6, 28000),
(106, 'Testing', 4, 22000);

SELECT * FROM students;

SELECT name, email FROM students;

SELECT * FROM students
WHERE age > 21;

SELECT * FROM students
WHERE location = 'Chennai';

UPDATE students SET location = 'Trichy' WHERE student_id = 3;

SET SQL_SAFE_UPDATES = 0; -- Because when we update a cell without a key workbench blocks it

UPDATE course_details SET fee = fee + 1000 WHERE course_name = 'SQL';

UPDATE payments SET payment_mode = 'NetBanking' WHERE payment_id = 3;

DELETE FROM payments WHERE student_id = 4; -- Because payment is a child class of students so we cannot directly delete a row from students
DELETE FROM students WHERE student_id = 4;

DELETE FROM students WHERE join_date < '2023-06-01';

SELECT * FROM students WHERE age BETWEEN 20 AND 22;

SELECT * FROM course_details WHERE fee IN (9000, 12000);

SELECT * FROM students WHERE name LIKE 'a%';

SELECT COUNT(*) FROM students;

SELECT MAX(amount) FROM payments;

SELECT course_id, COUNT(enroll_id) FROM enrollments
GROUP BY course_id;

INSERT INTO students VALUES (4, 'Meena', 'meena@gmail.com', 23, 'Salem', '2023-05-20','9876549321');

SELECT course_id, COUNT(*) FROM enrollments
GROUP BY course_id
HAVING COUNT(*) > 1;

SELECT location, COUNT(*) FROM students
GROUP BY location
HAVING COUNT(*) = 1;

SELECT students.name, course_details.course_name
FROM enrollments
JOIN students ON students.student_id = enrollments.student_id
JOIN course_details ON course_details.course_id = enrollments.course_id;

SELECT students.student_id, students.name
FROM students
LEFT JOIN payments ON students.student_id = payments.student_id
WHERE payments.student_id IS NULL;

SELECT course_details.course_name, COUNT(student_id)
FROM course_details
LEFT JOIN enrollments ON course_details.course_id = enrollments.course_id
GROUP BY course_details.course_name;



