
#-- load library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#-- for windows
df_sellers = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/olist_sellers_dataset.csv")
df_orders = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/olist_orders_dataset.csv")
df_oitems = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/olist_order_items_dataset.csv")
df_opay = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/olist_order_payments_dataset.csv")
df_prod = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/olist_products_dataset.csv")
df_cus = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/olist_customers_dataset.csv")
df_rev = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/olist_order_reviews_dataset.csv")
df_geo = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/olist_geolocation_dataset.csv")

df_oitempp = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/orders_items_prod_pay.csv")
df_scdpay = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/sel-cus-distance-pay.csv")
df_scdprice = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/sel-cus-distance-time-price.csv")
df_selocus = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/sel_ord_cus.csv")
df_sel = pd.read_csv("C:/Users/djroz/Desktop/PJT1_dataset/sellers.csv")



#-- data load sample
df_sellers["seller_id"].describe()

df_sel["SELLER_ID"].describe()

df_sel.isna().sum()

# call null row 
df_sel[df_sel['CITY'].isna()]



#-- column name print1
print("orders 컬럼명: ", df_orders.columns.tolist())
print("sellers 컬럼명: ", df_sellers.columns.tolist())
print("order_items 컬럼명: ", df_oitems.columns.tolist())
print("products 컬럼명: ", df_prod.columns.tolist())
print("payments 컬럼명: ", df_opay.columns.tolist())
print("customers 컬럼명: ", df_cus.columns.tolist())
print("reviews 컬럼명: ", df_rev.columns.tolist())
print("geolocations 컬럼명: ", df_geo.columns.tolist())
#-- column name print2
print("oitem-pay-price 컬럼명: ", df_oitempp.columns.tolist())
print("seller-customer-deliv-pay 컬럼명: ", df_scdpay.columns.tolist())
print("seller-customer-deliv-price 컬럼명: ", df_scdprice.columns.tolist())
print("seller-order-cus 컬럼명: ", df_selocus.columns.tolist())



#-- 도시명-geolocation.csv 확인
    # df_selocus 잘못 입력된 도시명 수정하기

print(df_selocus['CITY'].unique())
print(df_selocus['CITY'].nunique())
print(type(df_selocus['CITY'].unique()))

    # df_selocus 도시- geolocation 파일에 zip코드로 연결하면 도시를 정확하게 받아올 수 있을 것이다.



#-- 배송처리시간 확인 
df_selocus.info()
df_selocus.head()

# delivery 정보만 담은 프레임 만들기
df_delv_state = df_selocus[['STATE','CUSTOMER_STATE','STATUS','PURCHASE_TIMESTAMP', 'APPROVED_AT', 'DELIV_CARRIER_DATE', 'DELIV_CUSTOMER_DATE', 'ESTIMATED_DELIV']]

# 중복 데이터 제거하기1
df_selocus = df_selocus.drop_duplicates(subset=None, keep='first', inplace=True, ignore_index=False)
    # 112650 rows × 8 columns -> 100010 rows × 15 columns

# 중복 데이터 제거하기2
term2 = (df_selocus['STATUS']=='delivered')
    # orders 테이블의 총 (99441, 8) 인데 (97819 rows × 15 columns)차이가 나는 이유는 한 order_id 안에 복수의 물건이 있을 수 있기 떄문.


# 중복 데이터 제거하기3
    # (데려온 오더 중)
df_deliverd.isna().sum()
df_deliverd["APPROVED_AT"].isna()
    # 위에서 확인한 결측치를 가진 데이터만 불러와본다.
df_deliverd[(df_deliverd["APPROVED_AT"].isna())|(df_deliverd["DELIV_CARRIER_DATE"].isna())|(df_deliverd["DELIV_CUSTOMER_DATE"].isna())|(df_deliverd["ESTIMATED_DELIV"].isna())]

# 결측값이 들어있는 행 전체 삭제하기(delete row with NaN) : df.dropna(axis=0)
# 출처: https://rfriend.tistory.com/263 [R, Python 분석과 프로그래밍의 친구 (by R Friend)]
df_deliverd = df_deliverd.dropna(axis=0)
df_deliverd
    # (97819 rows × 15 columns) -> (97796 rows × 15 columns) 개로 줄었다.



