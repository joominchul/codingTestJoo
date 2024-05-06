-- https://school.programmers.co.kr/learn/courses/30/lessons/144854
SELECT b.BOOK_ID, a.AUTHOR_NAME, date_format(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE 
from BOOK as b, AUTHOR as a
where b.AUTHOR_ID = a.AUTHOR_ID and b.CATEGORY = '경제' 
order by PUBLISHED_DATE asc;
