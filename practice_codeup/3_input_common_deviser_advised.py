input1 = int(input("첫 번째 수를 입력하세요."))
input2 = int(input("두 번째 수를 입력하세요."))
d_list1 = []
d_list2 = []
for n1 in range(1, input1+1):
	if input1%n1 == 0:
	    d_list1.append(n1)
for n2 in range(1, input2+1):
	if input2%n2 == 0:
	    d_list2.append(n2)

cd_list = []
for cd1 in d_list1:
    for n in d_list2:
	    if cd1 == n:
	        cd_list.append(cd1)
print(cd_list)
		
