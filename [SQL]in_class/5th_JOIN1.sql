-- 5차시 1

--1. 조인
---- FROM 절에 조인에 참여할 테이블 명시, 그리고 Alias를 주는 것이 좋음
---- 모든 컬럼은 alias.컬럼명 형태로 사용
---- WHERE 절에서는 조인 조건과 일반 조건 함께 사용

--2. INNER JOIN
---- 조인 조건에 만족하는 컬럼만 조회


--3. INNER JOIN1
SELECT a.employee_id, a. first_name, a.department_id, b.department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id
ORDER BY a.department_id;
---- department 컬럼이 NULL 인 건 1건 제외하고 전부 나온다.
---- SELECT count(1) FROM employees : 총 로우수를 한줄로 가져오는 쿼리


--4. INNER JOIN2
SELECT a.employee_id, a.first_name || ' ' || a.last_name AS emp_names, b.job_title, c.department_it, c.department_name
FROM employees a, jobs b, departments c
WHERE 1=1
	AND a.job_id = b.job_id
	AND a.department_id = c.department_id
ORDER BY 1;
---- 내부 조인은 쉽다.


--5. OUTER JOIN
---- 조인 조건에 만족하지 않는 데이터(로우) 까지 포함해 조회 
---- 조인 조건에 (+) 을 붙여야함. (오라클에만 있음)
---- (+)가 안붙은 쪽의 데이터까지 조회하는 방식이다.


--6. OUTER JOIN1
SELECT a.employee_id AS emp_id, a.first_name || ' ' || a.last_name AS emp_names, a.department_id AS a_dept_id, b.department_id AS b_dept_id, b.department_name
FROM employees a, departments b
WHERE a.department_id(+) = b.department_id 
ORDER BY a.department_id;


--7. OUTER JOIN2
SELECT a.employee_id AS emp_id, a.first_name || ' ' || a.last_name AS emp_names, a.department_id AS dept_id, c.department_name, d.location_id, d.street_address, d.city
FROM employees a, departments c, locations d
WHERE a.department_id = c.department_id (+)
	AND c.location_id = d.location_id(+)
ORDER BY 1;


-- 8. 샘플 파일 넣고 F5하기

