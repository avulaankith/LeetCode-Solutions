# Write your MySQL query statement below

select tb.customer_id, count(tb.visit_id) as count_no_trans

from (
    select *
    from visits v
    where v.visit_id not in (select visit_id from transactions)
) as tb
group by customer_id
order by count_no_trans