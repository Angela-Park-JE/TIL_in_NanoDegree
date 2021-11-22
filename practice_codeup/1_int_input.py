# 1부터 입력받은 숫자 까지 3의 배수만 제외하고 출력하는 코드

num = int(input("숫자를 입력하세요"))
num_list = list(range(num+1))
for i in num_list:
    if i % 3 != 0:
    	print(i, end=" ")

#print는 강제적으로 /이 들어가기 때문에 end="사이에_넣을것" 하면 띄어쓰기 출력이 가능하다.
