-- https://school.programmers.co.kr/learn/courses/30/lessons/133025
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, "NONE") as TLNO -- 전화번호가 null 일 경우 NONE로 대체
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W' -- 12살이하 성별이 여
ORDER BY AGE DESC, PT_NAME ASC

-- https://school.programmers.co.kr/learn/courses/30/lessons/133025
-- 다른 두 테이블에서 같은 키로 테이블당 조건으 가져올 때
SELECT FH.FLAVOR
FROM FIRST_HALF FH, ICECREAM_INFO II -- 조건1 테이블 한개, 조건2 테이블 다른 한개
WHERE FH.FLAVOR = II.FLAVOR  -- 키 값 공유
      AND FH.TOTAL_ORDER > 3000  -- 서로 다른 조건
      AND II.INGREDIENT_TYPE = 'fruit_based'  -- 서로 다른 조건
ORDER BY FH.TOTAL_ORDER DESC

-- https://school.programmers.co.kr/learn/courses/30/lessons/132203
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD,'%Y-%m-%d') -- 날짜포멧
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC -- ASC 오름차순 DESE 내림차순

-- https://school.programmers.co.kr/learn/courses/30/lessons/131120
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') AS DATE_OF_BIRTH -- 날짜포멧
FROM MEMBER_PROFILE
WHERE GENDER = 'W' AND DATE_FORMAT(DATE_OF_BIRTH,'%m') = '03'/* MONTH(DATE_OF_BIRTH) = 3 */ AND TLNO IS NOT NULL -- 여성,생일 3월, < AND NOT "컬럼" IS NULL > -- NULL 제외
ORDER BY MEMBER_ID ASC

SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE 'A%' --A로 시작하는 문자를 찾기
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '%A' --A로 끝나는 문자 찾기
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '%A%' --A를 포함하는 문자 찾기
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE 'A_' --A로 시작하는 두글자 문자 찾기
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE'[^A]' --첫번째 문자가 'A''가 아닌 모든 문자열 찾기

SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '[ABC]' --첫번째 문자가 'A'또는'B'또는'C'인 문자열 찾기
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '[A-C]'

-- https://school.programmers.co.kr/questions/38243
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도%'
ORDER BY FACTORY_ID ASC

-- https://school.programmers.co.kr/learn/courses/30/lessons/131118
SELECT RI.REST_ID, RI.REST_NAME, RI.FOOD_TYPE, RI.FAVORITES, RI.ADDRESS, ROUND(AVG(RR.REVIEW_SCORE),2) AS SCORE -- 평균내기
FROM REST_INFO RI, REST_REVIEW RR
WHERE RI.REST_ID = RR.REST_ID 
AND RI.ADDRESS LIKE '서울%' --서울로 시작하는 컬럼
GROUP BY RI.REST_NAME -- SUM(), AVG() 에 필수로!!!
ORDER BY SCORE DESC, RI.FAVORITES DESC

SELECT 컬럼A, SUM(컬럼B)  /* ----   SUM을쓰거나 AVG 쓸때는 GROUB BY 필수!!! */
FROM cookie_sales         /*    ㅣ    */        
GROUP BY 컬럼C            /* ----    */

-- https://school.programmers.co.kr/learn/courses/30/lessons/131535
SELECT COUNT(*) AS USERS -- 컬럼 수 카운팅, * = 모든
FROM USER_INFO
WHERE YEAR(JOINED) = 2021 AND AGE >= 20 AND AGE <= 29 -- 년도 2021, 나이 20살 이상 29살 이하

-- https://school.programmers.co.kr/learn/courses/30/lessons/59405
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1-- 가장 첫번째 limit 활용
SELECT NAME                                              -- 다른 풀이
FROM ANIMAL_INS 
WHERE DATETIME IN ( SELECT MIN (DATETIME) --  datetime 이 가장 작은 
                      FROM ANIMAL_INS);

-- https://school.programmers.co.kr/learn/courses/30/lessons/131536
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID -- 구분을 두개로 해야하기 때문에 구룹화, 재구매한 데이터를 구하기 위함
HAVING COUNT(*) > 1 -- 구룹화 한것 중에 카운팅, 재구매한 데이터를 구하기 위함
ORDER BY USER_ID ASC, PRODUCT_ID DESC -- 정렬

-- 첫번째 정답 https://school.programmers.co.kr/learn/courses/30/lessons/131537
SELECT DATE_FORMAT(OS.SALES_DATE,'%Y-%m-%d') AS SALES_DATE, 
       OS.PRODUCT_ID,
       OS.USER_ID,
       OS.SALES_AMOUNT
FROM (
    SELECT ONLINE_SALE_ID, USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE FROM ONLINE_SALE
    UNION ALL -- 중복 데이터도 추가, UNION 중복 데이터 삭제
    SELECT OFFLINE_SALE_ID, NULL, PRODUCT_ID, SALES_AMOUNT, SALES_DATE FROM OFFLINE_SALE
) OS
WHERE YEAR(OS.SALES_DATE) = 2022 AND MONTH(OS.SALES_DATE) = 3
ORDER BY OS.SALES_DATE, OS.PRODUCT_ID, OS.USER_ID

-- 두번째 정답
SELECT date_format(sales_date, "%Y-%m-%d") as sales_date, product_id, user_id, sales_amount
from online_sale
where sales_date like '2022-03%'
union
select date_format(sales_date, "%Y-%m-%d") as sales_date, product_id, NULL as user_id, sales_amount
from offline_sale
where sales_date like '2022-03%'
order by sales_date asc, product_id asc, user_id asc;
