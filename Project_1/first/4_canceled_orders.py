# 주문취소가 된 건들은 뭘까?

# 1. STATUS 고유값 보기
df_scdprice['STATUS'].unique().tolist()

# ['processing',
#  'delivered',
#  'canceled',
#  'shipped',
#  'invoiced',
#  'unavailable',
#  'approved']


# 2. 주문테이블에서 주문 취소가 된 것들의 특징을 보자
    # df_scdprice 

df_canceled_orders = df_scdprice[df_scdprice['STATUS'] == 'canceled']
df_canceled_orders
    # 566 rows × 18 columns

# 3. 가격과 관계가 있나?
# 취소되지 않은 건들의 가격대와 취소된 건들의 수를y, 가격x 그래프로 그리기
sns.countplot(data=df_scdprice, x="PRICE", hue="STATUS")
    # 나오는 데에도 오래걸렸고, 매우 불편하게 나온다. 보기도 어렵다.

# 3-1. 가격과의 관계성 쉽게 보기
sns.lineplot(data=df_scdprice, y="PRICE", x="STATUS" )
    # 특별히 차이가 없어보인다. 실제로 수치를 내보면,

# 3-2. 상태별 가격의 평균
df_scdprice.groupby(by='STATUS').mean()[['PRICE']]

# approved	69.866667
# canceled	179.047085
# delivered	120.083702
# invoiced	169.701159
# processing	169.226160
# shipped	132.885651
# unavailable	286.812857
    # 취소된 건이 약간은 더 많지만, 실제로 많은 차이를 보이지는 않는다.

# 4. 셀러별 취소건 개수는 분포가 어떨까? 특별히 많은 사람이 있을까?
sns.countplot(data=df_canceled_orders, x="SELLER_ID")
    # 보통은 한 건인데 4번 이상인 사람들은 문제가 있어보인다.

# 4-1. 취소 건수가 많은(4번 이상인) 셀러들을 보고싶은데...
# 여기서 잠깐, 원래 많이 팔다보니 취소 건 비율도 늘어나는 것일 수 있다.
# 그렇기에 df_canceled_orders 데이터만 볼것이 아니라 df_selocus 을 보는게 나을 수 있다.
df_canceled_orders1.describe(include="all")[["SELLER_ID","CATEGORY","PRICE"]]

#-- 중단
