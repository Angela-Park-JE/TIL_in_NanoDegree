# 참고 : https://bigdaheta.tistory.com/42

### 1. loc
#loc = 데이터프레임의 행 또는 컬럼의 label이나 boolean array로 인덱싱한다.
#사람이 읽을 수 있는 라벨 값으로 특정 값들을 골라오는 방법.

df.loc[행 인덱싱 값, 열 인덱싱 값]
# 숫자와 컬럼네임을 함께 적어주면 특정위치 값을 출력시킬 수 있다.

# 인수 숫자 하나를 입력하면 인덱싱 넘버로 알아듣는다.
# loc를 이용하여 컬럼을 전체 보고 싶다면,
# df['컬럼명'] = df.loc[ : , '컬럼명']

## 슬라이싱이 가능하다.
# [ : , : ]라고 적으면 처음부터 끝까지 가져온다.


## 그리고 loc는 불린으로 특정 값을 추출해 올 수 있다. 
# 전체 DataFrame에서 특정한 조건을 만족시키는 값들만 추출해 올 수 있다.

#(1) 추출하려는 특정 조건을 하나의 변수로 정해준다.
cond1 = df["cylinders"] == 4
#(2) 변수를 loc에 넣어버린다.
df.loc[cond1]
#(3) 물론 조건을 []안에 직접 넣어도 알아듣는다.
df.loc[df["cylinders"] == 4]
#(4) 물론 조건을 | 나 & 을 사용하여 다중으로 걸어도 알아듣는다. 괄호 주의!
df.loc[(df["cylinders"] == 4) & (df["mpg"] >= 18)]



### 2. iloc
# iloc = integer location. DataFrame의 행이나 컬럼의 순서를 나타내는 정수로 특정 값을 추출해오는 방법이다.
# loc는 사람이 읽기 좋은 방법으로 접근, iloc는 컴퓨터가 좋아하는(숫자)로 데이터가 있는 위치(순서)에 접근한다.
pirnt("주의할 점은 컬럼의 이름을 직접 입력해주면 못 알아듣는다.")

df.iloc[행 인덱스, 열 인덱스]
# 숫자와 숫자로 특정 위치의 값을 출력시킬 수 있다.

# 인수 숫자 하나를 입력하면 인덱싱 넘버로 알아듣는다. (loc와 같은 결과)

## 슬라이싱이 가능하다.
# :5 는 0~4 인덱스를 가져오는 것을 꼭 주의하자.
 
## iloc도 특정 조건의 행 또는 열만 추출 할 수 있다.
# 주의할 점은 컬럼 이름을 입력하는 조건은 못 알아듣는다.
# 짝수번째에 위치한 행들만 추출하고 싶다면 
df.iloc[::2,:]
# df 전체 값 중에, 2 간격으로 추출하고, 열은 전체를 가져오라는 의미.
# 컬럼에도 동일하게 적용할 수 있다.
