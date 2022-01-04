
```python
import scipy.stats as spt
import numpy as np
import pandas as pd
import seaborn as sb
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import statsmodels.stats.weightstats as sw
import matplotlib.pyplot as plt
```

```python
# Two sample t test

fres = np.array([3.7,4.3,2.5,3.3,3.6,3.1])
soph = np.array([1.8,4.2,4.1,2.2,3.2,3.8])
twosam = spt.ttest_ind(fres,soph)
print(twosam)

print('t statistic = %.3f, p-value = %.3f'%(twosam))

print('1학년 :', np.mean(fres))
print('2학년 :', np.mean(soph))
```

ANOVA는 표본의 집단이 3개 이상일 때 사용.

표본 집단이 1개나 2개일 때에는 T테스트를 한다.

평균값이 차이가 있는지 없는지 확인하는것. 집단의 이질성이 있나 없나 확인하는 것.

```python
# Dataframe

data1=pd.DataFrame(data=np.array([[3.7,1.8,3.3,4.1],[4.3,4.2,3.7,3.8],[2.5,4.1,3.4,3.5],[3.3,2.2,3.9,3.2],[3.6,3.2,np.nan,2.3]]),
                   columns=['fre','sop','jun','sen'])
print(data1['jun'],'\n')

sop = data1['sop']
jun = data1['jun']
jun = jun.fillna(jun.mean())

print(jun,'\n')

tsam = spt.ttest_ind(sop,jun)
print(tsam)
```

```python
# Paired t test

before=np.array([68,61,60,68,67,64,66,67,66,67,72,74,61,71,58,77])
after=np.array([56,55,67,62,59,67,50,60,59,53,60,65,62,61,64,57])

pairsam = spt.ttest_rel(before,after)
print(pairsam)
```

```python
# Statsmodels를 이용한 t test

fre=data1['fre']
sen=data1['sen']

# 가설에는 two-sided / larger / smaller 3가지, 분산에는 pooled, unequal 2가지, value는 두 집단의 평균 차이가 얼마인지 나타내는 수
tsams=sw.ttest_ind(fre,sen,alternative='two-sided',usevar='pooled',value=0)
print('tstat = \t',tsams[0],'\np-val = \t',tsams[1],'\ndegree of freedom = \t',tsams[2])

# 쌍체검정 (One-sided)

ptsams = sw.ttost_paired(before,after,0.1,0.2)
print(ptsams)
```

```python
# Two-way ANOVA from statsmodels // Referred : https://www.statsmodels.org/stable/anova.html#module-statsmodels.stats.anova

moore = sm.datasets.get_rdataset("Moore", "carData", cache=True)

data2 = moore.data

data2 = data2.rename(columns={"partner.status":"partner_status"})

moore_lm = ols('conformity ~ C(fcategory, Sum)*C(partner_status, Sum)',data=data2).fit()

table = sm.stats.anova_lm(moore_lm, typ=2)

print(table)
```
