
-- city 엉망을 고쳐보자
```
-- ~연습장~!
create table new_emp as
select empno,ename,sal from emp where dmpno>7700 ;

똑같은 테이블 구조로 해당 데이터까지 생성
create table new_emp as
select empno,ename,sal from emp where dmpno>7700 and 1=3;
```


-- 카테고리명 영어로 보이게 하여서 카테고리 별 카운트
WITH cate_eng AS(
    SELECT p.product_id, p.category AS cate_por, c.category_name_english AS category_name, 
           p.name_length, p.description_length, p.photos_qty, p.weight_g, p.length_cm, p.height_cm, p.width_cm
    FROM products p
    LEFT JOIN categories c ON p.category  = c.category_name (+))

SELECT cate_por, count(*)
FROM cate_eng
GROUP BY cate_por;


-- 영문 카테고리 이름과 함꼐 물건 살펴보기
SELECT p.product_id, p.category AS cate_por, 
       c.category_name_english AS category_name, 
       p.name_length, p.description_length, p.photos_qty, p.weight_g, p.length_cm, p.height_cm, p.width_cm
FROM products p, categories c
WHERE p.category = c.category_name (+);


-- 카테고리 이름이 null이 있는가 
SELECT p.product_id, p.category AS cate_por, c.category_name_english AS category_name, 
    p.name_length, p.description_length, p.photos_qty, p.weight_g, p.length_cm, p.height_cm, p.width_cm
FROM products p
LEFT JOIN categories c ON p.category  = c.category_name (+)
ORDER BY 2 NULLS FIRST;


```
=IF([@[FALSE=0]]=1,[@[geolocation_city]],VLOOKUP([@[geolocation_zip_code_prefix]],[geolocation_zip_code_prefix],4))
```

