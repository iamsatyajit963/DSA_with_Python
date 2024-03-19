/**
Problem Description:

Write a query to find all the employees whose first_name ends with the letter 'n'.

Return the columns 'employee_id', 'full_name' (first name and last name separated by space), and 'phone_number'.
Return the output ordered by employee_id in ascending order.

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
    CONCAT(first_name, ' ', last_name) AS full_name,
    phone_number
FROM 
    employees
WHERE 
    SUBSTRING(first_name, -1) = 'n'
ORDER BY 
    employee_id ASC;

