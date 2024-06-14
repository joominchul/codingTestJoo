-- https://school.programmers.co.kr/learn/courses/30/lessons/133027
SELECT f.FLAVOR from FIRST_HALF as f inner join JULY as j using(FLAVOR)
group by FLAVOR order by sum(f.TOTAL_ORDER) + sum(j.TOTAL_ORDER) desc limit 3
