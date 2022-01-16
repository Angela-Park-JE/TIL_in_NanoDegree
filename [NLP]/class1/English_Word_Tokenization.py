# 단어 토큰화(Word Tokenization): 단어 단위로 토큰화를 수행하는 것
# NLTK: 영어로 토큰화 할 때 일반적으로 사용하는 모델, 영어 자연어 처리를 위한 패키지
# 어떤 토크나이저를 사용할 지 정답은 없다.



# NLTK의 토크나이저 1. word_tokenize
import nltk
nltk.download('punkt')

sentence = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."

# 아포스트로피가 들어간 상황에서의 토큰화
from nltk.tokenize import word_tokenize  
print(word_tokenize(sentence))

# Don't를 Do와 n't로 분리하였으며, Jone's는 Jone과 's로 분리



# NLTK의 토크나이저 2. WordPunctTokenizer
from nltk.tokenize import WordPunctTokenizer  
print(WordPunctTokenizer().tokenize(sentence))

# Don't를 Don과 '와 t로 분리하였으며, Jone's를 Jone과 '와 s로 분리



# NLTK의 토크나이저 3. TreebankWordTokenizer
# Penn Treebank Tokenizer의 규칙
# 규칙 1. 하이픈으로 구성된 단어는 하나로 유지한다.
# 규칙 2. doesn't와 같이 아포스트로피로 '접어'가 함께하는 단어는 분리해준다.
from nltk.tokenize import TreebankWordTokenizer
tokenizer=TreebankWordTokenizer()
text = "Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."
print(tokenizer.tokenize(text))

