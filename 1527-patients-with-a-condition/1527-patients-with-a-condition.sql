# Write your MySQL query statement below

select p.patient_id, p.patient_name, p.conditions
from Patients p
where conditions like "DIAB1%" or conditions like "% DIAB1%"