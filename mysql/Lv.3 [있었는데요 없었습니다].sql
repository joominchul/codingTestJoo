-- https://school.programmers.co.kr/learn/courses/30/lessons/59043
SELECT o.ANIMAL_ID, o.NAME 
from ANIMAL_INS as i right join ANIMAL_OUTS as o using(ANIMAL_ID)
where o.DATETIME < i.DATETIME order by i.DATETIME
