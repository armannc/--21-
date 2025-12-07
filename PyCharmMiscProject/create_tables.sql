
-- Students
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    country VARCHAR(10),
    signup_date DATE,
    is_premium BOOLEAN
);

-- Courses
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    category VARCHAR(50),
    price_usd DECIMAL(10,2)
);

-- Enrollments
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    price_paid_usd DECIMAL(10,2),
    rating DECIMAL(3,2),
    discount_code VARCHAR(20),
    marketing_channel VARCHAR(50),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Activity Log
CREATE TABLE activity_log (
    log_id INT PRIMARY KEY,
    student_id INT,
    event_time TIMESTAMP,
    duration_sec INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
