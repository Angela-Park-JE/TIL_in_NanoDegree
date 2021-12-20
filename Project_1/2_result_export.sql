-- 쿼리의 결과를 csv로 내보내서 저장하기

--1. orders table에 seller_id, product_id, category, payment 정보를 붙인 쿼리

SELECT orders.*, order_items.seller_id, order_items.product_id, products."CATEGORY", order_items.price, order_payments.*
FROM orders, order_items , products, order_payments
WHERE 1=1 
    AND orders.order_id = order_items.order_id 
    AND order_items.product_id = products.product_id
    AND orders.order_id = order_payments.order_id
ORDER BY orders.purchase_timestamp;


--2. 쿼리의 결과를 저장하기

---- 처음에는 구글링 후 SPOOL 기능을 쓰려고 했으나, 잘 되지 않았다.
    --SPOOL C:\Users\djroz\Desktop\000_ND_000\Kaggle Data\PJT_1_Olist\data_eda\txtorder_item_category_payments.out
    --SELECT orders.*, order_items.seller_id, order_items.product_id, products."CATEGORY", order_items.price, order_payments.*
    --FROM orders, order_items , products, order_payments
    --WHERE 1=1 
    --    AND orders.order_id = order_items.order_id 
    --    AND order_items.product_id = products.product_id
    --    AND orders.order_id = order_payments.order_id
    --ORDER BY orders.purchase_timestamp;
    --SPOOL off

---- 참조: https://mine-it-record.tistory.com/194
---- 쿼리 결과 컬럼 우클릭 후 '익스포트(Export)' 누르고 형식(csv나 xlsx 등)을 지정한다. 위치를 지정하고 다음 '익스포트 요약'은 넘어가면 된다.    
---- orders_items_prod_pay.csv 파일로 export 했다.
