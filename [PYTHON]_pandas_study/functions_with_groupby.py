# 한 데이터 프레임에서 그룹바이가 되어있는 상태일때, 그 상태를 바로 변수에 담아 줄 수 있다.

# 숫자 자료형을 groupby 해보자. 숫자 자료형을 groupby 하면, 각 숫자가 key 가 되어 그룹이 만들어진다.

# groupby(level=0)
# 그룹바이로 정렬된 컬럼들을 차례로 level = 0, level = 1, ... 으로 선택하여 볼 수 있다.

# 첫 번쨰 level(그룹화된 컬럼 첫번째)로 묶어서 급여를 보고싶다면
df_grouped['급여'].sum().groupby(level=0).mean()

# reset_index()
# 그룹으로 묶어둔 데이터프레임을 풀 수 있다.
df_grouped['급여'].mean().reset_index().head()

# 그룹으로 묶어둔 데이터프레임을 가로로 눞여서 풀 수 있따.
# reset_index()에서 다중 인덱스를 가로와 세로축으로 풀어주는 것이다.
df_grouped['급여'].mean().unstack()
