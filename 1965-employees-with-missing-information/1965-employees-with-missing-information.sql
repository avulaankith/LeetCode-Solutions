# Write your MySQL query statement below

select distinct(t.employee_id)
from (
    select 
    CASE
        WHEN e.employee_id not in (select employee_id from Salaries) and e.employee_id is not NULL THEN e.employee_id
        WHEN s.employee_id not in (select employee_id from Employees) and s.employee_id is not NULL THEN s.employee_id
    END as employee_id
    from Employees e, Salaries s
) as t
where t.employee_id is not NULL
order by t.employee_id