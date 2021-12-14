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
