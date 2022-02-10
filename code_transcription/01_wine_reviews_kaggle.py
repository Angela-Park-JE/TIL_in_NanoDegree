### dataset reference: https://www.kaggle.com/zynicide/wine-reviews/code?datasetId=1442&sortBy=voteCount



### importing required packages.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier # 앙상블 모델 
from sklearn.svm import SVC # ?
from sklearn.linear_model import SGDClassifier # 선형회귀를 통한 분류모델
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
%matplotlib inline

# Loading dataset
wine = pd.read_csv('/content/drive/MyDrive/AI/2nd/winemag-data-130k-v2 (1).csv')



### viewing
wine.head()
wine.info()
wine.country
wine.iloc[0]
wine.iloc[15:20,:7]
wine.iloc[-3:] # 끝에서 3줄 가져오기



### EDA little 1
wine.loc[:,['taster_name','taster_twitter_handle','points']]
wine.country.unique()
wine.country == 'US'
wine.loc[wine.country == 'US']
wine.loc[wine.country.isin(['Italy', 'France', 'Spain'])]



### EDA little 2 : by country
by_country = wine.groupby(['country', 'points']).taster_name.agg('count')
