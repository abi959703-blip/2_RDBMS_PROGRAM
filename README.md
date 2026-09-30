# Student Table – SQL Programming Assignment

## Problem Statement

Create a database named `CollegeDB` and create a table named `Student`
with the following fields:

| Field | Data Type | Constraint |
|---|---|---|
| StudentID | INT | PRIMARY KEY |
| StudentName | VARCHAR(20) | UNIQUE, NOT NULL |
| DOB | DATE | NOT NULL |
| Gender | VARCHAR(10) | NOT NULL |
| DepartmentID | INT | NOT NULL |

## Requirements

Create a database named:

CollegeDB

Create a table named:

Student

The Student table must contain exactly five columns:

1. StudentID – INT – PRIMARY KEY
2. StudentName – VARCHAR(20) – UNIQUE, NOT NULL
3. DOB – DATE – NOT NULL
4. Gender – VARCHAR(10) – NOT NULL
5. DepartmentID – INT – NOT NULL

## Constraints

The following constraints must be applied:

- StudentID must be the PRIMARY KEY.
- StudentName must be UNIQUE.
- StudentName must be NOT NULL.
- DOB must be NOT NULL.
- Gender must be NOT NULL.
- DepartmentID must be NOT NULL.

## Submission

Write your SQL program in:

solution.sql

## Expected SQL Structure

```sql
CREATE DATABASE CollegeDB;

USE CollegeDB;

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(20) UNIQUE NOT NULL,
    DOB DATE NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    DepartmentID INT NOT NULL
);
