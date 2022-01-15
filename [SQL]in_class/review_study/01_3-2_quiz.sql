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

-- (2) 3년 뒤를 날짜 더하기로 구한다면
SELECT SYSDATE + 365*3
FROM DUAL;



-- 특정 날짜 기준으로 그 달 말일의 요일 구하기

SELECT TO_CHAR(LAST_DATE(TO_DATE('2022-01-14')), 'DAY') AS lastday
FROM DUAL;



-- 2021년 10월 31일은 서기가 시작된 이후 몇 일이 지난 걸까

-- (1)
SELECT TO_DATE('2021-10-31') - TO_DATE('0001-01-01') -- 내가 한 것
FROM DUAL;

-- (2)
SELECT TO_DATE('2021-10-31', 'YYYY-MM-DD') - TO_DATE('0001-01-01', 'YYYY-MM-DD') -- 전답
FROM DUAL;
