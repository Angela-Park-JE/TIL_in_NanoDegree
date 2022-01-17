# 라이브러리호출
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers



# 독립변수 데이터를 x, 숫자 10 이상인 경우 1, 미만인 경우 0을 부여한 레이블 데이터를 y라고 가정했을 때
x = np.array([-50, -40, -30, -20, -10, -5, 0, 5, 10, 20, 30, 40, 50])
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# 1개의 실수 x로부터, 1개의 실수 y를 예측하는 맵핑 관계의 데이터이다. 
# 시그모이드 함수를 사용할 것이므로 activation의 인자값을 sigmoid로 적는다.
# 1개의 실수 x로부터, 1개의 실수 y를 예측하는 맵핑 관계 - Denxe의 output_dim = 1 , imput_dim = 1

model = Sequential()
model.add(Dense(1, input_dim = 1, activation='sigmoid')) 

sgd = optimizers.SGD(lr=0.01)
model.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['binary_accuracy'])

model.fit(x, y, epochs=200) # 200회 수행

# 실제값과 오차를 최소화하도록 값이 변경된 w 와 b 의 값을 가진 모델을 시각화
plt.plot(x, model.predict(x), 'b', x, y, 'k.')



#--#
# test 데이터
print(model.predict([1, 2, 3, 4, 4.5]))
print(model.predict([11, 21, 31, 41, 500]))

# 실제 출력값
# [[0.4780311]
#  [0.5370409]
#  [0.595031 ]
#  [0.6504848]
#  [0.6768547]]
# [[0.9068482 ]
#  [0.99042916]
#  [0.9990918 ]
#  [0.99991447]
#  [1.        ]]
