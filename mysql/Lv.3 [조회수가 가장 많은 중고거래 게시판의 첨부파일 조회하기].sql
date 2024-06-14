-- https://school.programmers.co.kr/learn/courses/30/lessons/164671
with v as (SELECT BOARD_ID from USED_GOODS_BOARD order by VIEWS desc limit 1)
select concat("/home/grep/src/",f.BOARD_ID, "/", f.FILE_ID, f.FILE_NAME, f.FILE_EXT) as FILE_PATH from USED_GOODS_FILE as f, v where f.BOARD_ID = v.BOARD_ID order by f.FILE_ID desc
