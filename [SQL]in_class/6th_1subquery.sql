-- 6차시 서브쿼리

--1. 서브쿼리
---- SELECT 안에 SELECT 문장이 또있는 형태


-- 2. 스칼라 서브쿼리
SELECT a.employee_id, a.first_name||a.last_name emp_name, a.department_id, 
    (SELECT b.department_name 
        FROM departments b
        WHERE a.department_id = b.department_id) dept_name
FROM employees a
ORDER BY 1;
---- 부서명처럼 특정 코드 명칭을 타 테이블에서 가져올 때 스칼라 서브쿼리를 사용하는 경우가 많다.


--3. 인라인뷰
SELECT a.employee_id,  a.first_name||a.last_name emp_name, a.department_id, c.dept_name
FROM  employees a,
    (SELECT b.department_id, b.department_name dept_name
    FROM departments b) c
WHERE a.department_id = c.department_id
ORDER BY 1;


--4. 중첩 서브쿼리
SELECT *
FROM departments a
WHERE EXISTS
    (SELECT 1
    FROM employees b
    WHERE a.department_id = b.department_id
    );
    -- exists 는 in과 비슷한 역할을 한다.


--5. 세미조인  


--6. 안티조인
SELECT *
FROM departments a
WHERE NOT EXISTS
    (SELECT 1
    FROM employees b
    WHERE a.department_id = b.department_id
    );
   
