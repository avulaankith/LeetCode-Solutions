# Write your MySQL query statement below


select customer_number 
from (
    select customer_number, count(order_number) as count
    from Orders
    group by customer_number
) as tb 
order by count desc
limit 1