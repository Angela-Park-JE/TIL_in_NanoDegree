# 0303 수치형변수 요약 조회 및 시각화

### 라이브러리 로드 및 버전 확인
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print(pd.__version__)
print(sns.__version__)
# 0.11.0 버전 이상을 사용. 안되어있다면 커맨더에서 !pip install seaborn --upgrade

# dataset 로드
df = sns.load_dataset("mpg")



### 데이터 일부만 보기

df.head()
df.tail()
df.sample(5)

# 데이터 요약하여 보기
df.info()
# 결측치 보기
df.isnull()
# 결측치 갯수 확인하기
df.isna().sum()
# 결측치 비율(해당컬럼 중) 확인하기
df.isna().mean() * 100

# 기술통계 보기 (수치로 적힌 데이터만 가져온다.)
df.describe()
# 모든 컬럼 보기
df.describe(include="all")
# object 컬럼만 보기 (count, unique, top, freq)
df.describe(include="object")



### 수치형변수 값 확인 및 판다스 히스토그램

# 수치형 변수의 unique 값 확인하기
df["mpg"].unique()
# 고유한 값이 많을 시 수치형변수로 간주한다. 적을 경우 범주형으로 간주한다.

# - 그래프 상단의 로그가 출력되지 않게 하려면
plt.show() #를 코드 아래 함께 적어준다.

# - 그래프의 사이즈를 조절하려면
%matplotlib inline #을 미리 실행해둔다.
# 그리고 시각화 함수 파라미터로
# figsize=(n, n)


## .hist() : 수치변수에 대한 히스토그램
# 히스토그램 안에서 막대가 붙어있으면 연속된 수치형 데이터, 비어있는 곳들이 많을 수록 범주형 데이터라고 볼 수 있다.
df.hist(figsize=(12,6), bins=25)
# 파라미터에 bins=n 으로 계급구간 개수를 지정할 수 있다. 그려보고 정해주기.
# 구간 안의 빈도수를 보여주기 때문에 막대 개수에 따라 y축 범주가 바뀐다.


## .skew() : 수치변수에 대한 왜도 구하기
df.skew()
# 실수 값 확률 변수의 확률 분포 비대칭성을 나타내는 지표
# 왜도가 정의되지 않을 수도 있음.
# 음수일 경우 x가 큰 쪽으로, 양수일 경우 x가 작은 쪽으로 자료분포가 치우쳐있음.
# 평균과 중앙값이 같으면 왜도는 0. 0에 가까울 수록 분포도가 대칭으로 나타난다.
#---결과 예시 : horsepower      1.087326

## .kurt() : 수치변수에 대한 첨도 구하기
df.kurt()
# 관측치들이 어느 정도 집중적으로 중심에 몰려있는지 측정.
# 확률분포의 뾰족한 정도를 나타낸다. 첨도값(K)가 3에 가까울 수록 산포도가 정규분포에 가깝다.
# 3보다 작으면 뾰족하고 3보다 큰 양수일 경우 완만하다.
# 기본은 Fisher's 정의를 따른다.

# mpg 값에 대해 agg(aggrigation)으로 skew, kurt 값 같이 구하기
df["mpg"].agg(["skew", "kurt"])



### 수치형변수로 씨본 그래프

## 한 개의 수치변수 시각화하기

# displot() : 히스토그램 그리기
sns.displot(data=df, x = "mpg")
# kdeplot 넣어주기 (부드러운 밀도추정곡선 그리도록 하기)
sns.displot(data=df, x = "mpg", kde = True)

# kdeplot() : 밀도함수(Kernel Density Estimation) 표현하기
sns.kdeplot(data=df, x = "mpg")
# 판다스에서도 kde 그대로 씀

# rugplot() : 밀도가 어디에 많이 몰려있는지 한 그래프에 함께 볼 수 있음
sns.kdeplot(data=df, x = "mpg", shade = True)  # 색 칠하기
sns.rugplot(data=df, x = "mpg")
# 물론 러그플롯은 따로도 쓸 수 있음

# boxplot() : 사분위수 표현하기
sns.boxplot(data=df, x = "mpg")
# 25%, 중앙값, 75% 값을 박스형태로 보여주며 이상치도 함께 그려진다.
# 이때 아웃라이어를 확인하기 위해 describe()로 기술통계값을 구해볼 수 있지만
# 통계값 안에 있는 최소 최대는 아웃라이어를 제외한 값만 나타난다.

