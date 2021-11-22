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

#df.info()
#df.shape
#df.dtypes
#df.describe()

# describe(percentiles=None, include=None, exclude=None, datetime_is_numeric=False)
#df.describe(include="all")
#df.describe(include="object") # 문자 컬럼: 계산 빼고 
#df.describe(include="float64") # 실수 컬럼: unique나 freq 빼고

# 2개 이상의 컬럼을 가져올 때에는 리스트 자료형을 사용한다.
#df[["약품명", "가격"]]
#df.loc[0]
#df.loc[[0,1,2]]

#df.loc[0,"약품명"]
#df.loc[1,["약품명","가격"]]
#df.loc[[0,1], ["약품명","가격"]]

#df.loc[0,"약품명"]
#df.loc[0]["약품명"]

#%timeit df.loc[0,"약품명"]
#%timeit df.loc[0]["약품명"]

# ---

### 특정한 문자로 검색하기. 
# 로우별로 T/F, 불리언 형태로 가져온다.
df["약품명"].str.contains("vita")
# 불리언 인덱싱. 포함된 로우만 가져온다.
df[df["약품명"].str.contains("vita")]
# or로 함께 가져오고 싶다면 | 을 사용한다.
df[df["약품명"].str.contains("비타|vita")]
# 약품명에 있는 영문을 (검색하기 쉽게) 전부 소문자로 바꾼다.
df["약품명"].str.lower() # 바꿔서 보기만 한 것이므로 df의 값이 변하지는 않는다.

### 파생변수만들기
# 대소문자로 인해 검색이 되지 않는 문제를 해결하기 위해 모두 소문자로 만듭니다.
# 파이썬의 str 메소드를 사용해서 소문자로 변경이 가능합니다.
# 새로운 컬럼을 만들어서 소문자로된 약품명을 넣어버리자.
df["약품명_소문자"] = df["약품명"].str.lower()
# 약품명_소문자 컬럼에서 vita|비타 검색
df[df["약품명_소문자"].str.contains("비타|vita")]
# and로 검색하고 싶다면 & 을 사용한다.

### > , < 대소비교로 조건에 맞는 값을 가져오기
# 특정 금액 이상의 가격에 해당하는 데이터프레임을 가져온다.
df["가격"] > 3200
# 특정 금액 이하의 가격에 해당되는 데이터를 리스트로 가져옵니다.
df[df["가격"]] <= 3200

### 정렬하기
# sort_values 를 통해 정렬한다.
# df.sort_values("가격", "약품명") # 라고 쓰면
# ValueError: No axis named 약품명 for object type DataFrame.
df.sort_values(["가격", "약품명"]) # 항상 리스트로.

# by="" 안써도 알아서 컬럼 순서대로 첫 번째로 오름차순으로 정렬. 
# ascending 으로 각 컬럼별로 정렬 기준을 정해줄 수 있다.
df.sort_values(by=["가격","약품명"]), ascending = [False, True]
# 가격은 내림차순 False, 약품명은 오름차순 True

### 파일로 저장/불러오기
# to_csv 를 통해 csv 파일로 저장합니다.
df.to_csv("pandas_df_20211121.csv")
# pd.read_csv 를 통해 csv을 읽어옵니다.
pd.read_csv("pandas_df_20211121.csv")
# 저장 할 때 인덱스를 저장하지 않는 방법
df.to_csv("pandas_df_20211121.csv", index=False)
# 저장된 csv파일을 인코딩하여 불러오는 방법
pd.read_csv("pandas_df_20211121.csv", encoding="cp949")
# 이렇게 뜬다: UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 0: illegal multibyte sequence
