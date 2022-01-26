df_sel_geo.to_csv("01_df_sel_geo.csv")
df_cus_geo.to_csv("02_df_cus_geo.csv")


# 1차 분석에서는 null을 drop 한다. 
df_sel_geo.dropna(inplace=True)
df_cus_geo.dropna(inplace=True)


(1) 배송 완료된 오더 
df_delivered.to_csv("08_df_delivered.csv")

(1-1) delivered + oitems (에서 order_id 중복 뺸것)
df_deli_items.to_csv("09_df_delivered_items_info.csv")


(2) (1-1) + seller 정보 : df_deli_items_sel

(3) (2) + customer 정보 : df_deli_items_sel_cus


배송완료 + 아이템정보 일부 + seller + customer
df_deli_items_sel_cus.to_csv("03_df_deli_items_sel_cus.csv")


-- 
이름 예쁘게
df_for_time_geo = df_deli_items_sel_cus
--

import time
from datetime import timedelta

df_for_time_geo.columns
['order_id', 'seller_id', 'customer_id', 'customer_unique_id', 'price',
       'freight_value', 'seller_city', 'seller_state', 'customer_city',
       'customer_state', 'order_purchase_timestamp', 'order_approved_at',
       'order_delivered_carrier_date', 'order_delivered_customer_date',
       'order_estimated_delivery_date', 'shipping_limit_date']

df_for_time_geo.isna().sum()
# order_id                           0
# customer_id                        0
# seller_id                          0
# order_purchase_timestamp           0
# order_approved_at                  0
# order_delivered_carrier_date       0
# order_delivered_customer_date      0
# order_estimated_delivery_date      0
# shipping_limit_date                0
# seller_city                      215
# seller_state                     215
# customer_city                    264
# customer_state                   264


df_for_time_geo.to_csv("10_df_for_time_geo.csv")


df_final.to_csv("11_df_final.csv")

['order_id', 'customer_id', 'seller_id', 'order_purchase_timestamp',
       'order_approved_at', 'order_delivered_carrier_date',
       'order_delivered_customer_date', 'order_estimated_delivery_date',
       'shipping_limit_date', 'seller_city', 'seller_state', 'customer_city',
       'customer_state', 'price', 'freight_value', 'category', 'p_name_length',
       'p_description_length', 'p_photos_qty', 'p_weight_g', 'p_length_cm',
       'p_height_cm', 'p_width_cm', 'category_eng', 'review_score',
       'rev_creation_date', 'rev_answer_timestamp']



------

--
시간 넣기: 각각 조건별로 시간 넣은 것 csv로 받아오기
--
그 다음 df_final 에다가 5 가지 시간 넣기
--
나중에 평균적으로 받은지 얼마만에 리뷰를 다는지도 볼 수 있겠네
------

1. df_same_city : 4978 개
df_same_city.isna().sum()
order_id                          0
customer_id                       0
seller_id                         0
order_purchase_timestamp          0
order_approved_at                 0
order_delivered_carrier_date      0
order_delivered_customer_date     0
order_estimated_delivery_date     0
shipping_limit_date               0
seller_city                       0
seller_state                      0
customer_city                     0
customer_state                    0
price                            96
freight_value                    96
category                         96
p_name_length                    96
p_description_length             96
p_photos_qty                     96
p_weight_g                       96
p_length_cm                      96
p_height_cm                      96
p_width_cm                       96
category_eng                     96
review_score                     96
rev_creation_date                96
rev_answer_timestamp             96
del_lead_time_insamecity          0
esti_lead_time_insamecity         0
gap_esti_real_insamecity          0
gap_limit_real_insamecity         0
gap_limit_esti_insamecity         0


df_same_city.to_csv("11_df_same_city.csv")

2. df_same_state : 
여기서 시간 데이터로 완전히 바꾸면서 결측값 확인을 한다.
아래는 df_final 에 대한 값이다.
order_id                            0
customer_id                         0
seller_id                           0
order_purchase_timestamp            0
order_approved_at                   0
order_delivered_carrier_date        0
order_delivered_customer_date       0
order_estimated_delivery_date       0
shipping_limit_date                 0
seller_city                       215
seller_state                      215
customer_city                     264
customer_state                    264
price                            2441
freight_value                    2441
category                         2441
p_name_length                    2441
p_description_length             2441
p_photos_qty                     2441
p_weight_g                       2441
p_length_cm                      2441
p_height_cm                      2441
p_width_cm                       2441
category_eng                     2441
review_score                     2441
rev_creation_date                2441
rev_answer_timestamp             2441
	29545

2-1. 
df_same_state.isna().sum()
order_id                           0
customer_id                        0
seller_id                          0
order_purchase_timestamp           0
order_approved_at                  0
order_delivered_carrier_date       0
order_delivered_customer_date      0
order_estimated_delivery_date      0
shipping_limit_date                0
seller_city                        0
seller_state                       0
customer_city                      0
customer_state                     0
price                            602
freight_value                    602
category                         602
p_name_length                    602
p_description_length             602
p_photos_qty                     602
p_weight_g                       602
p_length_cm                      602
p_height_cm                      602
p_width_cm                       602
category_eng                     602
review_score                     602
rev_creation_date                602
rev_answer_timestamp             602
del_lead_time_insamestate          0
esti_lead_time_insamestate         0
gap_esti_real_insamestate          0
gap_limit_real_insamestate         0
gap_limit_esti_insamestate         0
	29545

df_same_state.to_csv("12_df_same_state.csv")


3.df_notsame_state
61932
주가 다른 건은 96455 주문건 중 61932 건이 된다.
이때 문제는 결측값이 있는 애들은 값 비교를 못하기 때문에 이 데이터에 모두 포함된다는 것이다.
order_id                            0
customer_id                         0
seller_id                           0
order_purchase_timestamp            0
order_approved_at                   0
order_delivered_carrier_date        0
order_delivered_customer_date       0
order_estimated_delivery_date       0
shipping_limit_date                 0
seller_city                       215
seller_state                      215
customer_city                     264
customer_state                    264
price                            1743
freight_value                    1743
category                         1743
p_name_length                    1743
p_description_length             1743
p_photos_qty                     1743
p_weight_g                       1743
p_length_cm                      1743
p_height_cm                      1743
p_width_cm                       1743
category_eng                     1743
review_score                     1743
rev_creation_date                1743
rev_answer_timestamp             1743

3-1. df_diff_states = df_notsame_state.dropna()

3-2. df_diff_states
결측 있는건 다 제외한다. 60189

df_diff_states.to_csv("13_df_diff_states.csv")

  
