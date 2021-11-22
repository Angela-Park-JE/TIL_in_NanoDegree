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


