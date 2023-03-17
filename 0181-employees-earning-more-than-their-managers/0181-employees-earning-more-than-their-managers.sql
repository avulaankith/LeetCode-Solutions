# Write your MySQL query statement below

select name as "Employee" from Employee e
where salary > (select salary from Employee e2 where e2.id = e.managerId and e.managerId is not null)