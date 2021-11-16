# 숫자 두 개를 입력 받아서, 두 수의 공약수를 찾아보자.
# 내가 한 것

input1 = int(input("첫 번째 수를 입력하세요."))
input2 = int(input("두 번째 수를 입력하세요."))
num_list1 = range(1, input1+1)
num_list2 = range(1, input2+1)
d_list1 = []
d_list2 = []
sorted(num_list1)
sorted(num_list2)
for n1 in num_list1:
	d1=input1%n1
	if d1 == 0:
	    d_list1.append(n1)
for n2 in num_list2:
	d2=input2%n2
	if d2 == 0:
	    d_list2.append(n2)

cd_list = []
for n in range(len(d_list1))
    if d_list1[n] == d_list2[n]:
    	cd_list.append(d_list1[n])
print(cd_list)





