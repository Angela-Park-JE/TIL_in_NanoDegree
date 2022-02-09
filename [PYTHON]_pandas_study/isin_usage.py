# 특정 컬럼 안에 특정 값이 있음을 확인하고 싶을 때 사용
# DataFrame.loc[DataFrame.column_name.isin(['search_str1','search_str2',...])]
# 찾는 값이 [] 리스트 안에 있을 경우 데이터프레임 형태로 호출한다.

wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France'])]
