-- https://school.programmers.co.kr/learn/courses/30/lessons/131117
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, sum(p.PRICE*o.AMOUNT) as TOTAL_SALES 
from FOOD_PRODUCT as p inner join FOOD_ORDER as o using(PRODUCT_ID)
where o.PRODUCE_DATE like '2022-05%' group by PRODUCT_ID order by 3 desc, 1
