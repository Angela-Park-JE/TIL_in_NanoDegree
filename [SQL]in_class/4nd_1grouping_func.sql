-- 4차시 정리 1


-- 1. 집계 쿼리
---- GROUP BY 절과 집계 함수를 사용한 쿼리
---- 특정 항목(컬럼)별로 평군, 최소 최대, 합, 표중편차, 분산 등 통계값 산출
---- GROUP BY 절과 집계 함수 각각 단독 사용할 수 있지만 일반적으로 함께 사용


-- 2. GROUP BY
SELECT expr1, expr2...
FROM table
WHERE ...
GROUP BY expr1, expr2...
ORDER BY ... ;

-- GROUP BY 절에 기술한 컬럼, 표현식 이외의 항목을 SELECT 절에 명시 불가하다. 하지만 집계 함수는 가능
-- GROUP BY 절에는 SELECT 절에 적은 형태 그대로 사용해야 하며, alias는 사용할 수 없다.


-- 3. 집계 함수
COUNT( expr ) -- expr은 컬럼을 포함한 표현식으로, 전체 개수이므로 보통 * 사용. *은 COUNT함수에서만 사용.
MAX( expr ) -- 최댓값
MIN( expr ) -- 최솟값
SUM( expr ) -- 합계
AVG( expr ) -- 평균
STDDEV( expr ) -- 표준편차
VARIANCE( expr ) -- 분산

-- GROUP BY 절 없이 집계 함수만 사용 시, 조회되는 데이터 전체에 대한 집계 값 계산
-- GROUP BY 절 함께 사용시, GROUP BY 절에 명시한 항목 별 집계 값 계산
-- 집계 함수나 집계 함수가 포함된 절은 WHERE 절에서 사용 불가 (HAVING으로 해결 가능)


-- 4. GROUP BY절에 컬럼 하나를 두었을 때
SELECT job_id
FROM employees
GROUP BY job_id ;
-- job_id 컬럼 기준으로 집계하여 job_id 컬럼의 유일한 값들만 모아 보인다. 로우가 요약된다.

SELECT TO_CHAR(hire_date, 'YYYY') AS HIRE_YEAR
FROM employees
GROUP BY TO_CHAR(hire_date 'YYYY') ;
-- 입사년도 별 집계. 


-- 5. GROUP BY + 집계 함수 예시
SELECT job_id, COUNT(*), MIN(salary), MAX(salary)
FROM employees
GROUP BY job_id
ORDER BY job_id ;
-- job_id 별 - EMPLOYEES 내의 로우수, salary의 최솟값, salary의 최댓값

SELECT TO_CHAR(gire_date, 'YYYY') AS HIRE_YEAR, 
    department_id, COUNT(*), SUM(salary), ROUND(AVG(salary), 0)
FROM employees
WHERE TO_CHAR(hire_date, 'YYYY') >= '2004'
GROUP BY TO_CHAR(hire_date, 'YYYY'), department_id
ORDER BY 1, 2 ; 
-- 2004년 이후 입사한 사람들 중 입사년도 별 부서 별 인원수, 급여 총액, 급여 평균(정수)

