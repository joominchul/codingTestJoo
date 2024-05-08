-- https://school.programmers.co.kr/learn/courses/30/lessons/131534
with a as (select USER_ID from USER_INFO where year(JOINED) = 2021)
, b as (select year(SALES_DATE) as YEAR, month(SALES_DATE) as MONTH, USER_ID FROM ONLINE_SALE WHERE user_id IN (SELECT * FROM A))
select YEAR, MONTH, count(DISTINCT USER_ID) as PUCHASED_USERS, ROUND(count(DISTINCT(user_id)) / (SELECT COUNT(user_id) FROM A), 1) as PUCHASED_RATIO from b
group by 1,2
order by 1,2
