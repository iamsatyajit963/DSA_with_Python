/**
Problem Statement:

Display the details of all the employees whose department location is in Seattle.

Return the columns 'employee_id', 'first_name', 'last_name', and job_id'.
Return the table ordered by employee_id in ascending order.

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
    e.employee_id,
    e.first_name,
    e.last_name,
    e.job_id
FROM 
    Employees e
JOIN 
    departments d ON e.department_id = d.department_id
JOIN 
    locations l ON d.location_id = l.location_id
WHERE 
    l.city = 'Seattle'
ORDER BY 
    e.employee_id ASC;
