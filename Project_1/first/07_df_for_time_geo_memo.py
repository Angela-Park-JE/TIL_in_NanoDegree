데이터셋 메타데이터



geo 데이터 : 1048575

nunique
geolocation_zip_code_prefix     19015
geolocation_lat                716685
geolocation_lng                717097
geolocation_city                 5960
geolocation_state                  27
-> null 값 drop 후: 1000162




customer 데이터 : 99441
nunique
customer_id                 99441
customer_unique_id          96096
customer_zip_code_prefix    14994
customer_city                4119
customer_state                 27



sellers 데이터 : 3095
nunique
seller_id                 3095
seller_zip_code_prefix    2246
seller_city                609
seller_state                23



-- df_sel_merge_geo -> df_sel_geo

1. merge
df_sel_merge_geo : sellers 테이블에 geo left join
	435094 rows × 10 columns

2. drop_duplicates
seller_id 기준으로 중복값 제거
	3095 rows × 10 columns

3. 이떄 zipcode가 있지만 geo에서는 정보가 없어서 비는 7명 셀러는 
2.1.4 에서 나중에 수정하기로 한다.

4. 컬럼 순서와 이름 변경 등 하여서

5. df_sel_geo 라는 테이블 만듦.
3095
 0   seller_id        3095 non-null   object 
 1   seller_zip_code  3095 non-null   int64  
 2   seller_city      3088 non-null   object 
 3   seller_state     3088 non-null   object 
 4   seller_lat       3088 non-null   float64
 5   seller_lng       3088 non-null   float64



-- df_cus_merge_geo -> df_cus_geo

1. merge
df_cus_merge_geo : custmers 테이블에 geo left join
	15083733 rows × 11 columns

2. drop_duplicates
customer_id 기준으로 중복값 제거
	99441 rows × 11 columns

3. 이떄 zipcode가 있지만 geo에서는 정보가 없어서 비는 278명 고객은 
2.2.3am 에서 나중에 수정하기로 한다.
-> 어차피 구매 취소한 사람들일 수도 있음.

4. 컬럼 순서와 이름 변경 등 하여서

5. df_cus_geo 라는 테이블 만듦.
99441
 0   customer_id         99441 non-null  object 
 1   customer_unique_id  99441 non-null  object 
 2   customer_zip_code   99441 non-null  int64  
 3   customer_city       99163 non-null  object 
 4   customer_state      99163 non-null  object 
 5   customer_lat        99163 non-null  float64
 6   customer_lng        99163 non-null  float64



-- 2.4  1차 분석에서는 df_sel_geo 와 df_cus_geo null 값 drop해버리기
df_sel_geo.dropna(inplace=True)
df_cus_geo.dropna(inplace=True)
--> 이때 이사람들 데이터가 있는지 없는지 orders테이블이랑 연결시켜서 볼 수도 있었을것. 




-----------------




orders 데이터 : 99441

order_id                       99441 non-null  object
customer_id                    99441 non-null  object
order_status                   99441 non-null  object
order_purchase_timestamp       99441 non-null  object
order_approved_at              99281 non-null  object
order_delivered_carrier_date   97658 non-null  object
order_delivered_customer_date  96476 non-null  object
order_estimated_delivery_date  99441 non-null  object

nunique
order_id                         99441
customer_id                      99441
order_status                         8
order_purchase_timestamp         98875
order_approved_at                90733
order_delivered_carrier_date     81018
order_delivered_customer_date    95664
order_estimated_delivery_date      459

df_orders.isna().sum()
order_id                            0
customer_id                         0
order_status                        0
order_purchase_timestamp            0
order_approved_at                 160
order_delivered_carrier_date     1783
order_delivered_customer_date    2965
order_estimated_delivery_date       0


3.2.1 상태의 고유값들
df_orders["order_status"].unique().tolist()
['delivered',
 'invoiced',
 'shipped',
 'processing',
 'unavailable',
 'canceled',
 'created',
 'approved']



-- df_orders --> df_delivered

1. 배송 완료인 것: 
df_orders[df_orders["order_status"] == "delivered"]
	96478 rows × 8 columns
