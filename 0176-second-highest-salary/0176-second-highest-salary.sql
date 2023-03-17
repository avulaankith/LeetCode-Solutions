# Write your MySQL query statement below

select max(tb.salary) as 'SecondHighestSalary'
from (
    select salary
    from Employee
    where salary < (select max(salary) from Employee)
) as tb
