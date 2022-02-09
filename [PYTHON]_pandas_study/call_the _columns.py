# column을 부르는 방법은 두 가지가 있다. 사람에 따라 다르게 쓰는 것 같다.
# 아래 두 명령의 결과는 같다.

wine_reviews.country
wine_revies['country']

# 이를 이렇게 볼 수도 있다.

wine_reviews[taster_name].value_counts()
wine_reviews.taster_name.value_counts()
