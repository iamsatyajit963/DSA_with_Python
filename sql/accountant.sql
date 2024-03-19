/**
Problem Statement:
Using the employees table, create a new column as 'Accountant'.

If the employees are working at the 'FI_ACCOUNT' or 'AC_ACCOUNT' designation then label it as 1, else label all other designations as 0.

Return the columns 'employee_id', 'first_name', 'last_name', 'salary', 'Accountant'.
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

Note:Refer to the column job_id to get the details of the designation.
**/
SELECT employee_id, first_name, last_name, salary,
 CASE 
    WHEN job_id IN ('FI_ACCOUNT', 'AC_ACCOUNT') THEN 1 ELSE 0 END AS Accountant
FROM
employees
ORDER BY employee_id
