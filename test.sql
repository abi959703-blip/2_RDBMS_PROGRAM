-- ============================================================
-- TEST.SQL
-- Student Table Autograding Test
-- ============================================================

USE CollegeDB;

-- ============================================================
-- TEST 1: Student table exists
-- ============================================================

SELECT
CASE
    WHEN COUNT(*) = 1
    THEN 'PASS - Student table exists'
    ELSE 'FAIL - Student table does not exist'
END AS Result
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student';


-- ============================================================
-- TEST 2: Student table has exactly 5 columns
-- ============================================================

SELECT
CASE
    WHEN COUNT(*) = 5
    THEN 'PASS - Student table has exactly 5 columns'
    ELSE 'FAIL - Student table must have exactly 5 columns'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student';


-- ============================================================
-- TEST 3: StudentID - INT
-- ============================================================

SELECT
CASE
    WHEN DATA_TYPE IN ('int', 'integer')
    THEN 'PASS - StudentID is INT'
    ELSE 'FAIL - StudentID must be INT'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'StudentID';


-- ============================================================
-- TEST 4: StudentID - PRIMARY KEY
-- ============================================================

SELECT
CASE
    WHEN COLUMN_KEY = 'PRI'
    THEN 'PASS - StudentID is PRIMARY KEY'
    ELSE 'FAIL - StudentID must be PRIMARY KEY'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'StudentID';


-- ============================================================
-- TEST 5: StudentName - VARCHAR(20)
-- ============================================================

SELECT
CASE
    WHEN DATA_TYPE = 'varchar'
    AND CHARACTER_MAXIMUM_LENGTH = 20
    THEN 'PASS - StudentName is VARCHAR(20)'
    ELSE 'FAIL - StudentName must be VARCHAR(20)'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'StudentName';


-- ============================================================
-- TEST 6: StudentName - NOT NULL
-- ============================================================

SELECT
CASE
    WHEN IS_NULLABLE = 'NO'
    THEN 'PASS - StudentName is NOT NULL'
    ELSE 'FAIL - StudentName must be NOT NULL'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'StudentName';


-- ============================================================
-- TEST 7: StudentName - UNIQUE
-- ============================================================

SELECT
CASE
    WHEN COUNT(*) > 0
    THEN 'PASS - StudentName has UNIQUE constraint'
    ELSE 'FAIL - StudentName must have UNIQUE constraint'
END AS Result
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'StudentName'
AND NON_UNIQUE = 0;


-- ============================================================
-- TEST 8: DOB - DATE
-- ============================================================

SELECT
CASE
    WHEN DATA_TYPE = 'date'
    THEN 'PASS - DOB is DATE'
    ELSE 'FAIL - DOB must be DATE'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'DOB';


-- ============================================================
-- TEST 9: DOB - NOT NULL
-- ============================================================

SELECT
CASE
    WHEN IS_NULLABLE = 'NO'
    THEN 'PASS - DOB is NOT NULL'
    ELSE 'FAIL - DOB must be NOT NULL'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'DOB';


-- ============================================================
-- TEST 10: Gender - VARCHAR(10)
-- ============================================================

SELECT
CASE
    WHEN DATA_TYPE = 'varchar'
    AND CHARACTER_MAXIMUM_LENGTH = 10
    THEN 'PASS - Gender is VARCHAR(10)'
    ELSE 'FAIL - Gender must be VARCHAR(10)'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'Gender';


-- ============================================================
-- TEST 11: Gender - NOT NULL
-- ============================================================

SELECT
CASE
    WHEN IS_NULLABLE = 'NO'
    THEN 'PASS - Gender is NOT NULL'
    ELSE 'FAIL - Gender must be NOT NULL'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'Gender';


-- ============================================================
-- TEST 12: DepartmentID - INT
-- ============================================================

SELECT
CASE
    WHEN DATA_TYPE IN ('int', 'integer')
    THEN 'PASS - DepartmentID is INT'
    ELSE 'FAIL - DepartmentID must be INT'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'DepartmentID';


-- ============================================================
-- TEST 13: DepartmentID - NOT NULL
-- ============================================================

SELECT
CASE
    WHEN IS_NULLABLE = 'NO'
    THEN 'PASS - DepartmentID is NOT NULL'
    ELSE 'FAIL - DepartmentID must be NOT NULL'
END AS Result
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
AND COLUMN_NAME = 'DepartmentID';


-- ============================================================
-- FINAL TABLE STRUCTURE
-- ============================================================

SELECT
    COLUMN_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    IS_NULLABLE,
    COLUMN_KEY
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'CollegeDB'
AND TABLE_NAME = 'Student'
ORDER BY ORDINAL_POSITION;
