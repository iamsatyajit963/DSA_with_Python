/**
Write a query to find the details of the other employees who work in the same job as the employee with employee_id as 107.

Note:

Create a new column "full_name" by concatenating the first_name and last_name columns, separated by space.
Return the columns 'full_name', 'salary', 'department_id', and 'job_id'.
Return the output ordered by full_name in ascending order.

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
    CONCAT(first_name, ' ', last_name) AS full_name,
    salary,
    department_id,
    job_id
FROM
    employees
WHERE
    job_id = (SELECT job_id FROM employees WHERE employee_id = 107)
ORDER BY
    full_name ASC;
