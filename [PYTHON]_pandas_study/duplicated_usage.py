### duplicated() and drop_duplicates() usage 
# duplicated: 메소드가 적용된 열과 길이가 동일한 불리언 벡터를 반환하며 어떤 요소가 중복 요소인지 확인할 수 있다.
# drop_duplicates: 중복 요소가 있는 행을 삭제한다. 기본은 전체 열을 대상으로 검색하며 검사할 열을 지정할 수 있다.

# subset 파라미터는 기본값으로 모든 열에 대해 중복 데이터를 확인한다.
# 'first|last|False': first (default) - 처음 발견 데이터 제외 마크 혹은 삭제, 
#                   last - 마지막 발견 데이터 제외 마크 혹은 삭제
#                   false - 모든 중복 데이터 마크 혹은 삭제


import pandas as pd
data = pd.DataFrame(source)


### 중복 기준(특정 컬럼) 적어서 점검하기
data.duplicated(subset = None, keep = 'first|last|False')
# subset은 중복데이터를 찾을 열을 적으며, series, index에 적용할 경우 사용하지 않는다.
# keep은 중복데이터 발견시 어떤 데이터를 찾을지 결정하는 변수이다.

# keep=False: 컬럼을 기준으로 모든 중복 데이터를 불러오기
data.duplicated('filter_column_name', keep = 'first')

# 열의 레이블 배열하여 한 행에서 열끼리 비교
data.duplicated(['filter_column_name','filter_column_name2'])

# 중복 기준(특정 컬럼) 적은채로 정렬하기
data.duplicated('filter_column_name', keep = 'first').sort_values('sorting_column_name')

# 중복된 행인지 점검하기(동일한 데이터가 있는지), 불리언타입 시리즈 형태로 반환
display(data.duplicated())

# 중복된 행의 데이터만 표시하기: 행 전체가 일치해야 출력되는 것으로 보임
display(data[data.duplicated()])


### 중복 기준 적어서 삭제하기
data.drop_duplicates(subset = None, keep = 'first|last|False', inplace = True|False)
# subset은 중복데이터를 찾을 열을 적으며, series, index에 적용할 경우 사용하지 않는다.
# keep은 중복데이터 발견시 어떤 데이터를 삭제할 지 결정하는 변수이다.
# inplace는 메소드가 적용되는 원본 데이터를 변경(대체)할지 아닌지 결정한다.

# keep = fisrt(defualt), inplace = True : 중복된 행은 '하나만' 남기고 제거하여 결과 저장하기
data.drop_duplicates(inplace = True)

# keep = last : 파라미터를 이용하여 남길 값을 마지막 값으로 선택하기
data.drop_duplicates("column_name", keep = 'last').sort_values('sorting_column_name', ascending=False) 

