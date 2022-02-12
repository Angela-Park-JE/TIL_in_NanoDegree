### 설정

cnt = 0
movies['영화이름'] = ''
movies['영화이름'][0] = action_list['영화이름'][cnt]
movies['영화코드'] = ''
movies['영화코드'][0] = action_list['영화코드'][cnt]
movies['개봉일'] = ''
movies['개봉일'][0] = action_list['개봉일'][cnt]


### for 문
# 조건에 맞을 때 변화를 주고 그렇지 않도록 한 상태이다.

# movie_code 도 넣고 싶으면 movie_list와 동일하게 만들어서 

for i in trange(1,len(movies)):
    if (movies['공감차이'][i] - movies['공감차이'][i-1]) <= 0:
        movies['영화이름'][i] = action_list['영화이름'][cnt]
        movies['영화코드'][i] = action_list['영화코드'][cnt]
        movies['개봉일'][i] = action_list['개봉일'][cnt]       
    else:
        cnt += 1
        movies['영화이름'][i] = action_list['영화이름'][cnt]
        movies['영화코드'][i] = action_list['영화코드'][cnt]
        movies['개봉일'][i] = action_list['개봉일'][cnt]