2. 배송 완료 외의 상태인것: 
df_orders[df_orders["order_status"] != "delivered"]
	2963 rows × 8 columns

총 오더수 99441 중 96478 배송완료, 2963는 배송완료 외의 상태이므로 측정을 제외한다.
실제로 order_delivered_customer_date 의 결측치는 2965 배송완료 외의 상태들을 모두 포함한다.

3. 배송 완료인 것 중 결측치 확인
df_orders[df_orders["order_status"] == "delivered"].isna().sum()
order_id                          0
customer_id                       0
order_status                      0
order_purchase_timestamp          0
order_approved_at                14
order_delivered_carrier_date      2
order_delivered_customer_date     8
order_estimated_delivery_date     0

4. 주문승인 시간이나 출고 시간이 적히지 않았지만 배달완료가 된 주문건수가 있다.
이들또한 제거하고 보기로 한다.
df_delivered = df_orders[df_orders["order_status"] == "delivered"].dropna()
	96455 rows × 8 columns
96478 개에서 96455 로 줄었다.

5. delivered 상태는 이미 있으니 column drop
df_delivered.drop(columns=['order_status'],inplace=True)







-----------------







최종 시간데이터를 쓰기 위해서는 orders_item 테이블이 필요하다.

# -- merge 순서

# 1. df_oitem 결측 데이터 확인
# order_id               0
# order_item_id          0
# product_id             0
# seller_id              0
# shipping_limit_date    0
# price                  0
# freight_value          0

# 2. df_oitems + df_sel_geo: df_oitems_sel_geo
# seller_id 로 붙인다.
# df_oitems 와 df_oitems_selgeo 가 112650 로 로우수가 일치한다.

# 2-1. 이때 결측값은 셀러 집 데이터가 없던 값과 같다.
# order_id                 0
# order_item_id            0
# product_id               0
# seller_id                0
# shipping_limit_date      0
# price                    0
# freight_value            0
# seller_zip_code        253
# seller_city            253
# seller_state           253
# seller_lat             253
# seller_lng             253

# 2-2. 쓸모없는 컬럼 지운다.
# ['order_item_id','product_id','seller_lat','seller_lng']

# 3. df_delivered + df_oitems_sel_geo: df_delivered_geo
# order_id 로 붙인다.
# 	110173 rows × 15 columns

# 4. 붙이고 order_id 별로 중복값등을 다 삭제한다.
# df_delivered_geo = df_delivered_geo.drop_duplicates(['order_id','order_delivered_customer_date'], keep='first', inplace=False, ignore_index=False)
# 96455 rows × 15 columns



-- merge 순서
1. df_delivered + df_oitems: df_deli_items
order_id 로 결합

2. df_deli_items.info()
 # 0   order_id                       110173 non-null  object 
 # 1   customer_id                    110173 non-null  object 
 # 2   order_purchase_timestamp       110173 non-null  object 
 # 3   order_approved_at              110173 non-null  object 
 # 4   order_delivered_carrier_date   110173 non-null  object 
 # 5   order_delivered_customer_date  110173 non-null  object 
 # 6   order_estimated_delivery_date  110173 non-null  object 
 # 7   order_item_id                  110173 non-null  int64  
 # 8   product_id                     110173 non-null  object 
 # 9   seller_id                      110173 non-null  object 
 # 10  shipping_limit_date            110173 non-null  object 
 # 11  price                          110173 non-null  float64
 # 12  freight_value                  110173 non-null  float64
    110173

3. order_id와 도착시간 둘 다 중복되는 것은 지운다.
	96455 rows × 13 columns


--
1. df_deli_items + df_sel_geo: df_deli_items_sel
seller_id 로 결합

