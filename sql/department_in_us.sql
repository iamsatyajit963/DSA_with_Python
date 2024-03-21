/**
Problem Statement:
Display the details of those employees who have a manager working in the department that is US (i.e., country_id) based.

Note:

Return the columns employee_id, first_name, and last_name.
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
select 
e.employee_id, e.first_name, e.last_name 
from employees e 
join employees e1
on e.manager_id = e1.employee_id 
join departments d
on e1.department_id = d.department_id
join locations l
on d.location_id = l.location_id 
where country_id = 'US'
order by employee_id;
