CREATE USER ORAUSER IDENTIFIED BY angela;

GRANT CREATE SESSION TO ORAUSER;

-- 들어온 사람은 이렇게 쓸 수 있다
SELECT USER FROM DUAL;

SELECT *
FROM USER_TABLES;


-- 날짜 타입 변경하기
SELECT SYSDATE FROM DUAL;



-- table 만들기 예시

CREATE TABLE EMP (
    EMP_NO VARCHAR2(30) NOT NULL,
    EMP_NAME VARCHAR2(80) NOt NULL,
    SALARY NUMBER       NULL,
    HIRE_DATE DATE      NULL
);

-- 결과창

명령의 1 행에서 시작하는 중 오류 발생 -
CREATE TABLE EMP (
    EMP_NO VARCHAR2(30) NOT NULL,
    EMP_NAME VARCHAR2(80) NOt NULL,
    SALARY NUMBER       NULL,
    HIRE_DATE DATE      NULL
)
오류 보고 -
ORA-01031: 권한이 불충분합니다
01031. 00000 -  "insufficient privileges"
*Cause:    An attempt was made to perform a database operation without
           the necessary privileges.
*Action:   Ask your database administrator or designated security
           administrator to grant you the necessary privileges
           
           
           