# violinplot() : 박스플롯 보완하기
sns.violinplot(data=df, x = "mpg")
# kdeplot을 마주보게 그리면 비슷하지만, 밀도 추정에 파라미터 설정이 다르다.
# 바이올린 플롯은 kde 플롯을 적분 했을 떄 1이 되도록 설정하고 밀도를 추정한다.


## 전체 변수 박스플롯으로 스케일 차이 확인하기
# boxplot() : 전체 변수를 박스플롯 형태로 보여준다.
sns.boxplot(data=df)
# 스케일 값이 차이가 많이 나면 그래프가 이상해진다.
# 이때 전체 변수의 표준편차를 구해본다.
df.std()
# 표준편차가 극히 차이날 경우, 머신러닝 할 때 스케일 값을 0~1로 변경해서 학습시킨다.



### 회귀분석 : scatter 그래프 및 회귀선
# scatterplot() : 2개 이상의 수치변수 비교하는 점 스캐터그래프 그리기
sns.scatterplot(data=df, x = "mpg", y = "horsepower")
# 양 혹은 음의 상관관계를 파악할 수 있다.

# regplot() : 회귀선 시각화
sns.regplot(data=df, x ="mpg", y = "horsepower")
# 값들에 따라 회귀선에 가깝거나 멀다. 분류(범주), 회귀(수치)...
# scatterplot에 회귀는 선을 그려 예측하는 것이다.
# 선에서 값이 얼마나 떨어져 있느냐를 '잔차'라고 한다. (오차 같은 것)

# residplot() : 회귀선을 0에 두고 잔차를 시각화
residplot(data=df, x = "mpg", y = "horsepower")
# 실제값과 예측값과 얼마나 차이가 있나 궁금할 때 그릴 수 있다.

# lmplot() : 회귀선 시각화, regplot은 hue를 지원하지 않기 때문에 사용
sns.lmplot(data=df, x = "mpg", y = "horsepower", hue = "origin", col = "origin")


## jointplot() : 2개의 수치변수에 대해 scatterplot과 hist 함께 표현하기
sns.jointplot(data=df, x = "mpg", y = "horsepower")
# 각 변수에 대한 histogram과 둘의 scatterplot을 보여준다.
# 사이드의 histplot은 scatterplot의 범주 기준으로 보여준다.

# scatterplot 형태를 헥사곤으로 표현하기
sns.jointplot(data=df, x = "mpg", y = "horsepower", kind = "hex")
# scatterplot 형태를 등고선으로, hist를 kde 선으로 표현
sns.jointplot(data=df, x = "mpg", y = "horsepower", kind = "kde")

#- 각 범주 형태에 따라 공통적으로 여러 그래프를 그려본다.
#- 데이터를 봤을 때 요약된 데이터만으로는 알 수 없고, 
#- 범주형/수치형 변수를 표현하는데 적합한 그래프가 각각 다르다.


## pairplot으로 전체 데이터를 서로 비교하여 시각화
# pairplot() : 각 변수를 x,y 로 서로 붙여 그려보는 그래프
# 관측값들이 많을 수록 시간이 더더욱 많이 걸리기 때문에 일부 샘플을 추출해 그려본 후 샘플의 수를 늘려가며 그리는 것을 추천.
df_sample = df.sample(100)
sns.pairplot(data=df_sample)

# 이때 hue 파라미터에 나눠보고 싶은 범주형 변수를 넣어 그릴 수 있다.
df_sample = df.sample(100)
sns.pairplot(data=df_sample, hue = "origin")

# 이때 corner 파라미터로 자신을 비교하는 대각선 기준으로 대칭되는 그래프를 뺄 수 있다.
df_sample = df.sample(100)
sns.pairplot(data=df_sample, hue = "origin", corner = True)

# variance가 0이면 warning이 뜨기도 한다. 대각선 위의 것은 안그릴때 쓴다. warning 뜰때를 대비해 ignore를 쓰기도 한다 (?)
# 보고용으로 쓰려면 warning message를 빼고, 학습용이면 되도록 출력해서 같이 보길 추천.
# 하지만 출력을 하는 것을 추천한다. 앞으로 라이브러리가 어떻게 개선해나가고자 하는 지를 알 수 있다. 공지성 메세지 같은 것.


