-- 4차시 정리 2: HAVING, DISTINCT, ROLLUP(), CUBE()


-- 1. HAVING 절
----  집계 쿼리에서 집계 함수 산출 값에 대한 조건을 걸 때 사용
----  일반적인 조건은 WHERE, 집계 쿼리에 대한 조건은 HAVING

-- 2. HAVING 절 예시: 입사년도 별 부서 별 인원수, 부서 총 salary, 평균 salary, 그 중 평균 연봉이 5000 이상 되는 사람들
SELECT TO_CHAR(hire_date, 'YYYY') AS hire_year, department_id, COUNT(*), SUM(salary), ROUND(AVG(salary),0)
FROM employees
GROUP B& TO_CHAR(hire_date, 'YYYY'), department_id
HAVING ROUND(AVG(salary),0) >= 5000
ORDER BY 1, 2;

-- 3. HAVING 절 예시: 입사년도 별 부서 별 인원수, 부서 총 salary, 평균 salary, 그 중 인원수가 1명이 아닌 결과
SELECT TO_CHAR(hire_date, 'YYYY') AS hire_year, department_id, COUNT(*), SUM(salary), ROUND(AVG(salary),0)
FROM employees
GROUP B& TO_CHAR(hire_date, 'YYYY'), department_id
HAVING COUNT(*) > 1
ORDER BY 1, 2;



-- 4. DISTINCT 
---- DISTINCT 뒤에 명시한 표현식(컬럼)의 고유한 값을 조회
---- 집계 함수 없이 GROUP BY 절만 사용하면, 원하는 컬럼이나 표현식의 고유한 값을 얻을 수 있는데,
---- 이때 DISTINCT 키워드를 대신 사용하면 GROUP BY 절 없이 SELECT절에 쓴 것만으로 동일한 결과를 얻을 수 있다.

-- 5. DISTINCT 예시: GROUP BY 대신 쓴 것
SELECT job_id
FROM employees
GROUP BY job_id ; 
--
SELECT DISTINCT job_id
FROM employees ;

-- 6. DISTINCT 예시: GROUP BY로 묶을 것을 SELECT에 바로 쓴 것
SELECT DISTINCT TO_CHAR(hire_date, 'YYYY') AS hire_year, department_id
FROM employees
ORDER BY 1, 2 ;



-- 7. ROLLUP(): 소계(sub total)
---- ROLLUP에 명시한 표현식 수 + 1개를 그룹으로 묶음
---- col1에 대한 소계, col1과 col2와 소계, 그리고 전체 합계
SELECT col1, col2, SUM(col3)
FROM table1
GROUP BY ROLLUP(col1, col2)...

-- 8. CUBE(): 가능한 모든 조합에 대한 소계
---- CUBE 절에 명시한 표현식 수(콤마로 구분된 수)가 n개면 2의 n승계의 조합
---- 결과가 많고 복잡하게 나와서 생각보다 많이 안쓴다.
SELECT col1, col2, SUM(col3)
FROM table1
GROUP BY CUBE(col1, col2) ...

-- 9. ROLLUP과 CUBE 예시: job_id 별 phone_number 별 salary의 합계 
SELECT SUBSTR(phone_number, 1, 3), -- phone_number 컬럼을 첫번째 부터 3자리 가져온다
    job_id, SUM(salary)
FROM employees
GROUP BY job_id, SUBSTR(phone_number, 1, 3)
ORDER BY 1, 2 ;

    ---- 이때 CUBE를 사용한다면
    SELECT SUBSTR(phone_number, 1, 3), job_id, SUM(salary)
    FROM employees
    GROUP BY 
        CUBE(SUBSTR(phone_number, 1, 3), job_id)
    ORDER BY 1, 2 ;
    ---- SUBSTR으로 묶은 것이 끝날 때마다 phone_number 별로 소계를 산출 한 뒤, 맨 뒤에 job_id 별로 소계를 또 산출한다.
    
    ---- 이때 ROLLUP을 사용한다면
    SELECT SUBSTR(phone_number, 1, 3), job_id, SUM(salary)
    FROM employees
    GROUP BY 
        ROLLUP(SUBSTR(phone_number, 1, 3), job_id)
    ORDER BY 1, 2 ;
    ---- SUBSTR으로 묶은 것이 끝날 때마다 phone_number 별로 소계를 산출 한 뒤, 맨 뒤에 모든 소계를 한 줄에 산출한다.
