
### 4 finding methods.
# https://ponyozzang.tistory.com/279

### match(pattern, string)
# 문자열의 시작 부분부터 패턴과 매칭이 되는지 검색하는 함수
pattern = r"ca"
text = "caabsacasca"
matchOB = re.match(pattern , text)
if matchOB:
	print matchOB.group() # 'ca'



### search(pattern, string)
# 문자열에 패턴과 매칭 되는 부분이 있는지 검색하는 함수.
# 시작 부분이 아니더라도 데려옴.
pattern = r"ca"
text = "caabsacasca"
matchOB = re.search(pattern , text)

if matchOB:
	print matchOB
	print matchOB.group() # 매칭된 문자열 # ca
	print matchOB.start() # 매칭된 문자열 시작 위치 # 0
	print matchOB.end()   # 매칭된 문자열 종료 위치 # 2
	print matchOB.span()  # 매칭된 문자열 시작,종료 위치 # (0, 2)

  
  
### findall(pattern, string)
# 문자열에 패턴과 매칭 되는 부분을 리스트로 전부 반환.
# list 형태로 반환되기 때문에 group()같은 함수를 쓸 수 없다.
pattern = r"ca"
text = "caabsacasca"
# 매칭된 값은 리스트로 모두 반환
matchedList = re.findall(pattern,text)
if matchedList:
	print matchedList # ['ca', 'ca']

  

### finditer(pattern, string)
# 문자열에 패턴과 매칭 되는 부분을 이터레이터로 반환.
# findall 은 리스트를 반환하지만 finditer는 오브젝트 형태로 된 이터레이터를 반환하기 때문에 
# for 문 내에서 group()같은 정보 추출 함수 등을 사용할 수 있다.
pattern = r"ca"
text = "caabsacasca"
# 매칭된 값은 이터레이터로 모두 반환
iterator = re.finditer(pattern ,text)
for match in iterator:
	print match.group() # 1回目: ca 2回目: ca
	print match.start() # 1回目: 0 2回目: 6
	print match.end() # 1回目: 2 2回目: 8
	print match.span() # 1回目: (0, 2) 2回目: (6, 8)
