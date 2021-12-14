-- SQL 3차시 정리

-- 1. 함수

-- 숫자형 함수
SELECT ABS(n) --* 절대값 반환
SELECT CEIL(n)/FLOOR(n) -- 같거나 큰 최소 정수 / 같거나 작은 최대 정수
SELECT EXP(n) -- e의 n승 반환
SELECT LN(n) -- n의 자연로그 반환
SELECT LOG(n2, n1) -- n2는 밑, n1은 진수. n1은 양수 n2는 1과 0이 아닌 양수
SELECT MOD(n2, n1) --* n2를 n1으로 나눈 나머지 반환
SELECT POWER(n2, n1) -- n2의 n1승 반환
SELECT ROUND(n, i) --* n의 소수점 기준 (i+1)번째에서 반올림.
SELECT SIGN(n) -- 양수면 1, 음수면 -1, 0 = 0 반환
SELECT SQRT(n) -- n의 제곱근 반환
SELECT TRUNC(n1, n2) --* n1의 소수점 기준 n2자리에서 절사. 생략시 0.

-- 문자형 함수
SELECT CONCAT(chr1, chr2) -- 두 문자 결합
SELECT INITCAP(chr) -- chr의 첫 번째 문자를 대문자로 변환
SELECT UPPER(chr)/LOWER(chr) --* 전부 대/소문자로 ㅂㄴ환
SELECT LPAD(expr1, n, expr2)/RPAD(expr1, n, expr2) -- expr1를 반환하는데 expr2를 (n-expr1길이) 만큼 왼쪽/오른쪽을 채워 반환
SELECT LTRIM(exper1, expr2)/RTRIM(exper1, expr2) -- 왼쪽/오른쪽에서 expr2를 제거
SELECT SUBSTR(chr, n1, n2) --* chr의 n1번째에서 시작해서 n2만큼 잘라낸 결과 반환. n1이 음수면 끝에서 부터. n2 생략시 시작부터 전부.
SELECT TRIM(chr) --* 양쪽 끝의 공백 제거
SELECT ASCII(chr) -- ASCII코드값 
SELECT LENGTH(chr) --* 문자의 글자 수 반환
SELECT LENGTHB(chr) -- 문자의 바이트수 변환
SELECT REPLACE(chr, serch_str, rep_str) --* serch_str을 찾아서 rep_str로 대체
SELECT INSTR(chr1, chr2, n1, n2) --* chr1 에서 chr2를 찾아서 시작 위치 반환. n1은 몇 번째부터, n2는 찾은 것중 몇 번째를 가져올 것인지.
