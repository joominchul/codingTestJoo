-- https://school.programmers.co.kr/learn/courses/30/lessons/59042
SELECT o.ANIMAL_ID, o.NAME 
from ANIMAL_INS as i right join ANIMAL_OUTS as o using(ANIMAL_ID)
where i.ANIMAL_ID is null order by ANIMAL_ID
