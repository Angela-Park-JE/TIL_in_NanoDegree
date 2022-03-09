-- 일부 pk를 조정하는 작업을 했다.

ALTER TABLE categories ADD PRIMARY KEY (CATEGORY_NAME) ENABLE;
COMMIT;

--ALTER TABLE order_items ADD PRIMARY KEY (order_id) ENABLE;
--ALTER TABLE order_payments ADD PRIMARY KEY (order_id) ENABLE;
ALTER TABLE orders ADD PRIMARY KEY (order_id) ENABLE;
ALTER TABLE products ADD PRIMARY KEY (product_id) ENABLE;
ALTER TABLE sellers ADD PRIMARY KEY (seller_id) ENABLE;
commit;
