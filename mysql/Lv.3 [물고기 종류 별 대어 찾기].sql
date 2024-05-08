-- https://school.programmers.co.kr/learn/courses/30/lessons/293261
with a as(select FISH_TYPE as f, max(LENGTH) as m from FISH_INFO group by FISH_TYPE)
select id, FISH_NAME, LENGTH from FISH_INFO i join FISH_NAME_INFO n using(FISH_TYPE), a
where FISH_TYPE = a.f and LENGTH = a.m order by 1
