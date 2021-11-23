# 0202-anscombe-seaborn-pandas-input.ipynb

# pandas, seaborn, numpy 
# 변수를 잘 맞게 지정을 해주자. 나중에 헷갈린다.
import pandas as pd
import seaborn as sns
import numpy as np

# 데이터 로드: 가끔 안될 때가 있다. 이럴때는 이렇게 지정해서 불러온다.
# df = sns.load_dataset("anscombe")
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/anscombe.csv")
# df.shape

### 데이터 셋에서 일부 데이터만 가져오기
df.head()
df.tail()
df.sample()

### ---

### 컬럼 값 기준에 따라 개별 Dataset 만들기
# bool Indexing [[]] !!!
# df_1, df_2, df_3, df_4 로 나누어 만들기
# 'dataset'이라는 컬럼 값 기준에 따라 하위 개별 데이터셋 sub set 만들기
df_1 = df[df["dataset"] == "I"]
df_2 = df[df["dataset"] == "II"]
df_3 = df[df["dataset"] == "III"]
df_4 = df[df["dataset"] == "IV"]
df_1.shape, df_2.shape, df_3.shape, df_4.shape # 각 서브셋 모양 확인하기

# 개별 게이터 셋의 기술통계량
df_1.describe()
df_2.describe()
df_3.describe()
df_4.describe()
# 평균은 거의 같지만 min, max가 조금씩 다르다.

### 분명 다른 데이터인데, 평균은 같을 때.
# 각 컬럼사이의 상관계수 구하기
df_1.corr()
df_2.corr()
df_3.corr()
df_4.corr()
# 소수점 3째 자리 까지 같다. 이럴때 '분석해봤더니, 상관관계가 이렇게 있으므로 비슷한 데이터'라고 보고를 할 수도 있다.
# 그러나

### Series 의 빈도수 구하기
# value_counts 통해 빈도수 구하기
df["dataset"].value_counts()
# value_counts 를 통해 dataset의 빈도수를, normalize로 전체 데이터 중 비율 구하기
df["dataset"].value_counts(normalize=True)


### Groupby 를 통한 dataset 별 기술통계량 보기
# pandas에 그룹바이를 제공하므로, 하나씩 할 필요가 없다.
# desc => df.groupby("dataset")[["x", "y"]].describe()
# 묶어보고 싶은 컬럼을 기준으로 groubpy하기. 
df.groupby("dataset").describe()
# 요약된 기술통계량 만으로는 비슷하다는 결론을 낼 수 있다.

### 상관계수 - 양의 상관관계 음의 상관관계
df.groupby("dataset").corr()
# heatmap!!!

### seaborn 시각화
# 축을 변경하여 그리기
# x = "000" 대신 y = "000"

# cplot 빈도수
sns.countplot(data=df, x="dataset")

# barplot 기본으로 평균값을 알려준다.
sns.barplot(data=df, x="dataset", y="x")
sns.barplot(data=df, x="x", y="y")

# estimator
# ci는 신뢰구간을 의미한다.
sns.barplot(data=df, x="dataset", y="y", ci="sd")
# estimator는 ?
# sns.barplot(data=df, x="dataset", y="y", ci="sd")
sns.barplot(data=df, x="dataset", y="y", estimator=np.sum)
# groupby를 통 barplot의 y값 직접 받아내기
# [[]]!! 2차원으로 감싸주기
df.groupby("dataset")[["x","y"]].mean()

# boxplot 
# 4분위수를 표현해준다. 맨밑이 이상치를 제외한 최소값, 맨위가 이상치를 제외한 최대값. 
sns.boxplot(data=df, x="dataset", y="y")
#박스안에 분포를 알기 어렵다는 그런 단점을 보완한게 바이올린 플롯.

# violinplot
sns.violinplot(data=df, x="dataset", y="y")

# scatterplot
sns.scatterplot(data=df, x="x", y="y", hue="dataset")

# 범례 원하는 위치로 바꾸기
import matplotlib.pyplot as plt
sns.scatterplot(data=df, x="x", y="y", hue="dataset")
plt.legend(loc=4)

# regplot 
sns.regplot(data=df, x="x", y="y")

# 신뢰구간 범위 없애버리기 ci = False
sns.regplot(data=df, x="x", y="y", ci=False)

# lmplot 선형모델
sns.lmplot(data=df, x="x", y="y", hue="dataset")
# 각 세그먼트별로 나눠받기
# col = "나눠볼 세그먼트"
sns.lmplot(data=df, x="x", y="y", hue="dataset", col = "dataset")
# 나눠 받은 것을 병렬로 받기
# col_wrap = 한 줄에 표시할 그래프 수
sns.lmplot(data=df, x="x", y="y", hue="dataset", col="dataset", col_wrap=3)
# x값 범주 평준화시켜보기
# truncate = False
sns.lmplot(data=df, x="x", y="y", hue="dataset", col="dataset", col_wrap=2, truncate=False)
