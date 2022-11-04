-- https://school.programmers.co.kr/learn/courses/30/lessons/131115
SELECT *
FROM FOOD_PRODUCT
WHERE
    PRICE = ( SELECT MAX(PRICE) FROM FOOD_PRODUCT ) -- max를 먼저 찾고 컬럼에 맞게 짠다.

SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE FROM FOOD_PRODUCT ORDER BY PRICE DESC LIMIT 1; -- 정렬에서 첫번째가 가장 max