2. df_oitems_sel_geo.info()
 # 0   order_id                       96455 non-null  object 
 # 1   customer_id                    96455 non-null  object 
 # 2   order_purchase_timestamp       96455 non-null  object 
 # 3   order_approved_at              96455 non-null  object 
 # 4   order_delivered_carrier_date   96455 non-null  object 
 # 5   order_delivered_customer_date  96455 non-null  object 
 # 6   order_estimated_delivery_date  96455 non-null  object 
 # 7   order_item_id                  96455 non-null  int64  
 # 8   product_id                     96455 non-null  object 
 # 9   seller_id                      96455 non-null  object 
 # 10  shipping_limit_date            96455 non-null  object 
 # 11  price                          96455 non-null  float64
 # 12  freight_value                  96455 non-null  float64
 # 13  seller_zip_code                96240 non-null  float64
 # 14  seller_city                    96240 non-null  object 
 # 15  seller_state                   96240 non-null  object 
 # 16  seller_lat                     96240 non-null  float64
 # 17  seller_lng                     96240 non-null  float64
    96455 개로 돌아왔다.

3. order_id 중복값은 지워야겠다.
	96455

4. columns 관리하기

--
1. df_deli_items_sel + df_cus_geo: df_deli_items_sel_cus
customer_id 로 결합

2. df_deli_items_sel_cus.info()
# 0   order_id                       96455 non-null  object 
#  1   customer_id                    96455 non-null  object 
#  2   order_purchase_timestamp       96455 non-null  object 
#  3   order_approved_at              96455 non-null  object 
#  4   order_delivered_carrier_date   96455 non-null  object 
#  5   order_delivered_customer_date  96455 non-null  object 
#  6   order_estimated_delivery_date  96455 non-null  object 
#  7   seller_id                      96455 non-null  object 
#  8   shipping_limit_date            96455 non-null  object 
#  9   price                          96455 non-null  float64
#  10  freight_value                  96455 non-null  float64
#  11  seller_zip_code                96240 non-null  float64
#  12  seller_city                    96240 non-null  object 
#  13  seller_state                   96240 non-null  object 
#  14  customer_unique_id             96191 non-null  object 
#  15  customer_zip_code              96191 non-null  float64
#  16  customer_city                  96191 non-null  object 
#  17  customer_state                 96191 non-null  object 
#  18  customer_lat                   96191 non-null  float64
#  19  customer_lng                   96191 non-null  float64
	96455

3. 아까는 셀러로, 이번은 주문 아이디로 엮었고 주문아이디 중복값은 이미 order_items 가져올떄 관리했기 떄문에 96455 개가 유지된다.

4. columns 관리 


--

1. df_deli_items_sel_cus 순서변경

df_deli_items_sel_cus = df_deli_items_sel_cus[['order_id','seller_id', 'customer_id', 'customer_unique_id','price', 'freight_value','seller_city', 'seller_state',  'customer_city',
       'customer_state', 'order_purchase_timestamp',
       'order_approved_at', 'order_delivered_carrier_date',
       'order_delivered_customer_date', 'order_estimated_delivery_date',
       'shipping_limit_date'
       ]]

2. df_deli_items_sel_cus 이름 변경 -> df_geo_with_time




---

시간 모듈 들여오기

1. df_for_time_geo.info()
 0   order_id                       96455 non-null  object
 1   seller_id                      96455 non-null  object
 2   customer_id                    96455 non-null  object
 3   seller_city                    96240 non-null  object
 4   seller_state                   96240 non-null  object
 5   customer_city                  96191 non-null  object
 6   customer_state                 96191 non-null  object
 7   order_purchase_timestamp       96455 non-null  object
 8   order_approved_at              96455 non-null  object
 9   order_delivered_carrier_date   96455 non-null  object
 10  order_delivered_customer_date  96455 non-null  object
 11  order_estimated_delivery_date  96455 non-null  object
 12  shipping_limit_date            96455 non-null  object
 	96455
10.3+ MB

2. 컬럼 시간 먼저로 순서 바꾸기

3. df_for_time_geo 결측치 확인
order_id                           0
customer_id                        0
seller_id                          0
order_purchase_timestamp           0
order_approved_at                  0
order_delivered_carrier_date       0
order_delivered_customer_date      0
order_estimated_delivery_date      0
shipping_limit_date                0
seller_city                      215
seller_state                     215
customer_city                    264
customer_state                   264



