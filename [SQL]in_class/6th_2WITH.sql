-- 6차시 2 WITH절과 TOP n query


--1. WITH절
WITH dept AS()


--2. 처리방식


--3. TOP n QUERY

---- 기존 방식
SELECT *
FROM ( 
	SELECT a.employee_id, a.first_name
	.........................)


--6-3 컬럼과 로우 서로 변환하기
--(1) CASE WHEN
--(2) DECODE
--(3) WITH
--(4) PIVOT절

-- 스코어 테이블 생성
CREATE TABLE score_table(
    YEARS VARCHAR2(4),
    GUBUN VARCHAR2(30),
    SUBJECTS VARCHAR2(30),
    SCORE NUMBER);
