-- (바르게 수정된) 셀러 테이블에서 주 별 셀러 수

SELECT "STATE" ,COUNT(seller_id)
FROM sellers_modi
GROUP BY "STATE";

-- 결과

PE	9
RN	5
AM	1
MG	244
RO	2
SE	2
CE	13
GO	40
MT	4
MS	5
PA	1
ES	23
PI	1
MA	1
DF	30
RS	129
PR	349
SC	190
AC	1
BA	19
PB	6
RJ	171
SP	1849



-- 고객 테이블에서 주 별 고객 수 (고유아이디)

SELECT customer_state ,COUNT(customer_unique_id)
FROM CUSTOMERS
GROUP BY customer_state;

-- 결과

