# 특정 컬럼 안에 특정 값이 있음을 확인하고 싶을 때 사용
# DataFrame.loc[DataFrame.column_name.isin(['search_str1','search_str2',...])]

wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France'])]
