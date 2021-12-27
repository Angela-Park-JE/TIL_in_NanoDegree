# 같은 도시별, 같은 주별, 타 주별 배송 소요 시간과 예상 시간, 제한 기간 구하는 동안 지속적으로 쓴 코드

# 테이블 합치기
df_sel_merge_geo = pd.merge(df_sellers, df_geo, how='left', left_on='seller_zip_code_prefix', right_on='geolocation_zip_code_prefix')
df_sel_merge_geo

# 중복 로우 제거하기
df_sel_merge_geo.drop_duplicates(['seller_id'], keep='first', inplace=True, ignore_index=False)
df_sel_merge_geo

# 필요없는 컬럼 제거하기
df_oitems_selgeo = df_oitems_selgeo.drop(columns=['order_item_id','product_id','seller_lat','seller_lng'])
df_oitems_selgeo

# 컬럼 이름 변경하기
df_sel_geo.columns = ['seller_id', 'seller_zip_code', 'seller_lat', 'seller_lng', 'seller_city', 'seller_state']
df_sel_geo

# 컬럼 순서 변경하기
df_sel_geo = df_sel_geo[['seller_id', 'seller_zip_code', 'seller_city', 'seller_state', 'seller_lat', 'seller_lng']]
df_sel_geo



# date로 바꾸기
# datetime 모듈을 import 해야함!
df['enddate']=pd.to_datetime(df['enddate'])
# 연산
df['col_name']=df['datetimed_col_name1']-df['datetimed_col_name2']

