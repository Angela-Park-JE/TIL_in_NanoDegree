# 0301 파이썬 EDA-pandas-input.ipynb

# 라이브러리 로드
import pandas as pd
import numpy as np
import seaborn as sns

# 판다스와 씨본 버전 확인하기
print(pd.__version__)
print(sns.__version__)

# 씨본은 0.11.0 버전에서 변화가 많으니 이 버전 이상 사용하기
# 아나콘다 열어서 !pip install seaborn --upgrade 해주기.

# 자동차 연비 관련 데이터'mpg'(마일퍼 갤런)를 데려올 것이다.
# 데이터 시각화 라이브러리들은 기본적인 리드셋을 내장하고 있다.
sns.load_dataset("mpg")
df = sns.load_dataset("mpg")
df.shape

### 파이썬 클래스 
# 어트리뷰트는 속성으로, 값을 가져오거나 할 때 쓰고 괄호가 없다.
# 함수(메소드)는 기능(동작)으로, 괄호 안 파라미터(옵션)에 따라 가져오도록 한다.

### 살펴보기
# index 값만 보기
df.index

# column 값만 보기
df.column

# values 값 보기 - 모든 값들을 일부 중략 형태로 보여준다.
df.values

# 컬럼 별 데이터 타입 보기
df.dtypes

### 데이터셋 일부만 가져오기
# head, tail, sample
df.head()
df.tail()
df.sample(5)
# 일부를 살펴보거나, 시각화나 머신러닝 학습시킬 때 값이 너무 많을 때 샘플을 추출한다. 



### 데이터셋 요약정보 보기
df.info()
# info() 와 info는 다르다. info는 데이터 셋 일부를 보여주듯 가져온다.
df.info

### 결측치 확인
# 컬럼 별 count값 중 일부 수가 적은 것들은 결측치 때문이다.
# 참고로 True와 False의 값은 각각 1과 0이다.

# isnull()로 결측치 확인하기. 불타입으로 출력된다.
# False가 결측치 아닌 상태를 뜻한다.
df.isnull()

# 결측치 개수 확인
# True 값만 더해지므로 결측치 칸만 세어져서 숫자로 출력된다.
df.isnull().sum()

# isna().mean()으로 결측치 비율 확인
# *100으로 전체 중 몇 퍼센트가 결측치인지 확인할 수 있다.
df.isna().mean() * 100



### 기술통계 확인하기

# 수치형 값에 대한 통계 확인하기
# count 개수, mean 평균, std 표준편차, 50% 중간값
df. describe()

# 범주형 값에 대한 통계 확인하기
# top 과 freq는 가장 빈도가 높은 것에 대해 보여준다.
# unique는 고유값들이 몇 가지가 있는지.
df.describe(include="object")

# 수치형 범주형 함께보기
df.describe(include="all")



### Series와 DataFrame

# 특정 컬럼 하나 보기
df["name"]
# 타입 확인해보기
type(df["name"]) 
#--- pandas.core.series.Series --- : 시리즈는 1차원으로 괄호가 하나이다.

# 특정 컬럼을 데이터 프레임으로 보기
df[["name"]]
# 타입 확인해보기
type(df[["name"]])
#--- pandas.core.frame.DataFrame --- : 인덱스가 포함된 데이터프레임이다.

# 특정 컬럼 둘 이상 보기
df[["mpg","name"]]
# 타입 확인해보기
type(df[["mpg","name"]])
#--- pandas.core.frame.DataFrame --- : 데이터프레임은 2차원, 괄호가 둘이다.



### .loc 로 데이터 가져오기
# location
# 대괄호가 하나일 때에는 시리즈 형태, 둘일 때에는 데이터프레임 형태로 가져온다.
# 만약 열의 이름이 숫자일 경우 ""을 하지 않아도 알아서 가져와준다.

# .loc[인덱스번호]
df.loc[0]
# .loc[[인덱스번호1, 인덱스번호2, ...]]
df.loc[[0,1]]

# .loc[행 인덱스번호, 컬럼 네임]
df.loc[0,"name"]

# .loc[[행 인덱스번호 여러개], [컬럼 네임 여러개]]
df.loc[[0,1,2],["name", "mpg", "origin"]]

# 컬럼의 경우 인덱스 범위를 직접 입력 가능하다.
# loc[인덱스 범위, 컬럼 순번혹은 이름으로 범위]
df.loc[:5, :"cylinders"]

### .iloc[]도 슬라이싱으로 인덱스를 정해줄 수 있다.
df.iloc[:3, :3]
df.iloc[:5, 3:9]
# iloc는 정수로만 찾기 때문에 직접 컬럼 네임을 지정해주면 traceback이 뜬다.

