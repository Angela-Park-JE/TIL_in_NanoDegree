-- 4차시 정리 2


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
---- 집계 함수 없이 GROUP BY 절을 사용한 것과 동일한 효과
