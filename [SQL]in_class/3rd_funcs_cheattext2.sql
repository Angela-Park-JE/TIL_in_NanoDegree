-- SQL 3차시 정리2

-- 2. 형변환 함수

-- 묵시적 형변환: 오라클이 자동으로 형변환
SELECT *
	FROM employees
	WHERE hire_date = '2003-06-16';
-- 숫자형 문자와 숫자 비교시, 문자를 숫자로 변환해 비교
-- 날짜형 문자와 날짜 비교시, 문자를 날짜로 변환해 비교

-- 명시적 형변환
-- 사용자가 함수로 직접 변환. 가급적 명시적 형변환 해야 함.

--* 형변환 함수 *
TO_NUMBER(char) -- 숫자형 문자를 숫자로 변환
TO_CHAR(n, number_format) -- 숫자 n을 number_format에 맞게 문자로 변환. number_format 생략 가능.
TO_CHAR(date, date_format) -- 날짜 date을 date_format에 맞게 문자로 변환. date_format 생략 가능.
TO_DATE(char, date_format) -- 문자 char을 date_format에 맞게 문자로 변환. date_format 생략가능.

-- 숫자 변환 형식
9 -- 한 자리 숫자. 실제 숫자의 자리수와 같거나 크게 명시해야함.

-- 날짜 변환 형식
DDD -- 365일 중 몇 번째 날인지, 일을 1월 1일 기준으로 날짜.
DL -- 일을 요일까지 표현.
HH, HH2 -- 시간을 01, 02... 로 표현
MI -- 분
SS -- 초
WW -- week
W -- 해당 월 몇 번째 주

-- NULL 처리 함수
NVL(expr1, expr2) --* expr1가 NULL이면 expr2 반환
NVL2(expr1, expr2, expr3) -- expr1가 NULL이면 expr 3, NOT NULL이면 expr2 를 반환
COALESCE(expr1, expr2, ...) -- expr1, expr2, expr3 ... 에서 첫 번째로 NULL이 아닌 값 반환
NULLIF(expr1, expr2) -- expr1 같으면 NULL, 같지 않으면 expr1 반환

-- 기타 함수
DECODE(expr1, val1, result1, val2, result2, ... , default_value)
-- expr1 =val1이면 result1, =val2이면 result2, 일치하는 값이 없으면 default_value 반환
-- default_value 생략시 NULL 반환, 단순형 CASE 표현식과 같음.
