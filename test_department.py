import mysql.connector
import os
import sys


DB_NAME = "CollegeDB"
TABLE_NAME = "Student"


def connect_mysql(database=None):
    config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "root",
        "port": 3306
    }

    if database:
        config["database"] = database

    return mysql.connector.connect(**config)


def fail(message):
    print("❌ FAILED:", message)
    sys.exit(1)


def success(message):
    print("✅", message)


# --------------------------------------------------
# 1. Check solution.sql
# --------------------------------------------------

if not os.path.exists("solution.sql"):
    fail("solution.sql file was not found.")

success("solution.sql found.")


# --------------------------------------------------
# 2. Read solution.sql
# --------------------------------------------------

with open("solution.sql", "r", encoding="utf-8") as file:
    sql_script = file.read().strip()

if not sql_script:
    fail("solution.sql is empty.")

success("solution.sql contains SQL code.")


# --------------------------------------------------
# 3. Connect to MySQL
# --------------------------------------------------

try:
    connection = connect_mysql()
    cursor = connection.cursor()
    success("Connected to MySQL.")
except Exception as e:
    fail(f"Could not connect to MySQL: {e}")


# --------------------------------------------------
# 4. Execute student's SQL
# --------------------------------------------------

try:
    statements = sql_script.split(";")

    for statement in statements:
        statement = statement.strip()

        if statement:
            cursor.execute(statement)

    connection.commit()

    success("SQL script executed successfully.")

except Exception as e:
    fail(f"SQL execution failed: {e}")


# --------------------------------------------------
# 5. Check database
# --------------------------------------------------

try:
    cursor.execute(
        """
        SELECT SCHEMA_NAME
        FROM INFORMATION_SCHEMA.SCHEMATA
        WHERE SCHEMA_NAME = %s
        """,
        (DB_NAME,)
    )

    result = cursor.fetchone()

    if result is None:
        fail("CollegeDB database was not created.")

    success("CollegeDB database exists.")

except Exception as e:
    fail(f"Database verification failed: {e}")


# --------------------------------------------------
# 6. Select database
# --------------------------------------------------

try:
    cursor.execute("USE CollegeDB")
    success("CollegeDB selected successfully.")
except Exception as e:
    fail(f"Could not select CollegeDB: {e}")


# --------------------------------------------------
# 7. Check Student table
# --------------------------------------------------

try:
    cursor.execute(
        """
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = %s
        AND TABLE_NAME = %s
        """,
        (DB_NAME, TABLE_NAME)
    )

    result = cursor.fetchone()

    if result is None:
        fail("Student table was not created.")

    success("Student table exists.")

except Exception as e:
    fail(f"Student table verification failed: {e}")


# --------------------------------------------------
# 8. Get column information
# --------------------------------------------------

try:
    cursor.execute(
        """
        SELECT
            COLUMN_NAME,
            DATA_TYPE,
            CHARACTER_MAXIMUM_LENGTH,
            IS_NULLABLE,
            COLUMN_KEY,
            ORDINAL_POSITION
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = %s
        AND TABLE_NAME = %s
        ORDER BY ORDINAL_POSITION
        """,
        (DB_NAME, TABLE_NAME)
    )

    columns = cursor.fetchall()

except Exception as e:
    fail(f"Could not read Student table structure: {e}")


# --------------------------------------------------
# 9. Check exactly 5 columns
# --------------------------------------------------

if len(columns) != 5:
    fail(
        f"Student table must contain exactly 5 columns. "
        f"Found {len(columns)}."
    )

success("Student table contains exactly 5 columns.")


# --------------------------------------------------
# 10. Check StudentID
# --------------------------------------------------

student_id = columns[0]

if student_id[0].lower() != "studentid":
    fail("First column must be StudentID.")

if student_id[1].lower() not in [
    "int",
    "integer",
    "smallint",
    "mediumint",
    "bigint",
    "tinyint"
]:
    fail("StudentID must use an integer data type.")

if student_id[4] != "PRI":
    fail("StudentID must be the PRIMARY KEY.")

if student_id[3] != "NO":
    fail("StudentID must be NOT NULL.")

success("StudentID is correct and is the PRIMARY KEY.")


# --------------------------------------------------
# 11. Check StudentName
# --------------------------------------------------

student_name = columns[1]

if student_name[0].lower() != "studentname":
    fail("Second column must be StudentName.")

if student_name[1].lower() != "varchar":
    fail("StudentName must be VARCHAR.")

if student_name[2] != 20:
    fail("StudentName must be VARCHAR(20).")

if student_name[3] != "NO":
    fail("StudentName must be NOT NULL.")

success("StudentName VARCHAR(20) NOT NULL is correct.")


# --------------------------------------------------
# 12. Check StudentName UNIQUE constraint
# --------------------------------------------------

try:
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.STATISTICS
        WHERE TABLE_SCHEMA = %s
        AND TABLE_NAME = %s
        AND COLUMN_NAME = 'StudentName'
        AND NON_UNIQUE = 0
        """,
        (DB_NAME, TABLE_NAME)
    )

    unique_count = cursor.fetchone()[0]

    if unique_count == 0:
        fail("StudentName must have a UNIQUE constraint.")

    success("StudentName UNIQUE constraint is correct.")

except Exception as e:
    fail(f"Could not verify StudentName UNIQUE constraint: {e}")


# --------------------------------------------------
# 13. Check DOB
# --------------------------------------------------

dob = columns[2]

if dob[0].lower() != "dob":
    fail("Third column must be DOB.")

if dob[1].lower() != "date":
    fail("DOB must be DATE.")

if dob[3] != "NO":
    fail("DOB must be NOT NULL.")

success("DOB DATE NOT NULL is correct.")


# --------------------------------------------------
# 14. Check Gender
# --------------------------------------------------

gender = columns[3]

if gender[0].lower() != "gender":
    fail("Fourth column must be Gender.")

if gender[1].lower() != "varchar":
    fail("Gender must be VARCHAR.")

if gender[2] != 10:
    fail("Gender must be VARCHAR(10).")

if gender[3] != "NO":
    fail("Gender must be NOT NULL.")

success("Gender VARCHAR(10) NOT NULL is correct.")


# --------------------------------------------------
# 15. Check DepartmentID
# --------------------------------------------------

department_id = columns[4]

if department_id[0].lower() != "departmentid":
    fail("Fifth column must be DepartmentID.")

if department_id[1].lower() not in [
    "int",
    "integer",
    "smallint",
    "mediumint",
    "bigint",
    "tinyint"
]:
    fail("DepartmentID must use an integer data type.")

if department_id[3] != "NO":
    fail("DepartmentID must be NOT NULL.")

success("DepartmentID INTEGER NOT NULL is correct.")


# --------------------------------------------------
# 16. Final result
# --------------------------------------------------

print()
print("==============================================")
print("🎉 ALL TESTS PASSED")
print("==============================================")
print("CollegeDB database              : PASS")
print("Student table                   : PASS")
print("Exactly 5 columns               : PASS")
print("StudentID PRIMARY KEY           : PASS")
print("StudentID NOT NULL              : PASS")
print("StudentName VARCHAR(20)         : PASS")
print("StudentName UNIQUE              : PASS")
print("StudentName NOT NULL            : PASS")
print("DOB DATE NOT NULL               : PASS")
print("Gender VARCHAR(10) NOT NULL     : PASS")
print("DepartmentID INTEGER NOT NULL   : PASS")
print("==============================================")

cursor.close()
connection.close()

sys.exit(0)