## lineplot으로 신뢰구간 함께 나타내기
# lineplot() : 선 그래프에 신뢰구간(ci) 함께 시각화
sns.lineplot(data=df, x = "model_year", y = "mpg")
# ci = conidence interval
# 값이 많을 수록 시간이 오래걸린다. (n_boot = 1000 즉 값이 천 개일 때를 가정하고 그에 맞춰 그리기 때문에 오래 걸린다.)

# ci를 지우고 그리면 더 빠르게 그릴 수 있다.
sns.lineplot(data=df, x = "model_year", y = "mpg", ci = None)

# random forest. 샘플의 갯수가 많이 없을 땐 개수를 boot하여 쓴다고 한다.
# 이는 의사결정 나무에서 따온 것이라고 한다.
# https://blog.naver.com/freed0om/222006726927 


## relplot으로 범주형 변수에 따라 서브플롯 그리기
sns.relplot(data=df, x = "model_year", y = "mpg")
# relation plot의 의미

# kind 기본값은 scatter. line으로 바꿀 수 있다.
sns.relplot(data=df, x = "model_year", y = "mpg", kind = "line")
# 범주형 변수를 hue, col 등에 넣을 수 있다.
# line으로 그릴 경우 ci를 뺄 수 있다.
sns.relplot(data=df, x="model_year", y="mpg", kind="line", col="origin", hue="origin", ci=None)

# relplot에 전체 수치 변수에 대한 시각화 가능
sns.relplot(data=df) 
# 마찬가지로 kind 옵션 line으로 변경 가능
# 스케일에 따라 알아보기 어려울 수 있기 때문에 정규화해서 그리는 경우가 많다.



### 상관분석 : corr 와 sns.heatmap()
# 두 변수간의 연관된 정도를 나타낼 뿐 인과관계를 설명하는 것은 아니다.
# 피어슨 상관계수 : r 값은 X 와 Y 가 완전히 동일하면 +1, 전혀 다르면 0, 반대방향으로 완전히 동일 하면 –1 을 가진다.

# 데이터프레임 전체의 수치 변수에 대해 상관계수 구하기
# 변수를 따로 지정하지 않으면 피어슨 상관계수가 기본으로 지원된다.
corr = df.corr()
# 결과로 각 컬럼간의 서로의 상관관계를 구하여 데이터프레임이 반환된다.
# 자기 자신과의 상관계수는 1이다. 그래서 대각선 방향으로 값이 1이고,
# 대각선 기준으로 값들은 서로 마주본다(대칭된다).

### 히트맵 그리기 
sns.heatmap(data = corr)
# vmin, vmax 파라미터: 히트맵 내 값 최대 최소 정해주기
sns.heatmap(data = corr, vmin = -1, vmax = 1)

# 히트맵 컬러 선택해보기
print(plt.colormaps())
# 맷플랏립의 컬러들이다. sequancial이면 한 가지 색상을 그라데이션 하는 것을 추천.
# _r은 reverse로 본래 것의 값에 음양 색상을 스위칭 한 것임.
['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'crest', 'crest_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'flare', 'flare_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'mako', 'mako_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r']

# cmap 파라미터 : 히트맵 컬러 입히기
sns.heatmap(data = corr, cmap = "coolwarm", vmin = -1, vmax = 1)

# mask 파라미터: 히트맵 마주보는 곳 지우고 출력하기
# np.triu : matrix 를 상삼각 행렬로 만드는 numpy math이다.
# np.ones_like(x) : x와 크기만 같은 1로 이루어진 array를 생성한다.
# 이를 활용하여 매트릭스에서 대각선 기준으로 0을 넣고 이를 히트맵에 입히면 
# 0이 masking된 한 쪽 대각선은 색상으로 나타나지 않는다.
# 다시 말해 np.ones_like(df)는 df크기의 행렬 array를 만들고
# np.triu는 행렬 array에 대각선 방향으로 남은 곳들의 값을 비도록(0이 되도록) 만든다. 
mask = np.triu(np.ones_like(corr)) 
# 이를 실행시키고 mask를 mask라는 파라미터 값으로 넣는다.
# mask 파라미터는 0값이 곳은 출력을 하지 않나보다.



