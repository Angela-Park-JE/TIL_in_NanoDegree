CREATE USER ORAUSER IDENTIFIED BY angela;

GRANT CREATE SESSION TO ORAUSER;

-- 들어온 사람은 이렇게 쓸 수 있다
SELECT USER FROM DUAL;

SELECT *
FROM USER_TABLES;


-- 날짜 타입 변경하기
SELECT SYSDATE FROM DUAL;

