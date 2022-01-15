-- NVL과 DECODE 를 활용해 CASE 표현식을 바꿔보기
SELECT employee_id, first_name, last_name, salary , commission_pct,
       CASE WHEN commission_pct IS NULL THEN salary
         ELSE salary + (salary* commission_pct)
       END real_salary
FROM employees;

-- (1) NVL
SELECT employee_id, first_name, last_name, salary , commission_pct,
    salary + salary * NVL(commission_pct, 0) AS real_salary
FROM employees;

-- (2) DECODE
SELECT employee_id, first_name, last_name, salary , commission_pct,
    DECODE(commission_pct, NULL, salary, salary + salary*commission_pct) AS real_salary
FROM employees;    


-- 오늘 이후 1년 날짜 구하기

-- (1)
SELECT ADD_MONTHS(SYSDATE, 12)
FROM DUAL;

--(2)
SELECT SYSDATE + 365
FROM DUAL;


-- 특정 날짜 기준으로 그 달 말일의 요일 구하기

SELECT TO_CHAR(LAST_DATE(TO_DATE('2022-01-14')), 'DAY') AS lastday
FROM DUAL;
