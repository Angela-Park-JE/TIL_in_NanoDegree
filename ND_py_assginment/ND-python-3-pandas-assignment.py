
# 3차시 과제 진행 노트

# Pandas 연습과제
import pandas as pd
import seaborn as sns
%matplotlib inline

df = sns.load_dataset("titanic")
print(df.shape)
df.head()

# 1. groupby를 사용해서 다음의 결과가 나오도록 구해보세요.
df.groupby("embark_town")["fare"].mean()

# [못품] 2. groupby를 사용해서 deck 별로 운임요금의 "count", "mean", "sum" 값을 구합니다.
#df.groupby("deck")[[df("deck").value_counts()][df("deck").mean()][df("deck").sum()]]
#pd.groupby(df["origin"], df["cylinders"]) ???
pd.groupby("deck")["fare"].agg(["count","mean","sum"])


# 3. pivot_table 을 사용해서 alive(생존여부) 별로 age의 평균 값을 구합니다.
pd.pivot_table(data=df, index ="alive", values = "age") 

# 4. pivot_table 을 사용해서 "alive", "class" 별로 평균 fare(운임요금)을 구합니다.
pd.pivot_table(data=df, index = ("alive", "class"), values = "fare") 

# 5. class 별로 countplot 을 그리고 alive(생존여부)에 따라 색상을 다르게 표현해 주세요.
sns.countplot(data=df, x="class", hue="alive")

# 6. barplot을 그립니다. x축에는 class를 y축에는 fare를 그리고 alive 에 따라 다르게 색상을 표현해 주세요.
sns.barplot(data=df, x="class", y="fare", hue="alive")

# 7. pointplot 을 그립니다. x축에는 deck 을 y축에는 fare를 그립니다. alive 에 따라 다른 색상으로 표현해 주세요.
sns.pointplot(data=df, x="deck", y="fare", hue="alive")

# 8. lmplot으로 x축에 age 값을 y축에 fare 를 그리고 class 에 따라 다른 색상으로 표현되게 합니다.
sns.lmplot(data=df, x="age", y="fare", hue="class")

# [못품] 9. age 와 fare 에 따른 상관계수를 구하고 결과를 df_corr 에 할당해 주세요.
df2 = df[["age","fare"]].corr()
df2

# 10. 위에서 만든 상관계수를 heatmap 으로 표현해 주세요.
# 참조 sns.heatmap(data=corr, cmap="coolwarm", vmin = -1, vmax=1)
sns.heatmap(data=df2, annot=True, cmap = "Blues")

###문제
# 2. 데이터프레임에서 isnull()를 통해 결측치 여부를 확인해 볼 수 있습니다.이렇게 확인한 결측치의 비율을 구해볼 수 있는 것은 무엇일까요? 
df.isnull().mean()

# 5.박스플롯을 그렸을 때 알 수 있는 것이 아닌 것은?
평균? 이상치?

# 6.다음 바이올린 플롯에 대한 설명으로 적절하지 않은 것은?
평균을 알 수 있다?

# 7. lmplot에 대한 설명으로 바르지 않은 것을 찾아주세요.
막대그래프로 표현할 수도 있다.

# 8. 수치형 데이터의 서브플롯을 위한 relplot 에 대한 설명으로 바르지 않은 것을 찾아주세요.
kind를 통해 scatter, line 을 지정해 시각화 할 수 있다.
