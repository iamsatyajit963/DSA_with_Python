/**
Find the details of employees who are not working in any department.

Return the columns 'employee_id', 'first_name', 'last_name', 'job_id', and 'manager_id'.
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

Note: The missing value in the department_id column in the employee's table refers to not working in any department.
**/

SELECT employee_id, first_name, last_name, job_id, manager_id
FROM
employees
where department_id is null
ORDER BY employee_id
