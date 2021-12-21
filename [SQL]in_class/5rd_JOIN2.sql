-- 5차시 정리 2:  ANSI 표준 문법, cartesian product, self join

--1. ANSI 조인
---- OUTER JOIN 에서 OUTER 는 생략 가능하다.


--2. ANSI 내부 조인 
SELECT a.employee_id, a.first_name, a.department_id, b.department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id
ORDER BY a.department_id;

-->이것이 이렇게 바뀐다
SELECT a.employee_id, a. first_name, a.department_id, b.department_name
FROM employees a, departments b
INNER JOIN departments b
	ON a.department_id = b.department_id
ORDER BY a.department_id;



--3. ANSI LEFT (OUTER) JOIN
SELECT a.employee_id, a.first_name, a.department_id, b.department_name
FROM employees a
LEFT JOIN departments b ON a.department_id = b.department_id
ORDER BY a.employee_id;



--4. ANSI RIGHT (OUTER) JOIN
SELECT a.employee_id, a.first_name, a.department_id, b.department_name
FROM employees a
RIGHT JOIN departments b ON a.department_id = b.department_id
ORDER BY a.employee_id;


--5. ANSI FULL OUTER JOIN
SELECT a.employee_id, a.first_name, a.department_id, b.department_name
FROM employees a
FULL OUTER JOIN departments b ON a.department_id = b.department_id
ORDER BY a.employee_id;


--6. 다중 조인
SELECT a.employee_id, a.first_name || ' ' || a.last_name AS emp_names, b.job_title, c.department_it, c.department_name
FROM employees a, jobs b, departments c
WHERE 1=1
	AND a.job_id = b.job_id
	AND a.department_id = c.department_id
ORDER BY 1;
--> 이것이 이렇게 바뀐다



-- 7. cartesian product
---- 조인 참여 테이블을 FROM 절에 기술하고 WHERE 절에 조인 조건 기술하지 않음
---- 두 테이블 기준 모든 조합(경우의 수)가 조회됨
---- 거의 사용되지 않음



-- 8. self join
---- 자기 자신(동일한 테이블)끼리 조인.
SELECT a.employee_id,
	a.first_name || ' ' || a.last_name AS emp_name,
	a.manager_id,
	b.first_name || ' ' || a.last_name AS manager_name
FROM employees a, employees b
WHERE a.manager_id = b.employee_id
ORDER BY 1;
