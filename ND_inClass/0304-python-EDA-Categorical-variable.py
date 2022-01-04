# 0304-python-EDA-categorical-variable
# 범주형 변수 핸들링하기

# 라이브러리 로드
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 버전 확인하기 : 씨본은 0.11.0 이상을 해주기. 
# 이하일 경우 : !pip install seaborn --upgrade


### 데이터셋 로드 및 확인
# df url로 직접 불러와도 된다.
df = sns.load_dataset("mpg")
df

# 데이터셋 일부만 확인하기 - 기본은 5이고, 괄호 안에 정수를 넣어 원하는 로우수 만큼 불러올 수 있다.
df.head()
df.tail()
# sample()은 무작위로 추출하는데 기본은 1개의 로우만 가져온다.
df.sample()
# 데이터셋 요약하기
df.info()

### 결측치 보기 : isnull = isna / notnull = notna
df.isna()
# 결측치 개수 확인하기
df.isnull().sum()
# 히트맵으로 확인해보기 : 씨본 활용, cmap : 컬러셋 내에서 원하는 컬러로 지정할 수 있다.
sns.heatmap(df.isnull(), cmap = "Greys_r")
# 구매내역같은 시계열 데이터의 경우, 이런 히트맵들을 활용해서 확인할 수 있다.



### 범주형 변수에 대한 기술통계 보기
df.describe()
# 범주형 데이터에 대한 통계량 바로 보기
df.describe(include = "object")
# 모든 데이터에 대한 통계량 보기
df.describe(include = "all")

# 유일값 개수 보기
df.nunique()
# 유일값이 적은 컬럼은 범주형 변수에 더 가깝다.
# countplot으로 빈도수 시각화 하기
sns.countplot(data=df, x = "origin")



### value_counts 로 빈도수 구하기
# 한 개 변수의 빈도수 
df["origin"].value_counts()
# 두 개 이상의 빈도수 
df[["origin","cylinders"]].value_counts()
# 라고 하면 "origin"컬럼 별, "cylinders"컬럼 별 개수를 구해준다. 다소 조잡함.



### 두 개 이상의 변수에 대한 빈도수 시각화 하여 확인하기
# countplot에 hue 이용하기
sns.countplot(data=df, x = "origin", hue = "cylinders")
# 카운트플롯은 두 축이 다 지정될 수 없는데
# hue를 이용하면 색상으로 구분하여 한 가지 컬럼을 더 가져와서 두 가지를 같이 보기 가능하다.
# x와 hue 둘을 서로 바꾸어 보기도 가능하다.

# 두 개이상은 피봇 테이블이나 그룹바이를 쓸 수도 있지만 판다스에서는 크로스탭을 쓸 수 있다.

# pd.crosstab 으로 시각화 한 값 직접 구하기
# pd.crosstab([],[])
pd.crosstab(df["origin"], df["cylinders"])
# 인덱스 먼저 뒤에는 컬럼으로 올 값으로 적어서 표를 만들어준다.



### 범주형 vs 수치형 변수 (함께 쓰기)
# barplot으로 @@ 별 %% 값 구하기 : 기본 값은 평균이다.
sns.barplot(data=df, x = "origin", y = "mpg")
# 어느 지역 차가 연비가 더 좋은지 볼 수 있다.
# 기본으로 ci(신뢰구간)이 함께 나온다. 지우기 위해서 파라미터를 적어준다.
sns.barplot(data=df, x = "origin", y = "mpg", ci = None)
# hue를 이용하여 범주 추가하여 색상을 다르게 구하기
sns.barplot(data=df, x = "origin", y = "mpg", hue = "cylinders")



### groupby 를 통한 연산
# 데이터셋.groupby(by="컬럼"혹은[컬럼들])
# "origin" 별 그룹화 하고 평균 구하기
df.groupby("origin").mean()
# "origin" 별 "mpg"의 평균 구하기
df.groupby("origin")["mpg"].mean()
# "origin" 별 "cylinders" 별로 "mpg" 평균 구하기
df.groupby(["origin", "cylinders"])["mpg"].mean()
# 위의 것과 아래의 것은 같다.
df.groupby(["origin", "cylinders"])["mpg"].agg('mean')



### pivot_table을 통한 연산
# pd.pivot_table(data=데이터셋, index="x", columns="y", values="z")
# 피봇 테이블로 그룹 바이와 같은 값 구해보기 
pd.pivot_table(data=df, index = "origin", values = "mpg")
# df.pivot_table 라고 적어서 데이터를 미리 지정해줄 수도 있다.
# 그룹화를 두 개 이상으로 해줄 떄에는 리스트 형태로 묶어야 한다.
df.pivot_table(index = ["origin", "cylinders"], values = "mpg")
# agg 기본이 mean이다. agg 로 여러 통계값을 넣을 수 있다.
# 번외로 위 피봇테이블 뒤에 agg로 묶을 경우 origin 과 cylinders 에 의해 묶인 value들의 mean과 std가 출력된다.

