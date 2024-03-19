/**
Problem Statement:

Based on the employee's salary, divide the employees into three different classes.

Salary greater than 20,000 (i.e, excluding 20,000) as 'Class A'
Salary between 10,000 to 20,000 (i.e, including both 10,000 and 20,000) as 'Class B'
Salary less than 10,000 (i.e, excluding 10,000) as 'Class C'. Return the new column as 'Salary_bin'.
Return the columns 'employee_id', 'salary', and 'Salary_bin'.
Return the result ordered by employee_id in ascending order.
Table Name: employees
Schema:
Departmant [departmane_id, department_name, manager_id, location_id]
Employees [employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id]
Locations [location_id, street_address, postal_code, city, state_province, country_id]
Countries [country_id, country_name, region_id]
Regions [region_id, region_name]
Job_history [employee_id, start_date, end_date, job_id, department_id]
Jobs [job_id, job_title, min_salary, max_salary]

**/
SELECT 
    employee_id,
    salary,
    CASE
        WHEN salary > 20000 THEN 'Class A'
        WHEN salary >= 10000 AND salary <= 20000 THEN 'Class B'
        ELSE 'Class C'
    END AS Salary_bin
FROM 
    employees
ORDER BY 
    employee_id ASC;
