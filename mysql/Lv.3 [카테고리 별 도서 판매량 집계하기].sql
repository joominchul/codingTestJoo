-- https://school.programmers.co.kr/learn/courses/30/lessons/144855
select CATEGORY, sum(SALES) as TOTAL_SALES
from BOOK b join BOOK_SALES s on b.BOOK_ID = s.BOOK_ID
where year(SALES_DATE) = '2022' and month(SALES_DATE) = '1'
group by CATEGORY order by 1;