# seaborn에서 그래프 크기 변경하기
df.hist(figsize = (12,6), bins=50)
sns.barplot(data=df, x = "origin", y = "mpg", ci=None)
# barplot 안의 hue 파라미터로 세 가지를 한번에 볼 때
sns.barplot(data=df, x = "cylinders", y = "mpg", hue = "origin")



### boxplot 과 사분위수
# catplot 안에 boxplot 이 서브로 들어가있다. 박스플롯은 범주형 데이터와 같이 쓸 수 있어서 그렇다.
# boxplot으로 @@ 별 $$ 의 기술통계값
sns.boxplot(data=df, x = "origin", y = "mpg")
# 이전에는 mean만 봤고 이것이 대표값이었다. 그러나 평균이나 중앙값을 대표값으로 사용하면 함정에 빠질 수 있다.
# 그래서 사분위수 와 이상치를 보기 위해 박스플롯을 사용한다.
# 그러나 박스 안의 값(빈도)이 달라지더라도 제대로 표현하지 못하는 단점이 있다.
# 이것을 보고 외도가 음수라고 추측하는 등 알 수 없는 부분들이 많기에 바이올린 플롯을 보는 것이 좋다.

# groupby 로 표현하고 변수에 담아서 재사용, 컬럼들 4분위수로 만들기.
desc = df.groupby("origin")["mpg"].describe()
sns.boxplot(desc)

# 박스플롯 이해하기
# IQR, 이상치를 제외한 최대 최소 값 구하기
Q1 = europe["25%"]
Q3 = europe["75%"]
IQR = Q3 - Q1
OUT_MAX = Q3 + (1.5 * IQR)
OUT_MIN = Q1 - (1.5 * IQR)
print(Q1, IQR , Q3, OUT_MIN, OUT_MAX)

# europ에 해당하는 값에 대해 boxplot 그려서 확인해보기
plt.figure(figsize=(12,2))
sns.baxplot(data=df[df["origin"]=="europe"], x = "mpg")
# boxenplot 으로 boxplot 좀 더 실감나게 그리기
plt.figure(figsize=(12,2))
sns.boxenplot(data=df[df["origin"]=="europe"], x = "mpg")



### violinplot 그리기
plt.figure(figsize=(12,2))
sns.violinplot(dtata=df[df["origin"]=="europe"], x = "mpg")
# 참고로 바이올린플롯은 kde플롯을 마주보게 그린 형태.



### 산점도를 통한 범주형 데이터 표현 
## scatterplot 으로 범주형 변수 그리기
sns.scatterplot(data=df, x = "origin", y = "mpg")
# scatterplot 으로 그릴 순 있지만 범주형 변수는 많이 겹쳐져 보여서 의미가 없어보인다.

## stripplot으로 겹쳐진 부분을 약간 옆으로 퍼져서 보이도록 그리기
sns.stripplot(data=df, x = "origin", y = "mpg")
# 이 마저도 겹쳐진 부분이 잘 안 보일 수 있어서 분포를 정확히 가늠하기 어렵다.

## 이때 swarmplot 으로 겹쳐진 만큼 옆으로 퍼지도록 그릴 수 있다.
sns.swarmplot(data=df, x = "origin", y = "mpg")
# warning 메시지가 뜨는 것은 정해진 크기 안에 다 그리지 못 할 경우이다.
# figure()를 사용해서 크기를 더 크게 정해주자.
plt.figure(figsize=(12,4))
sns.swarmplot(data=df, x = "origin", y = "mpg")



### catplot 으로 그리기
sns.catplot(data=df, x = "origin", y = "mpg")
# 이는 스트립플롯과 비슷한 형태로 그려진다.

# catplot 은 column 을 하나 더 해서, 따로 나누어서 서브플롯을 그릴 수 있다.
sns.catplot(data=df, x = "origin", y = "mpg", kind = "violin")
# col 파라미터에 cylinders 컬럼을 넣어서 cylinders 값에 따라 그래프를 나누어보기
sns.catplot(data=df, x = "origin", y = "mpg", kind = "violin", col = "cylinders") 
# col_wrap 파라미터에 수를 넣어 한 줄에 볼 그래프 개수 정해주기
sns.catplot(data=df, x = "origin", y = "mpg", kind = "violin", col = "cylinders", col_wrap = 3)

