# 불러오기

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_sellers = pd.read_csv("olist_sellers_dataset.csv")
df_orders = pd.read_csv("olist_orders_dataset.csv")
df_oitems = pd.read_csv("olist_order_items_dataset.csv")
df_opay = pd.read_csv("olist_order_payments_dataset.csv")
df_prod = pd.read_csv("olist_products_dataset.csv")
df_cus = pd.read_csv("olist_customers_dataset.csv")

df_oitempp = pd.read_csv("/Volumes/GoogleDrive/내 드라이브/PJT_1_Olist/[3]merged_csv/orders_items_prod_pay.csv")
df_scdpay = pd.read_csv("/Volumes/GoogleDrive/내 드라이브/PJT_1_Olist/[3]merged_csv/sel-cus-distance-pay.csv")
df_scdprice = pd.read_csv("/Volumes/GoogleDrive/내 드라이브/PJT_1_Olist/[3]merged_csv/sel-cus-distance-time-price.csv")
df_selocus = pd.read_csv("/Volumes/GoogleDrive/내 드라이브/PJT_1_Olist/[3]merged_csv/sel_ord_cus.csv")



# 로우수 확인

print(df_sellers.shape, df_orders.shape, df_oitems.shape, df_opay.shape, df_prod.shape, df_cus.shape)
(3095, 4) (99441, 8) (112650, 7) (103886, 5) (32951, 9) (99441, 5)

# seller : 3095
# orders(주문건수) : 99441
# order_items(주문아이템들) : 103886 
# order_payments(주문건에 대한 결제방식) : 103886
# products(판매된 물건 정보) : 32951
# customers(주문건수에 해당되는 고객들) : 99441
# df_cus['customer_unique_id'].nunique() : 96096



# sql로 수정해서 받아온 테이블 확인

# print(df_oitempp.shape, df_scdpay.shape, df_scdprice.shape, df_selocus.shape)
# (117601, 17) (117601, 16) (117601, 18) (112650, 15)




# 시험삼아 보는 카테고리별 아이템수

df_prod.pivot_table(index='product_category_name', values='product_id', aggfunc = 'count')



# df_selocus 잘못 입력된 도시명 수정하기

#-- 1. 살펴보기
df_selocus.sort_values(['CITY','SELLER_ID'])
    # 112650 rows × 15 columns

#-- 2. CITY 값들 개수
df_selocus['CITY'].nunique()

#-- 3. CITY 값들 보기
df_CITY = df_selocus['CITY'].unique()
df_CITY

#--4. CITY 값들 보기
print(df_selocus['CITY'].unique())
print(df_selocus['CITY'].nunique())
print(type(df_selocus['CITY'].unique()))
    # 609 개

#--5. 값 변경하기
df_selocus['CITY'].replace(["sp","sao p%"], "sao paulo", inplace=True)      # 교체하기
print(df_selocus['CITY'].nunique())
    # 608 개

#--6. sao p로 시작하는 문자를 sao paulo로 치환하려 했다.
df_selocus["CITYNAME"] = df_selocus['CITY'].replace('(.*)sao p(.*)', r'sao paulo', regex=True,)
print(df_selocus['CITYNAME'].nunique())
    # 597 개

#--7. 리스트로 받기
np.array(df_selocus['CITYNAME'].tolist())
ct_list = list(np.array(df_selocus['CITYNAME'].tolist()))

#--8. ct_list 의 중복값을 set을 이용하여 제거
ct_list_sort = list(set(ct_list))
print(ct_list_sort)
print(len(ct_list_sort))

#--9. ct_list 의 중복값을 set을 이용하여 제거한 ct_list_sort 정렬
ct_list_sort.sort()
ct_list_sort

#--10. 결과값이 일일히 처리하기 어렵기 때문에, 만약 처리하기 위해서라면 GEOLOCATION 테이블을 이용해서 집코드로 매칭하여 챠쑈를 다시 입력해주는 수밖에 없을 것 같다. 하루를 거의 써버렸다.
