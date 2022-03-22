# 💫 Time Series analytics
시계열 분석 !!! I wanna be maewoo maewoo good at this 😚

공부하는 이유 (1) 이상치 분석에 관심이 많아서 (2) 예측 모델 공부 

## 1. 시계열 분석 
- 시계열 데이터 특징
- 시계열 분석의 절차

- AR(Auto Regression): 자기상관모형
- MA(Moving Average): 이동평균모형

- ARIMA (Auto-regressive Integrated Moving Average) : 자기회귀누적이동평균모형
- SARIMA (Seasonal Auto-regressive Integrated Moving Average)


## 2. 머신러닝과 시계열분석
- 딥러닝의 개념: 신경망 구조
- 머신러닝 
  - 지도 VS 비지도
  - 결정론적(ex. Regression) VS 생성론적 (Bayesian inference)
- RNN
  - 입력 시퀀스 종류에 따른 RNN의 종류
  - RNN의 variation
  - 시계열분석에서의 RNN의 한계: 과거 데이터의 출력이 현재를 설명할 수 있어야 RNN을 쓸 수 있다.
  - 실습예시: LSTM
  - DRNN
- CNN
  - 이미지 분석에서의 CNN
  - 시계열분석은 1D CNN


## 3. Seq2Seq
- CNN-LSTM 결합 모델
- Seq2Seq 의 구조
- RNN-RNN 결합모델
- 예시: AWS의 DeepAR+

- 시계열분석의 한계점과 using alternative data


## 4. AutoEncoder & GAN
- ARIMA가 여전히 많이 쓰이는 이유와 시계열분석이 딥러닝 모델을 단순히 쓸 수 없는 이유
- AutoEncoder
  - 인풋과 같은 아웃풋을 만들 수 있는 벡터값 생성
- GAN (Generative Adversarial Network)
  - Tad-GAN
- (추가로 언급하신 것) XAI : 해석 가능한 AI를 위해 연구중인 분야
