
-- SQL 4차시 퀴즈


4-1-1.

SELECT COUNTRY_ID, COUNT(*)
FROM LOCATIONS
GROUP BY country_id;


4-1-2.

SELECT TO_CHAR(hire_date, 'Q') AS hired_quarter, COUNT(*)
FROM EMPLOYEES
GROUP BY TO_CHAR(hire_date, 'Q')
ORDER BY 1;


4-1-3.

SELECT job_id, ROUND(AVG(salary), 0) AS avg_salary,
FROM employees
GROUP BY job_id
ORDER BY 1;
-- 이것에서 직접 구하는 컬럼 추가하기
SELECT job_id, ROUND(AVG(salary), 0) AS avg_salary, 
    ROUND( SUM(salary)/COUNT(employee_id), 0) AS avg_salary1
FROM employees
GROUP BY job_id
ORDER BY 1;


4-1-4.

SELECT iso_code, TO_CHAR(dates, 'YYYY-MM') AS year_month,
    COUNT(new_cases) AS new_cases
FROM covid19_test
GROUP BY iso_code, TO_CHAR(dates, 'YYYY-MM')
    HAVING iso_code = 'KOR'
ORDER BY 2;


4-1-5.

--SELECT TO_CHAR(dates, 'YYYY-MM') AS "MONTHS", 
--    SUM(new_cases) AS 확진자수, SUM(new_deaths) AS 사망자수, 
--    CASE WHEN SUM(new_cases) = 0 THEN 0
--        WHEN SUM(new_cases) != 0 THEN ROUND(SUM(new_deaths)/SUM(new_cases)) END 사망율
--FROM COVID19_TEST
--WHERE iso_code = 'KOR'
--GROUP BY TO_CHAR(dates, 'YYYY-MM') AS "MONTHS";
--5번문제 미해결

----> 5차시 앞서 과제 리뷰!
--사망자수는 월별 new_deaths 합계
--디코드를 케이스로 바꾸기
CASE WHEN SUM(new_cases) = 0 THEN 0
    ELSE ROUND(SUM(new_deaths)/SUM(new_cases) * 100, 2 )


4-1-6.

SELECT TO_CHAR(dates, 'YYYY-MM'),iso_code, SUM(new_cases)
FROM covid19_test
WHERE TO_CHAR(dates, 'YYYY-MM') = '2020-10'
GROUP BY TO_CHAR(dates, 'YYYY-MM'),iso_code
ORDER BY SUM(new_cases) DESC NULLS LAST;



4-2-1.


SELECT TO_CHAR(dates, 'YYYY-MM'),iso_code, SUM(new_cases)
FROM covid19_test
WHERE TO_CHAR(dates, 'YYYY-MM') = '2020-10'
GROUP BY TO_CHAR(dates, 'YYYY-MM'),iso_code
ORDER BY SUM(new_cases) DESC NULLS LAST;


4-2-2.

SELECT employee_id, hire_date
FROM employees
WHERE TO_CHAR(hire_date, 'YYYY') = '2001'
UNION ALL
SELECT employee_id, hire_date
FROM employees
WHERE TO_CHAR(hire_date, 'YYYY') = '2003'
ORDER BY hire_date;

-- 리뷰: 실제로는, 보통은 이렇게 한다 굳이 union all 하지 않고 ㅋㅋ
SELECT employee_id, hire_date
FROM employees
WHERE TO_CHAR(hire_date, 'YYYY') IN ('2001', '2003')



4-2-3.

SELECT job_id, SUM(salary)
FROM employees
GROUP BY job_id
UNION
SELECT 'total', SUM(salary)
FROM employees
ORDER BY job_id

--
SELECT job_id, SUM(salary)
FROM employees
GROUP BY rollup(job_id)


4-2-4. 

SELECT ISO_CODE AS 국가코드, TO_CHAR(DATES, 'YYYY-MM') AS 연도월, SUM(NEW_CASES) AS 월별확진자
FROM COVID19_TEST
WHERE 1=1
    AND DATES >= TO_DATE('2020-01-01')
    AND DATES <= TO_DATE('2020-06-30')
GROUP BY ISO_CODE, TO_CHAR(DATES, 'YYYY-MM')
    HAVING SUM(NEW_CASES) >= 10000
ORDER BY TO_CHAR(DATES, 'YYYY-MM')


-- 문제 이해를 잘못했다. 다시하자


-- 까지 되지만 엮는데 문제가 있다. 국가만 알고 싶은 것이었다.


SELECT COUNTRY 
FROM COVID19_TEST
WHERE 1=1
   AND DATES >= TO_DATE('2020-01-01')
   AND DATES <= TO_DATE('2020-06-30')
GROUP BY COUNTRY, TO_CHAR(DATES, 'YYYY-MM')
   HAVING SUM(NEW_CASES) >= 10000
INTERSECT
SELECT COUNTRY
FROM COVID19_TEST
WHERE 1=1
   AND DATES >= TO_DATE('2020-07-01')
   AND DATES <= TO_DATE('2020-10-31')
GROUP BY COUNTRY, TO_CHAR(DATES, 'YYYY-MM')
   HAVING SUM(NEW_CASES) <= 1000;

HAVING 절에 NVL(SUM(new_cases),0) <= 1000;
