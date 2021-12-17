SELECT employees.first_name, employees.last_name, employees.department_id, departments.location_id, locations.city
    FROM employees, departments, locations
WHERE employees.department_id = departments.department_id 
    AND departments.location_id = locations.location_id 
    AND employees.first_name = 'David'
    AND salary.employees >= 6000;


-- 강사님 정답, 세 문장의 기준은 SELECT로 시작하는 쿼리문 세 개.
SELECT *
FROM employees
WHERE first_name = 'David' AND salary >= 6000;

SELECT *
FROM departments
WHERE department_id = 80;

SELECT *
FROM locations
WHERE location_id = 2500;
