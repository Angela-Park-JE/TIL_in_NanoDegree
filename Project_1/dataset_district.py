# 도시-주-타주 별로 나눠보기



# 1. 같은 도시 조건

df_same_city = df_for_time_geo[(df_for_time_geo['seller_city']==df_for_time_geo['customer_city'])&(df_for_time_geo['seller_state']==df_for_time_geo['customer_state'])]

# 	4978 rows × 13 columns


# 2. datetime 으로 바꾸기
df_same_city['order_purchase_timestamp']=pd.to_datetime(df_same_city['order_purchase_timestamp'])
df_same_city['order_approved_at']=pd.to_datetime(df_same_city['order_approved_at'])
df_same_city['order_delivered_carrier_date']=pd.to_datetime(df_same_city['order_delivered_carrier_date'])
df_same_city['order_delivered_customer_date']=pd.to_datetime(df_same_city['order_delivered_customer_date'])
df_same_city['order_estimated_delivery_date']=pd.to_datetime(df_same_city['order_estimated_delivery_date'])
df_same_city['shipping_limit_date']=pd.to_datetime(df_same_city['shipping_limit_date'])

# 3. 실 소요 시간 = 배달완료-구매완료시간 : del_lead_time_insamecity
df_same_city["del_lead_time_insamecity"] = df_same_city['order_delivered_customer_date']-df_same_city['order_purchase_timestamp']

# 4. 예상 소요 시간 = 예상배달완료-구매완료시간 : esti_lead_time_insamecity
df_same_city["esti_lead_time_insamecity"] = df_same_city['order_estimated_delivery_date']-df_same_city['order_purchase_timestamp']

# 5. 실제 지연 시간 = 예상배달완료시간-배달완료시간 : gap_esti_real_insamecity
df_same_city["gap_esti_real_insamecity"] = df_same_city['order_estimated_delivery_date']-df_same_city['order_delivered_customer_date']

# 6. 남은 지연 시간 = 배송리밋시간-배달완료시간 : gap_limit_real_insamecity
df_same_city["gap_limit_real_insamecity"] = df_same_city['shipping_limit_date']-df_same_city['order_delivered_customer_date']

# 7. 추가 리밋 시간 = 배송리밋시간-예상배달완료 시간 : gap_limit_esti_insamecity
df_same_city["gap_limit_esti_insamecity"] = df_same_city['shipping_limit_date']-df_same_city['order_estimated_delivery_date']

# 8. df_same_city.isna().sum()
# order_id                         0
# customer_id                      0
# seller_id                        0
# order_purchase_timestamp         0
# order_approved_at                0
# order_delivered_carrier_date     0
# order_delivered_customer_date    0
# order_estimated_delivery_date    0
# shipping_limit_date              0
# seller_city                      0
# seller_state                     0
# customer_city                    0
# customer_state                   0
# del_lead_time_insamecity         0
# esti_lead_time_insamecity        0
# gap_esti_real_insamecity         0
# gap_limit_real_insamecity        0
# gap_limit_esti_insamecity        0




# 1. 같은 주 조건
df_same_state = df_for_time_geo[(df_for_time_geo['seller_state']==df_for_time_geo['customer_state'])&(df_for_time_geo['seller_city']!=df_for_time_geo['customer_city'])]

# 	29545 rows × 13 columns


# 2. 실 소요 시간 = 배달완료-구매완료시간 : del_lead_time_insamestate
df_same_state["del_lead_time_insamestate"] = df_same_state['order_delivered_customer_date']-df_same_state['order_purchase_timestamp']

# 3. 예상 소요 시간 = 예상배달완료-구매완료시간 : esti_lead_time_insamecity
df_same_state["esti_lead_time_insamestate"] = df_same_state['order_estimated_delivery_date']-df_same_state['order_purchase_timestamp']

# 4. 실제 지연 시간 = 예상배달완료시간-배달완료시간 : gap_esti_real_insamecity
df_same_state["gap_esti_real_insamestate"] = df_same_state['order_estimated_delivery_date']-df_same_state['order_delivered_customer_date']

# 5. 남은 지연 시간 = 배송리밋시간-배달완료시간 : gap_limit_real_insamestate
df_same_state["gap_limit_real_insamestate"] = df_same_state['shipping_limit_date']-df_same_state['order_delivered_customer_date']

# 6. 추가 리밋 시간 = 배송리밋시간-예상배달완료시간 : gap_limit_esti_insamestate
df_same_state["gap_limit_esti_insamestate"] = df_same_state['shipping_limit_date']-df_same_state['order_estimated_delivery_date']

# 7. df_same_state.isna().sum()
	# order_id                         0
	# customer_id                      0
	# seller_id                        0
	# order_purchase_timestamp         0
	# order_approved_at                0
	# order_delivered_carrier_date     0
	# order_delivered_customer_date    0
	# order_estimated_delivery_date    0
	# shipping_limit_date              0
	# seller_city                      0
	# seller_state                     0
	# customer_city                    0
	# customer_state                   0
	# del_lead_time_insamestate        0
	# esti_lead_time_insamestate       0
	# gap_esti_real_insamestate        0
	# gap_limit_real_insamestate       0
	# gap_limit_esti_insamestate       0



#--- 


# 1. 다른 주 조건
df_notsame_state = df_for_time_geo[(df_for_time_geo['seller_state']!=df_for_time_geo['customer_state'])]

# 	61932 rows × 13 columns


# 2. 문제는 결측값이 있는 애들은 값 비교를 못하기 때문에 이 데이터에 모두 포함된다는 것이다.

