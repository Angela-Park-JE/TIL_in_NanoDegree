-- 1. 집코드 살펴보기

-- city 와 state를 살펴보기
SELECT customer_zip_code_prefix, customer_city, customer_state
FROM CUSTOMERS
--GROUP BY CUSTOMER_CITY
ORDER BY customer_zip_code_prefix;


-- 몇 개의 도시가 있지?
SELECT SUM(city_num)
FROM
    (SELECT customer_state, COUNT(customer_city) as city_num
     FROM CUSTOMERS
     GROUP BY customer_state
     ORDER BY customer_state)
     ;
 ```
 99441 개라는데 브라질이 이런 나라였어?
 ```


-- 도시별 집코드가 몇개가 있을까?
SELECT customer_state, customer_city, COUNT(customer_zip_code_prefix)
FROM CUSTOMERS
GROUP BY customer_state, customer_city
--    HAVING LENGTH(AVG(TO_NUMBER(customer_zip_code_prefix)))>5   -- 도시별 집코드의 평균이 5개 이상인 곳 
ORDER BY customer_state;


-- 주별 평균 고객수
SELECT AVG(COUNT(customer_zip_code_prefix)) AS "주별 평균 고객수"
FROM CUSTOMERS
GROUP BY customer_state;
```
3683 명
```



-- 2. 예시: rio branco를 데려와보자

-- 이 도시 전체 집코드 개수
SELECT customer_state, customer_city, 
--       customer_zip_code_prefix, 
       COUNT(customer_zip_code_prefix)
FROM CUSTOMERS
WHERE  1=1
    AND customer_state IN ('AC') 
    AND customer_city = 'rio branco'
GROUP BY customer_state, customer_city
ORDER BY customer_state;
```
AC	rio branco	70
```


-- 3. CUSTOMER_ID와 CUSTOMER_UNIQUE_ID 

-- 두 개 이상의 customer_id를 가진 unique_id
SELECT customer_unique_id, count(customer_id)
FROM customers
GROUP BY customer_unique_id
    HAVING count(customer_id)>1
ORDER BY customer_unique_id;


-- 두 개 이상의 customer_id를 가진 unique_id 개수 (재구매이력이 있는 unique_id)
SELECT COUNT(*)
FROM
    (SELECT customer_unique_id, count(customer_id)
     FROM customers
     GROUP BY customer_unique_id
         HAVING count(customer_id)>1
     ORDER BY customer_unique_id)
     ;
```
결과는 2997
```
