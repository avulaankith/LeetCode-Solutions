# Write your MySQL query statement below
select u.name, a.balance
from (
    select account, sum(amount) as balance
    from Transactions
    group by account
) as a, Users u
where balance > 10000 and a.account = u.account