# duplicated() and drop_duplicates() usage 

import pandas as pd
data = pd.DataFrame(source)

# 중복 기준(특정 컬럼) 적어서 점검하기
# keep 의 경우 아직 버리거나 둘 것을 특정하게 선택하지 않은 것으로 보임 
data.duplicated('filter_column_name', keep = False)

# 중복 기준(특정 컬럼) 적은채로 정렬하기
data.duplicated('filter_column_name', keep = False).sort_values('sorting_column_name')

# 중복된 행인지 점검하기(동일한 데이터가 있는지), 불리언타입 시리즈 형태로 반환
display(data.duplicated())

# 중복된 행의 데이터만 표시하기, 행 전체가 일치해야 출력되는 것으로 보임
display(data[data.duplicated()])

# inplace = True : 중복된 행은 '하나만' 남기고 제거하기
data.drop_duplicates(inplace = True)

# keep = last : 파라미터를 이용하여 남길 값 선택하기
data.drop_duplicates("column_name", keep = 'last').sort_values('sorting_column_name', ascending=False) 

