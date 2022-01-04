

# 0102 제어문과 함수


### if

# 정수를 입력받아 양수음수 판별
y = int(input("써라 : "))
if y > 0:
  print("양수")
elif y < 0:
  print("음수")
else :
  print("아마도 0이지?")


### for - 반복문
alchol = ['와인', '브랜디', '맥주', '위스키', '소주', '동동주']
for i in alchol:
	print(i)

## range()
# range로 범위를 지정하여 반복문 수행
for i in range(6):
	print(i)
# 1부터 10까지 2씩 더하여 고르기 : 홀수만 출력하기
for i in range(1,10,2):
	print(i)

## 리스트를 변수로 받아 순회할 수도 있지만 리스트의 길이만큼 range값을 생성하여 순회할 수도 있다.
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(a[i])

## enumerate()
# 인덱스 번호와 값을 함께 가져올 수 있다
for i, val in enumerate(a):
	print(i, val)

## range로 합계 구하기
range(4) 
	# range(0,4)
sum(range(4))
	# 6

## 리스트 만들기
list(range(4))



### 조건문 + 반복문
for i in range(1,10):
	if i%2 == 1:
		print(i, "홀수")
	elif i%2 == 0:
		print(i, "짝수")
	else:
		print("정수가 아닙니다.")



### while 문
# 조건문이 참인 동안 순회하며 실행되기 때문에 특정 조건까지 반복문을 수행하고자 할 때 사용
# 변수가 특정 변수값이 되면 종료하도록.
변수 = 0
제한 = int(input("0부터 시작할 건데 정수 몇 까지 출력하고싶으시죠?"))
while True:
	print(변수)
	변수 = 변수 + 1
	if 변수 == 제한 + 1:
		break


		
### 함수 만들기 
#- 평균을 구하는 함수
def average(parameter):
	avg = sum(parameter) / len(parameter)
	return avg

#- 합을 구하는 함수
def total_sum(parameter):
	sum_n = 0
	for n in num:
		sum_n = sum_n + n
	return sum_n



