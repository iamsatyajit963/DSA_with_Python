/**
Problem Statement:
Display the details of those employees who have a manager working in the department that is US (i.e., country_id) based.

Note:

Return the columns employee_id, first_name, and last_name.
Return the result ordered by employee_id in ascending order.
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
