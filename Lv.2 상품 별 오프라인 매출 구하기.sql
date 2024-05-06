-- https://school.programmers.co.kr/learn/courses/30/lessons/131533
SELECT p.product_code, sum(o.SALES_AMOUNT * p.PRICE) as SALES 
from PRODUCT as p, OFFLINE_SALE as o
where p.PRODUCT_ID = o.PRODUCT_ID group by p.PRODUCT_ID
order by SALES desc, p.product_code;
