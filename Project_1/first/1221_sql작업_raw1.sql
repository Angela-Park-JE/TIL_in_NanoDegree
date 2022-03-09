
-- 카테고리 별 물건 수 (포르투갈어로 나옴)

SELECT p."CATEGORY", COUNT(oi.product_id)
FROM products p, sellers s, order_items oi, categories ct
WHERE p.product_id = oi.product_id
    AND oi.seller_id = s.seller_id
    AND p."CATEGORY" = ct."CATEGORY_NAME"
GROUP BY p."CATEGORY"
ORDER BY 2 DESC;


---- 파일로

-- 주문건의 소요 시간, 물건과 카테고리별 가격과 결제방식 
-- orders_items_prod_pay.csv 파일로 export
SELECT orders.*, order_items.seller_id, order_items.product_id, products."CATEGORY", order_items.price, order_payments.*
FROM orders, order_items , products, order_payments
WHERE 1=1 
    AND orders.order_id = order_items.order_id 
    AND order_items.product_id = products.product_id
    AND orders.order_id = order_payments.order_id
ORDER BY orders.purchase_timestamp;


-- 주-도시별 셀러, 고객 그리고 결제방식
-- sel-cus-distance-pay.csv 파일로 export
SELECT s.*, c.*, i.product_id, p."CATEGORY", i.price, pay.payment_value, pay.payment_sequential, pay.payment_type, pay.payment_installments
FROM sellers s, customers c, orders o, order_items i, products p, order_payments pay
WHERE 1=1 
    AND s.seller_id = i.seller_id
    AND o.customer_id = c.customer_id
    AND o.order_id = i.order_id 
    AND i.product_id = p.product_id
    AND o.order_id = pay.order_id
ORDER BY s."STATE", s.city, s.seller_id, c.customer_state, c.customer_city, o.purchase_timestamp;


-- 주-도시별 셀러, 고객 그리고 걸린 시간과 가격
-- sel-cus-distance-time-price.csv 파일로 export
SELECT s.*, c.*, i.product_id, p."CATEGORY", i.price, o.status, o.purchase_timestamp, o.approved_at, o.deliv_carrier_date, o.deliv_customer_date, o.estimated_deliv
FROM sellers s, customers c, orders o, order_items i, products p, order_payments pay
WHERE 1=1 
    AND s.seller_id = i.seller_id
    AND o.customer_id = c.customer_id
    AND o.order_id = i.order_id 
    AND i.product_id = p.product_id
    AND o.order_id = pay.order_id
ORDER BY s."STATE", s.city, s.seller_id, c.customer_state, c.customer_city, o.purchase_timestamp, o.approved_at;


--order_items.product_category_name,  빼고 
-- sel_ord_cus.csv 파일로 export
SELECT sellers.*, orders.*,  customers.customer_zip_code_prefix, customers.customer_city, customers.customer_state
FROM orders , sellers, customers, products, order_items
WHERE 1=1
    AND orders.order_id = order_items.order_id(+)
    AND order_items.seller_id = sellers.seller_id (+)
    AND orders.customer_id = customers.customer_id (+)
    AND order_items.product_id = products.product_id (+)
ORDER BY sellers.seller_id;


-- city 엉망인 것 고치기 위한 코드
SELECT s.seller_id, s.city, g.geolocaion_city, s."STATE", g.geolocation_state, s.seller_zip_code_prefix, g.geolocation_zip_code_prefix, customers.customer_state
FROM orders , sellers AS s, customers, products, order_items, geolocation AS g
WHERE 1=1
    AND orders.order_id = order_items.order_id(+)
    AND order_items.seller_id = s.seller_id (+)
    AND orders.customer_id = customers.customer_id (+)
    AND order_items.product_id = products.product_id (+)
    AND g.geolocation_zip_code_prefix(+) = s.seller_ZIP_CODE_PREFIX
    AND g.geolocation_zip_code_prefix(+) = customers.customer_ZIP_CODE_PREFIX
ORDER BY s.city, s.seller_id;

--응 이거 안돌아가.. 다시 시도하자
