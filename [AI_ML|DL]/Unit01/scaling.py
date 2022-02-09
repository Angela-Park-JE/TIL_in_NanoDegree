### call the libraries
import pandas as pd
import numpy as np

from scipy import stats

from mlxtend.preprocessing import minmax_scaling # 새로운 것을 보여드리기 위해 mlxtend.preprocessing을 가져왔습니다.

import seaborn as sns # 예쁘게 그리면 설득력이 될 수 있으니 여기서 이렇게 쓰세요
import matplotlib.pyplot as plt

np.random.seed(0)


# 지수 분포에서 무작위로 추출한 1000개의 데이터 포인트 생성
original_data = np.random.exponential(size=1000)

# mix-max 0과 1 사이의 데이터 스케일
scaled_data = minmax_scaling(original_data, columns=[0])

# 비교하기 위해 둘 모두를 그래프로 그림
fig, ax = plt.subplots(1,2) # 한 열에 두 개의 서브 플롯을 만들겠다.
sns.distplot(original_data, ax=ax[0]) # 그래프를 0번째에 그리고
ax[0].set_title("Original Data") # 1행 0번 제목을 추가해준 것!
sns.distplot(scaled_data, ax=ax[1]) # 그래프를 1번째에 그리고 - 서브플롯으로 묶여있어서 가능한 일이다.
ax[1].set_title("Scaled data") # 1행 1번 제목을 준 것.


# 왼쪽으로 치우친 것을 log 함수를 넣었을 때 우측으로 왜도가 변한다. 
sns.distplot(np.log(original_data))
