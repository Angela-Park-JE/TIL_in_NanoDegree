#0201-pands-for-eda-input2

import pandas as pd
import numpy as np
pd.DataFrame() 
df = pd.DataFrame()
df["약품명"] = ["소화제", "감기약", "비타민", "digestive", "Omega3", "오메가3", "vitamin", "Vitamin"]
df["제조사"] = ["동아제약", "유한양행", "대웅제약", "일양약품", "JW중외제약", "일동제약", "보령제약", "한미약품"]
df["가격"] = 3500
#type(df)
#type(df["가격"])
#type(df["제조사"])
#df["약품명"].tolist()
df["가격"] = [3500, 3200, 4000, 3200, 3700, np.nan, 2000, 1000]
#type(np.nan)
df["지역"] = "서울"
df["종류"] = "일반의약품"
df["종류2"] = "1반의약품"
#df.drop("종류2") 
#df.drop("종류2", axis = 1)
df = df.drop("종류2", axis = 1)

# --- 

### 데이터 프레임의 정보를 봅니다.
df.info()
# 컬럼과 로우 갯수, 컬럼타입별 개수, 메모리 사용량 등 요약 정보.

### 데이터 프레임의 (행, 열) 개수를 본다.
df.shape

### 컬럼 별 데이터의 타입을 본다.
df.dtypes

### 수치형 데이터의 요약된 기술통계값(수치형 데이터)을 볼 수 있다.
df.describe()

### 범주형 데이터의 기술통계값을 볼 수 있다.
# describe(percentiles=None, include=None, exclude=None, datetime_is_numeric=False)
# string은 NaN으로 표현된다.
# include는 어떤 컬럼을 가져올 것인지 정한다.
df.describe(include="all")
df.describe(include="object") # 문자 컬럼: 계산 빼고 
df.describe(include="float64") # 실수 컬럼: unique나 freq 빼고

### 컬럼명으로 데이터 가져오기
# 2개 이상의 컬럼을 가져올 때에는 리스트 자료형을 사용한다.
df[["약품명", "가격"]]

### 행을 기준으로 데이터 가져오기
# 인덱스 번호로 첫번째 데이터 가져오기
# 인덱스를 따로 정해주진 않았지만 알아서 번호가 생성이 되었다!
df.loc[0]
# 위에서 3개의 행 데이터 가져오기
# 2개 이상의 행을 가져올 때에는 리스트 자료형을 사용한다.
df.loc[[0,1,2]]

### 행과 열을 함께 가져오기
# 특정 위치에 있을 데이터를 가져올 수 있다.
# df.loc[행 번호, 열]
df.loc[0,"약품명"]
# 2개 이상의 열을 가져올 때에는 리스트 자료형을 사용한다.
df.loc[1,["약품명","가격"]]
# 2개 이상의 행을 가져올 때에는 리스트 자료형을 사용한다.
df.loc[[0,1], ["약품명","가격"]]

### loc를 가져올 때 같지만 다른 것
df.loc[0,"약품명"]
df.loc[0]["약품명"]

### %timeit 으로 다른점 알아보기
%timeit df.loc[0,"약품명"]
%timeit df.loc[0]["약품명"]
# 결과는 같지만 속도가 첫 번째가 더 빠르다.