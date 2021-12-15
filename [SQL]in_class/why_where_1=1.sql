-- 왜 WHERE 1=1을 쓸까?

SELECT JOB_ID
FROM EMPLOYEES
WHERE 1=1
AND SALARY >=3000;

-- 여러 조건들을 하나하나 따져 볼때 첫 번째 조건을 잠시 주석 하는 경우 뒤의 AND를 썼다 지웠다 해야해서.
