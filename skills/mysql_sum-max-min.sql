-- https://school.programmers.co.kr/learn/courses/30/lessons/131115
SELECT *
FROM FOOD_PRODUCT
WHERE
    PRICE = ( SELECT MAX(PRICE) FROM FOOD_PRODUCT ) -- max를 먼저 찾고 컬럼에 맞게 짠다.

SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE FROM FOOD_PRODUCT ORDER BY PRICE DESC LIMIT 1; -- 정렬에서 첫번째가 가장 max

-- https://school.programmers.co.kr/learn/courses/30/lessons/59038
SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1; -- 최솟값 찾기 MIN() == ORDER BY 컬럼 ASC LIMIT 1;

-- 중복제거 https://school.programmers.co.kr/learn/courses/30/lessons/59408
SELECT COUNT(DISTINCT(NAME)) AS COUNT FROM ANIMAL_INS -- 중복제거 DISTINCT !!

select count(AI.name) -- 중복제거를 GROUP BY로 하는 방법
from 
    (SELECT name
    from ANIMAL_INS
    group by name) AI
