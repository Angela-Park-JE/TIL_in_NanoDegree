-- -- SELECT 문 -- --

SELECT COL1, COL2 ...
FROM TABLE_NAME -- 여기까지만 써도 불러올 수 있음
WHERE CONDITION1 -- 조건이 필요할 때
ORDER BY ORDER_CONDITION; -- 정렬이 필요할 때

-- 테이블 데이터 전체 조회
SELECT *
FROM EMPLOYEES;

-- 테이블 컬럼 선택해서 조회
SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, SALARY 
  --순서는 임의로 정해줄 수 있다.
FROM EMPLOYEES;


-- -- WHERE 절 -- --

-- WHERE 조건 걸기
  -- 사번이 100번인 사원 조회
  SELECT *
  FROM EMPLOYEES
  WHERE EMPLOYEE_ID = 100; -- 한 값만 나오는 건 사운 테이블에서 사번은 PK이기 때문이다.
  
  -- 사번이 100번이 아닌 사회 조회
  SELECT *
  FROM EMPLOYEES
  WHERE EMPLOYEE_ID <> 100;

  -- 사번이 100보다 크고 JOB_ID가 ST_CLERK인 사원 조회
  SELECT *
  FROM EMPLOYEES
  WHERE EMPLOYEE_ID > 100 
      AND jOB_ID = 'ST_CLERK' ;
  
  -- 급여가 2400 이하이거나 20000이상인 사원 조회
  SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, SALARY
  FROM EMPLOYEES
  WHERE SALARY <=2400 
    OR SALARY >= 20000 ;


-- -- ORDER BY 절 -- --
SELECT *
FROM TABLE_NAME
WHERE
ORDER BY CO21[ASC|DESC] , COL2[ASC|DESC], ...

-- 기본적으로 오름차순 정렬이다. ASC 는 생략되어있는 것이다.

-- ORDER BY 에 두개 이상 넣을 떄 적는 순서가 중요하다. 먼저 적은 것 순서대로 정렬한다.
  SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, SALARY
  FROM EMPLOYEES
  ORDER BY FIRST_NAME, LAST_NAME ;

-- 사원의 사번과 이름, 급여를 급여가 5000이상인 급여가 높은 순서로 보고싶다.
  SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, SALARY
  FROM EMPLOYEES
  WHERE SALARY >=5000 
  ORDER BY SALARY DESC ;
  
-- ORDER BY 에 숫자를 명시할 수 있다
  -- 해당 테이블의 두번째 컬럼 순, 세번째 컬럼 역순으로 정렬하기.
    SELECT * 
    FROM EMPLOYEES
    ORDER BY 2, 3 DESC

-- 불러오는 상태에서 특정 컬럼 명을 지정해서는 SELECT에 없어도 정렬이 가능하다. 
  SELECT COL1, COL2, COL3, COL4
  FROM TABLE_NAME
  ORDER BY 2, 3, COL5;
  -- 오류는 없지만 잘못 작성된, 의미가 없는 것이라고 하신다.

-- COMMISSION_PCT 컬럼으로 오름차순 정렬
  SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, COMMISSION_PCT
  FROM EMPLOYEES
  ORDER BY COMMISISION_PCT ;

-- NULL 값이 있는 로우가 먼저 밀린다. 오라클에서는 NULL이 큰 값으로 쓴다.
-- 만약 오름차순에서 NULL이 가장 작은 값으로 간주하고 싶다면
  SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, COMMISSION_PCT
  FROM EMPLOYEES
  ORDER BY COMMISSION_PCT NULLS FIRST;
-- NULL 이 먼저 나오고 NOT NULL들은 오름차순으로 나온다.
-- 비교적 최근에 나온 기능이라 실제로 쓰는 사람이 많지 않다고.
