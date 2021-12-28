# datetime 끼리의 연산으로 인해 나온 timedelta 타입의 데이터를 월이나 시간으로 보고 싶을 떄 사용한다.
# 이걸 찾느라 시간을 많이 버렸다.

# df_2 에 "del_lead_time"을 날짜 단위로 변경하고 싶을 떄

df_2["1del_lead_time"] = df_2["del_lead_time"].dt.days

# 시간 단위로 변경하는 것은 못찾았다. 날짜 단위로 자르는 수밖에.
