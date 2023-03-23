# Write your MySQL query statement below
select name, 
    case 
        when dist is not null then dist
        else 0
    end as travelled_distance
from Users u left join (
    select user_id, sum(distance) as dist from Rides group by user_id order by dist
) as tb 
on tb.user_id = u.id
order by dist desc, name asc