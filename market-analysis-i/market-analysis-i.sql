# Write your MySQL query statement below
select u.user_id as buyer_id, u.join_date, count(order_id) as orders_in_2019
from Users u left join 
(
    select * from Orders where YEAR(order_date) = 2019
) as o
on o.buyer_id = u.user_id
group by u.user_id