/**
Problem Description:
Write a query to calculate the salary of all employees after an increment of 20%. Save the newly calculated salary column as 'New_salary'.
Table: employees
Schema:
|----------|----------|
Column Name  Data Type
-----------|-----------
emp_id        int
name          varchar
salary        int

Note:
Return the columns emp_id, name, salary, and 'New_salary'.
Order the output by the emp_id in ascending order.
Steps to calculate the salary increment:

1. Multiply the current salary by the percentage of the increment.
2. Divide the result by 100.
3. Then add the result to the current salary.
4. Name the column as 'New_Salary'
5. Round off the 'New_salary'.
**/
SELECT 
    emp_id,
    name,
    salary,
    ROUND(salary + (salary * 0.20),0) AS New_salary
FROM 
    employees
ORDER BY 
    emp_id ASC;
