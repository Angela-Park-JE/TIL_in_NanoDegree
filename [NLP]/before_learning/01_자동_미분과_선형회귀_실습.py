
# 자동 미분

import tensorflow as tf

# tape_gradient() 는 자동 미분 기능을 수행하는 함수이다.
# 임의로 2w^2 + 5 라는 식을 세워보고, w에 대해 미분해본다.

w = tf.Variable(2.)

def f(w):
	y = w**2
	z = 2*y +5
	return z

# gradients를 출력하면 w에 대해 미분한 값이 저장된 것을 확인할 수 있다.

with tf.GradientTape() as tape:
	z = f(w)

gradients = tape.gradient(z,[w])
print(gradients)

### 결과
# [<tf.Tensor: shape=(), dtype=float32, numpy=8.0>]

# --- #

# Implementation of linear regression using automatic differential

### 학습될 가중치 변수 선언
w = tf.Variable(4.0)
b = tf.Variable(1.0)

### 가설을 함수로서 정의
@tf.function
def hypothesis(x):
	return w*x + b

### 테스트 임의의 값을 넣고 출력
x_test = [3.5, 5, 5.5, 6]
print(hypothesis(x_test).numpy())

### 평균 제곱오차를 손실함수로 정의
@tf.function
def mse_loss(y_pred, y):
	return tf.reduce_mean(tf.square(y_pred-y))
	# 두 변수의 차이값을 제곱하여 평균을 취하는 함수

### 이때 x와 y가 약 10배 차이나는 데이터를 넣어본다.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 공부하는 시간
y = [11, 22, 33, 44, 53, 66, 77, 87, 95] # 각 공부하는 시간에 맵핑되는 성적

### 옵티마이저는 경사 하강법을 사용하되, 학습률은 0.01을 사용한다.

optimizer = tf.optimizers.SGD(0.01)

# 약 300번에 걸쳐 경사 하강법을 수행한다.

for i in range(301):
  with tf.GradientTape() as tape:
    # 현재 파라미터에 기반한 입력 x에 대한 예측값을 y_pred
    y_pred = hypothesis(x)

    # 평균 제곱 오차를 계산
    cost = mse_loss(y_pred, y)

  # 손실 함수에 대한 파라미터의 미분값 계산
  gradients = tape.gradient(cost, [w, b])

  # 파라미터 업데이트
  optimizer.apply_gradients(zip(gradients, [w, b]))

  if i % 10 == 0:
    print("epoch : {:3} | w의 값 : {:5.4f} | b의 값 : {:5.4} | cost : {:5.6f}".format(i, w.numpy(), b.numpy(), cost))

# 각각 횟수번째(-1)와 w의 값, b의 값, 비용 함수값을 print되도록 한다.
