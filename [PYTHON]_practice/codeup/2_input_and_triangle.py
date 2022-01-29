# 정수 세 개를 입력받아서 세 개의 숫자로 이루어진 삼각형을 만들어보자.
# 가장 큰 변의 길이가 나머지 두개의 합보다 같거나 크면 삼각형이 안된다.

n1 = int(input("첫 번째 수를 입력하세요"))
num_list.append(n1)
n2 = int(input("두 번째 수를 입력하세요"))
num_list.append(n2)
n3 = int(input("세 번째 수를 입력하세요"))
num_list.append(n3)
sorted(num_list)
if num_list[2] >= num_list[0]+num_list[1]:
    print("삼각형을 만들 수 없어요.")
else:
	print("삼각형을 만들 수 있어요.")


#--- 더 짧게 할 수 있는 방법

num_list = input("세 개의 수를 띄어쓰기로 입력하세요.").split()
sorted(num_list)
if int(num_list[2]) >= int(num_list[0])+int(num_list[1]):
    print("삼각형을 만들 수 없어요.")
else:
	print("삼각형을 만들 수 있어요.")

# 더 짧게 쓸 수는 있었지만 줄을 줄여놓고 정렬을 위해 int를 쓰려고 하기 어려웠다,
# 그래서 if 문에서 대소비교 할 때 int()를 씌웠다.
