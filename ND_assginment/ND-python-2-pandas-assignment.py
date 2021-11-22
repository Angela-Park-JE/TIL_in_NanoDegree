# 0202-anscombe-seaborn-pandas-input.ipynb

# pandas, seaborn, numpy 
# 변수를 잘 맞게 지정을 해주자. 나중에 헷갈린다.
import pandas as pd
import seaborn as sns
import numpy as np
### 과제를 위해 다음의 셀을 실행해 주세요.

import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

# 1. 행과 열의 갯수를 출력해 주세요.
df.shape

# 2. 결측치의 수를 세어주세요. (Googling)
df.isnull().sum()

# 3. alive 의 수를 그룹화해서 세어주세요.
df["alive"].value_counts()

# 4. age의 요약값을 구합니다.
df["age"].describe()

# 5. object 타입의 요약값을 구합니다.
df.describe(include="object")

# 6. embark_town 컬럼의 값을 소문자로 변경 후에 "embark_lower" 라는 새로운 컬럼에 담아주세요.
df["embark_lower"] = df["embark_town"].str.lower()

# 7. embark_lower 컬럼에서 south 가 들어가는 데이터의 수를 세어보세요.
df["embark_lower"].str.contains("south").sum()

# 8. age 컬럼의 값이 15 이하인 값을 구합니다. True, False로 표시되는 값을 child 라는 새로운 컬럼에 담아주세요.
df["child"] = df["age"] <= 15

# 9. 위에서 만든 child 컬럼을 통해 child 의 값을 그룹화 해서 세어봅니다.
df["child"].value_counts()

# 10. embarked 컬럼의 값이 C 이고 pclass 가 3에 해당되는 값만 가져와서 데이터프레임으로 만든 뒤 행과 열의 수를 세어주세요.
df[(df["embarked"]=="C")&(df["pclass"]==3)].shape

# 11. fare 가 500보다 큰 값을 출력합니다.
df[df["fare"]>500]["fare"]

# 12. pclass 가 3이고 embarked 가 Q인 fare 의 평균을 구해주세요.
df[(df["pclass"]==3)&(df["embarked"]=="Q")]["fare"].mean()

# 13. fare 가 50 보다 큰 데이터에서 class 를 그룹화 해서 갯수를 세어보세요.
df[df["fare"]>50]["class"].value_counts()

# 14. fare 가 10 보다 크거나 같고 50 보다 작거나 같은 데이터만 가져와서 데이터프레임의 갯수를 출력해 주세요.
df[(df["fare"]>=10)&(df["fare"]<=50)].shape

# 15. age 의 결측치를 0 으로 채워서 age_fill 이라는 컬럼에 담고 age_fill 컬럼의 평균값을 출력해 주세요.
df["age_fill"] = df["age"].fillna(0)
df["age_fill"].mean()

# 16. deck 컬럼을 그룹화 해서 갯수를 카운트하고 A~G 순으로 정렬이 되도록 해주세요.
df["deck"].value_counts().sort_index()

# 17. pclass 컬럼의 값이 1 인 fare의 중앙값을 구해주세요.
df[df["pclass"]==1]["fare"].median()

# 18. embarked 가 C 이거나 deck 이 F인 데이터에서 age 컬럼의 평균값을 구해주세요.
df[(df["embarked"]=="C")|(df["deck"]=="F")]["age"].mean()

# 19. alive 가 yes 이고 alone 이 True인 값의 데이터프레임의 행과 열의 수를 출력해 주세요.
df[(df["alive"]=="yes")&(df["alone"]==True)].shape

# 20. age 를 역순으로 정렬하고 상위 5개만 출력합니다.
# df.sort_values(by = ["age"], ascending=False).top()
# df.sort_values(by=["가격","약품명"]), ascending = [False, True]
df["age"].sort_values(ascending=False).head()



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
