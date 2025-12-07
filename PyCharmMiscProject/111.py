import sqlite3
import pandas as pd

# CSV файлды оқу
students = pd.read_csv(r"C:\Users\ARMAN\Downloads\students.csv")

# Алғашқы 5 жолды алу
students_first5 = students.head()

# SQLite деректер қорына қосылу
db_path = r"C:\Users\ARMAN\PyCharmMiscProject\mydatabase.db"
conn = sqlite3.connect(db_path)

# Егер кесте жоқ болса, құру (бар болса, оны қайта құруға болады)
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    country TEXT,
    city TEXT,
    birth_date TEXT,
    signup_date TEXT,
    is_premium BOOLEAN,
    marketing_channel TEXT
)
""")

# Алғашқы 5 жолды кестеге жазу
students_first5.to_sql('students', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print("Алғашқы 5 студент mydatabase.db деректер қорына сәтті жазылды!")
