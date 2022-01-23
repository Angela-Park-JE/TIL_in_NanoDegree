### 기본 용어
# corpus: 말뭉치. 특정한 목적을 가지고 수집한 텍스트 데이터
# token: 의미를 가진 가장 작은 단위
# tokenization: 토큰 단위로 나누는 것
# vocabulary: corpus에 있는 모든 문서, 문장을 토큰화 하고 중복을 제거한 토큰의 집합

### 벡터화
# 자연어를 컴퓨터가 이해할 수 있도록 벡터로 만들어 주는 것을 뜻함
### 벡터화 하는 방법 두 가지
# Count-based representation: 등장 횟수 기반의 단어 표현. 
# Bag-of-words, TI-IDF
# Distributed representation: 분포 기반의 단어 표현. 타깃 단어 주변의 단어를 벡터화 하는 방법
# Word2Vec, GloVe, FastText

### Text Poreprocessing
# 1. 차원이 늘어날 수록 설명력이 떨어진다. 
# 2. 대, 소 문자 통일
# 3. 정규표현식 사용
# 4. 예시: SpaCy library 사용하여 토큰화

# 자연어 처리를 위한 모듈과 모델 로드
import spacy
from spacy.tokenizer import Tokenizer
nlp = spacy.load("en_core_web_sm")
tokenizer = Tokenizer(nlp.vocab)

# 토큰화를 위한 파이프라인 구성
tokens = []
for doc in tokenizer.pipe(df['reviews.text']):
	doc_tokens = [re.sub(r"[^a-z0-9]", "", token.text.lower()) for token in doc]
	tokens.append(doc_tokens)

# 토큰화 한 리스트를 데이터프레임에 넣고 로드
df['tokens'] = tokens
df['tokens'].head()

# 결과
>>>
0    [though, i, have, got, it, for, cheap, price, ...
1    [i, purchased, the, 7, for, my, son, when, he,...
2    [great, price, and, great, batteries, i, will,...
3    [great, tablet, for, kids, my, boys, love, the...
4    [they, lasted, really, little, some, of, them,...
Name: tokens, dtype: object

      
# 5. 불용어(stop_words)처리
# 별다른 의미를 갖지 않지만 자주 등장하는 단어들이 있을 수 있다. 이들을 묶어서 불용어로 넣어준다.
# SpaCy의 기본 제공 불용어 알아보기
print(nlp.Defaults.stop_words)

# 불용어를 제외하고 토큰화 하기