# histplot은 displot에 들어간다. 
# https://seaborn.pydata.org/tutorial/function_overview.html
# 플로리 익스프레스를 다 쓸 수 있으려면 여기 씨본을 다 익히면 된다 :)

## catplot 으로 boxplot 그리기
sns.catplot(data=df, x = "cylinders", y = "mpg", kind = "box", col = "origin")
# origin 별 cylinders 개수에 따른 mpg 값의 1-4분위수와 이상치를 볼 수 있다!
# 이렇게 캣플롯으로 다 그릴 수 있다. 

# 하지만 figsize를 사용할 수 없다.
# 이때 사이즈를 변경하려면 height 와 aspect 로 상대적 크기를 정할 수 있다.
sns.catplot(data=df, x = "cylinders", y = "mpg", kind = "box", col = "origin", height = 2, aspect = 2)
# 씨본의 여타 다른 시각화처럼 col_wrap 이 가능하다.

## catplot 으로 violinplot 그리기
sns.catplot(data=df, x = "cylinders", y = "mpg" , kind = "violin", col = "origin", height = 5, aspect = 1)
# origin 별 cylinders 개수에 따른  mpg 값의 바이올린플롯을 볼 수 있다.

## catplot 으로 countplot 그리기
# countplot 은 x에 따른 값 갯수(y에 따른 값 갯수) 즉 빈도수가 y축으로(x축으로) 들어가기 때문에
# x 와 y 둘 다 지정하면 오류가 난다. 둘 중 하나만 지정. (형태를 생각하면 까먹을 수가 없어요.)
sns.catplot(data=df, x = "cylinders", kind = "countplot", col = "origin")



### x, y 지정 없이 df로 시각화 해보기
sns.catplot(data=df, kind = "box")
sns.catplot(data=df, kind = "violin")

## 모든 컬럼이 다 들어가기 때문에 각 컬럼 마다 스케일 값이 달라서 확인하기 불편하게 그려질 수 있다.
## 이럴 때에는 몇 가지 방법이 있다.

# 1. data=df.drop([]) : 선택적으로 컬럼을 빼고 보고 싶을 때
sns.catplot(data=df.drop(["weight", "displacement"], axis =1), kind = "violin")

# 2-1. 숫자 타입 컬럼만 선택해서 보기
df.select_dtypes(exclude = "object")
# 2-2. 각 숫자 타입 컬럼이 각 해당 컬럼 평균에 비해 어느 정도인지 (값/컬럼평균값)
df.select_dtypes(exclude = "object") / df.select_dtypes(exclude = "object").mean()
# 임의의 정규화를 해보았다.(사이킷런은 이런 기능들을 다 제공함.) 진짜 normalizing은 아니지만 그려보자.
df_norm = df.select_dtypes(exclude = "object") / df.select_dtypes(exclude = "object").mean()
sns.catplot(data = df_norm, kind = "violin")

# 3-1. 표준화 하기
# 스케일을 엇비슷하게 맞추는 방법.
# 참고: standardization : 값이 평균으로부터 얼마나 떨어져 있는지를 값으로 표현.
# (Z-score 표준화) : (측정값/평균) / 표준편차
df_num = df.select_dtypes(exclude = "object")
df_stdrz = (df_num - df.num.mean()) / df_num.std()
# 주관적으로 평가기준이 다를 수 있는 '주관식 채점'같은 것에는 표준화 과정을 거친다.

# 4-1. 정규화(진짜) 하기 -번외
# 스케일을 강제로 0~1 로 맞추는 방법.
# 참고: normalization : 데이터의 상대적 크기에 대한 영향을 줄이기 위해 0~1 사이의 값으로 변환.
# (정규화) : (측정값 - 최소값) / (최대값 - 최소값)
df_min = df.select_dtypes(exclude = "object").min()
df_max = df.select_dtypes(exclude = "object").max()
df_num = df.select_dtypes(exclude = "object")
df_norml = (df_num - df_min) / (df_max - df_min)
# 4-2. 정한 데이터 프레임을 catplot-violin에 넣어버리기
sns.catplot(data=df_norml, kind="violin")
# 이때 1보다 넘는 값이 나오는 것은 이상치까지 포함해서 그려주기 때문인 듯 한데 정확하지 않아서 찜찜...
sns.catplot(data=df_norml, kind="box")
# boxplot 으로 그리고 나면 정확히 1까지 그려지는데 왜이러는 것일까요.
# 이것은 질문 드리고 추가하기로


### 크로스탭, 피봇테이블, 그룹바이 나누어진 이유
# 크로스탭 피봇 그룹바이 다있는 이유 모두가 쓸 수 있도록 해놓았다.
# 굳이 여러가지를 만들어둔 이유는 추상화 해서 사용하기 쉽게 만들어 둔 것이다.

