-- https://school.programmers.co.kr/learn/courses/30/lessons/59414
SELECT ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d') as '날짜' from ANIMAL_INS order by 1
