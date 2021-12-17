-- 3차시 과제 리뷰

-- 문장 뒤의 8글자 잘라오기
--> 방법1: 직접 위치를 세서 파라메터를 한 개 더 쓸 수 있지만 뒤에서 자를 땐 음수 형식으로 쓰기
SELECT SUBSTR('Is this the real life? Is this just fantasy?', -8)
FROM DUAL;
--> 방법2: 글자 검색해서 데려오기
SELECT SUBSTR('Is this the real life? Is this just fantasy?', 
    INSTR('Is this the real life? Is this just fantasy?', 'fant'))
FROM DUAL;


-- 현재 일자 기준 익울 1일을 반환하는 SELECT 문 쓰기
--> MINE: 날자를 반올림할 생각함
SELECT ROUNT(LAST_DAY(SYSDATE),'MM')
FROM DUAL;

--> TEACHER: 말일에 +1 만 하면 됨
SELECT LAST_DAY(SYSDATE) +1
FROM DUAL;


-- 2023년 8월 20일 기준으로 그 달의 마지막 날짜의 요일 구하기
--> MINE:
SELECT TO_CHAR(LAST_DAY(TO_DATE('2023-08-20', 'YYYY-MM-DD')),'DL')
FROM DUAL;
-- 결과: 2023년 8월 31일 목요일

--> TEACHER: 'DAY'는 함수이고 'DL'은 표시 법에 가까운듯...?
SELECT TO_CHAR(LAST_DAY(TO_DATE('2023-08-20', 'YYYY-MM-DD')),'DAY')
FROM DUAL;
-- 결과: 목요일


--* 다음 문장에서 CASE 표현식을 NVL 함수로 변환하기
SELECT employee_id, first_name, last_name, salary, commission_pct,
    CASE WHEN commission_pct IS NULL THEN salary
        ELSE salary + (salary*commission_pct)
    END real_salary
FROM employees;
--> MINE: NVL로 어떻게 해...? 하면서 NVL2를 씀. 결과가 다르진 않다.
SELECT employee_id, first_name, last_name, salary, commission_pct,
    NVL2(commission_pct, salary+(salary*commission_pct), salary) AS real_salary
FROM employees;

--> TEACHER: NVL로 가능하다. 
SELECT employee_id, first_name, last_name, salary, commission_pct,
    salary + salary * NVL(commission_pct, 0) AS real_salary
FROM employees;

-- 잠시 헷갈린 것: NULL은 + -도 되지 않는다. 무조건 모든 연산을 0으로 만들어버린다.
SELECT (NULL * 3) + 3 AS res1, (NULL + 3) + 3 AS res2
FROM DUAL;
-- 결과: res1 과 res2 모두 null
-- NVL(commission_pct, 0) - 커미션이 NULL이면 0을 쓴다는 뜻이기 때문에 NULL연산이 아니다.


-- 이전 문제의 CASE 표현식을 DECODE로 변환하기
--> MINE: 결과는 같음.
SELECT employee_id, first_name, last_name, salary, commission_pct,
    DECODE(commission_pct, NULL, salary, salary+(salary*commission_pct)) AS real_salary
FROM employees;

--> TEACHER: NVL과 같은 맥락으로, 함수를 바로 연산에 넣는다.
SELECT employee_id, first_name, last_name, salary, commission_pct,
    salary + salary * DECODE(commission_pct, NULL, 0, commission_pct) AS real_salary
FROM employees;


-- 2021년 10월 31일은 서기가 시작된 후 몇 일이나 지났을까.
--> MINE: 돌아가지도 않는다. 
SELECT TO_NUMBER(TO_CHAR('2021-10-31', 'DDD')) + 2020*365
FROM DUAL; 

--> TEACHER: 


