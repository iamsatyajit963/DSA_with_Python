/**
Problem Description:
Find the details of the employees who are working in the departments 'Administration', 'Marketing', and 'Human Resources'.

Return the columns 'employee_id', 'full_name'(first and last name separated by space), and 'salary'.
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
    employee_id, CONCAT(first_name, ' ', last_name) AS full_name, salary
FROM
employees
WHERE department_id in (SELECT department_id from departments where department_name in ('Administration', 'Marketing', 'Human Resources'))
ORDER BY employee_id
