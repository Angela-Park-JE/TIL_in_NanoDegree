--2차시 과제

-- first_name이 'David' 이고, 급여가 6000이상인 사람이 속한 부서가 위치한 도시를 찾는 문장을 3개의 문장으로.
-- MINE:
SELECT employees.first_name, employees.last_name, employees.department_id, departments.location_id, locations.city
    FROM employees, departments, locations
WHERE employees.department_id = departments.department_id 
    AND departments.location_id = locations.location_id 
    AND employees.first_name = 'David'
    AND salary.employees >= 6000;
    
-- TEACHER: 세 문장의 기준은 SELECT로 시작하는 쿼리문 세 개.
SELECT *
FROM employees
WHERE first_name = 'David' AND salary >= 6000;

SELECT *
FROM departments
WHERE department_id = 80;

SELECT *
FROM locations
WHERE location_id = 2500;


-- commission_pct가 있고없고에 따라 다른 real_salary 계산하는 문장 쓰기
-- MINE:
SELECT employee_id, first_name, last_name, salary, commision_pct,
    CASE WHEN commission_pct IS NULL THEN salary
        WHEN commission_pct IS NOT NULL THEN salary + (salary*commission_pct)
    END AS total_salary
FROM employees;

-- TEACHER: ELSE로 간단하게 줄인다.
SELECT employee_id, first_name, last_name, salary, commision_pct,
    CASE WHEN commission_pct IS NULL THEN salary
        ELSE salary + (salary*commission_pct)
    END real_salary
FROM employees;


-- 우편번호가 없는 건은 우편번호를 '99999'라는 임의의 수로 나오도록 조회하는 문장 쓰기
-- MINE: 손코딩하면서 엄청난 오류를 범해버렸다. 컬럼을 두 번 정했다. 
SELECT postal_code || ' - ' || street_address || ' - ' || city || ' - ' || state_province || ' - ' || country_id AS 주소
    CASE WHEN postal_code IS NULL THEN '99999' 
        ELSE postal_code 
    END || ' - ' || street_address || ' - ' || city || ' - ' || state_province || ' - ' || country_id AS 주소
FROM locations
WHERE country_id = 'UK'

-- TEACHER: 
SELECT CASE WHEN postal_code IS NULL THEN '99999' 
        ELSE postal_code 
    END || ' - ' || street_address || ' - ' || city || ' - ' || state_province || ' - ' || country_id AS 주소
FROM locations
WHERE country_id = 'UK'
ORDER BY 1;
