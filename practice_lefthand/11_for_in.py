## 왼손코딩 연습문제 복습하기
# Ch.11 횟수로 반복하기 연습문제


## 다음 코드의 출력 결과는?
for num in range(2):
	print(num)

	0
	1


## print()를 한번만 사용해서 아래 코드와 같은 결과가 나오게 하기
clovers = ["클로버1", "클로버2", "클로버3"]
print(clovers[0])
print(clovers[1])
print(clovers[2])
클로버1
클로버2
클로버3

    clovers = ["클로버1", "클로버2", "클로버3"]
    for i in clovers:
        print(i)

    # 다른 방법 - 인덱스를 넣어주기
    for num in [0, 1, 2]:
        print(clovers[num])


## for 와 range()로 3층의 별 찍기
	for i in range(1,4):
		print('*' * i)
#문자를 반복시키도록 하는데, 1 부터 시작해야 별이 찍히므로 range(1,4)로 해야 한다.


## 
