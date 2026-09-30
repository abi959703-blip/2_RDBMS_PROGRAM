# Student Table – SQL Programming Assignment

## Problem Statement

Create a database named `CollegeDB` and create a table named `Student` with the following fields:

| Field | Data Type | Constraint |
|---|---|---|
| StudentID | INT | PRIMARY KEY |
| StudentName | VARCHAR(20) | UNIQUE, NOT NULL |
| DOB | DATE | NOT NULL |
| Gender | VARCHAR(10) | NOT NULL |
| DepartmentID | INT | NOT NULL |

## Requirements

1. Create a database named `CollegeDB`.
2. Select/use the `CollegeDB` database.
3. Create a table named `Student`.
4. The table must contain exactly five fields:
   - `StudentID` – INT – PRIMARY KEY
   - `StudentName` – VARCHAR(20) – UNIQUE, NOT NULL
   - `DOB` – DATE – NOT NULL
   - `Gender` – VARCHAR(10) – NOT NULL
   - `DepartmentID` – INT – NOT NULL
5. `StudentID` must be the Primary Key.
6. `StudentName` must be UNIQUE.
7. `StudentName`, `DOB`, `Gender`, and `DepartmentID` must be NOT NULL.
8. Do not add extra columns.

## Submission

Create a file named:

```text
solution.sql