# 3. 비교를 할 수 없는 애들은 drop 한다.
# 이름을 df_notsame_state 에서 df_diff_states 로 바꾸어줬다.

# 4. df_diff_states.info()
	 # 0   order_id                       61454 non-null  object        
	 # 1   customer_id                    61454 non-null  object        
	 # 2   seller_id                      61454 non-null  object        
	 # 3   order_purchase_timestamp       61454 non-null  datetime64[ns]
	 # 4   order_approved_at              61454 non-null  datetime64[ns]
	 # 5   order_delivered_carrier_date   61454 non-null  datetime64[ns]
	 # 6   order_delivered_customer_date  61454 non-null  datetime64[ns]
	 # 7   order_estimated_delivery_date  61454 non-null  datetime64[ns]
	 # 8   shipping_limit_date            61454 non-null  datetime64[ns]
	 # 9   seller_city                    61454 non-null  object        
	 # 10  seller_state                   61454 non-null  object        
	 # 11  customer_city                  61454 non-null  object        
	 # 12  customer_state                 61454 non-null  object 
#  	61454 rows × 13 columns

# 5. 61932 에서 61454 가 되었다. 총 478 줄어들었다.



#---
# 처리하였으니 다시 한다.
# (따로 구했던 뒤로는 한번에 시간으로 아예 바꾼 다음 계산하려 했음)
# 문제는 데이터를 구해 올 때마다 시간 데이터로 매번 바꿔줘야 했고
# 그 다음에서야 day로 바꿀 수 있었음
# 우선 여기선 시간 데이터로 바꾸기만 하는 것을 적어둠

# 1.  실 소요 시간 = 배달완료-구매완료시간 : del_lead_time_indiffstates
df_diff_states["del_lead_time_indiffstates"] = df_diff_states['order_delivered_customer_date']-df_diff_states['order_purchase_timestamp']

# 2. 예상 소요 시간 = 예상배달완료-구매완료시간 : esti_lead_time_indiffstates
df_diff_states["esti_lead_time_indiffstates"] = df_diff_states['order_estimated_delivery_date']-df_diff_states['order_purchase_timestamp']

# 3. 실제 지연 시간 = 예상배달완료시간-배달완료시간 : gap_esti_real_indiffstates
df_diff_states["gap_esti_real_indiffstates"] = df_diff_states['order_estimated_delivery_date']-df_diff_states['order_delivered_customer_date']

# 4. 남은 지연 시간 = 배송리밋시간-배달완료시간 : gap_limit_real_indiffstates
df_diff_states["gap_limit_real_indiffstates"] = df_diff_states['shipping_limit_date']-df_diff_states['order_delivered_customer_date']

# 5. 추가 리밋 시간 = 배송리밋시간-예상배달완료 시간 : gap_limit_esti_indiffstates
df_diff_states["gap_limit_esti_indiffstates"] = df_diff_states['shipping_limit_date']-df_diff_states['order_estimated_delivery_date']





#---
# 숫자만 보기

df_same_city -> same_city
4978 rows × 11 columns


df_same_state -> same_state
29545 rows × 11 columns


df_diff_states -> diff_states
61454 rows × 11 columns

--> 합은 95977

# delivered 된 96455 개에서 95977 -> 478 개 : 
# 시간 데이터나 발송, 수신자 지역이 명확하지 않은 것 전부 지워진것.


# 셀러 주소 명확하지 않은 것 215
# 고객 주소 명확하지 않은 것 264
# 합은 479
# 둘 다 명확하지 않은 것이 있었기에 총 지워진 것이 278 개가 되었을 것.



 df_same_city.columns.to_list
 [['order_id', 'customer_id', 'seller_id', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date', 'shipping_limit_date', 'del_lead_time_insamecity', 'esti_lead_time_insamecity', 'gap_esti_real_insamecity', 'gap_limit_real_insamecity', 'gap_limit_esti_insamecity','seller_city', 'seller_state', 'customer_city', 'customer_state']]

 df_same_state.columns.to_list
 [['order_id', 'customer_id', 'seller_id', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date', 'shipping_limit_date', 'del_lead_time_insamestate', 'esti_lead_time_insamestate', 'gap_esti_real_insamestate', 'gap_limit_real_insamestate', 'gap_limit_esti_insamestate', 'seller_city', 'seller_state', 'customer_city', 'customer_state']]

 df_diff_states.columns.to_list
 [['order_id', 'customer_id', 'seller_id', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date', 'shipping_limit_date',  'del_lead_time_indiffstates', 'esti_lead_time_indiffstates', 'gap_esti_real_indiffstates', 'gap_limit_real_indiffstates', 'gap_limit_esti_indiffstates', 'seller_city', 'seller_state', 'customer_city', 'customer_state']]




#---

# 상관관계 구하려 할 때 시작 점

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as ml
import seaborn as sns
import folium as fm

import time
import datetime

# -- df_all 쓸 컬럼들
del_lead_time
esti_lead_time
gap_esti_real
gap_limit_real
gap_limit_esti
review-del : 크면 클수록 받고도 늦게 남긴 것

--

same_city.info()
Int64Index: 4978 entries, 19 to 96396

same_state.info()
Int64Index: 29545 entries, 0 to 96451

diff_states.info()
Int64Index: 61932 entries, 1 to 96454

# -> 이떄 diff_states 에는 지역정보가 없는 경우도 함께 있다.
# -> 하지만 타임 관련해서는 drop을 다 했기 때문에 결측이 안나오므로 그대로 사용하기로 하였다.



