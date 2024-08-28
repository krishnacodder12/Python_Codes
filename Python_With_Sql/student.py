import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='your_database'
        )
        if connection.is_connected():
            print(f"Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection closed")

def create_student_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                student_id INT UNIQUE,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                dob DATE,
                course_enrolled VARCHAR(255)
            )
        """)
        connection.commit()
        print("Table 'students' created successfully")
    except Error as e:
        print(f"Error: {e}")

def add_student(connection, student_id, first_name, last_name, dob, course_enrolled):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO students (student_id, first_name, last_name, dob, course_enrolled)
            VALUES (%s, %s, %s, %s, %s)
        """, (student_id, first_name, last_name, dob, course_enrolled))
        connection.commit()
        print("Student added successfully")
    except Error as e:
        print(f"Error: {e}")

def view_all_students(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        if not rows:
            print("No students found.")
        else:
            print("List of all students:")
            for row in rows:
                print(f"ID: {row[0]}, Student ID: {row[1]}, Name: {row[2]} {row[3]}, DOB: {row[4]}, Course: {row[5]}")
    except Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    connection = create_connection()

    if connection:
        create_student_table(connection)

        while True:
            print("\nStudent Management System Menu:")
            print("1. Add a new student record")
            print("2. View a list of all students")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                student_id = int(input("Enter Student ID: "))
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                dob = input("Enter Date of Birth (YYYY-MM-DD): ")
                course_enrolled = input("Enter Course Enrolled: ")

                add_student(connection, student_id, first_name, last_name, dob, course_enrolled)

            elif choice == '2':
                view_all_students(connection)

            elif choice == '3':
                break

        close_connection(connection)
