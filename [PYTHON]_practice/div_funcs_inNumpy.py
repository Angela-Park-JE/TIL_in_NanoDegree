### linespace
# 첫 번째 값부터 두 번째 값을 세 번쨰 값 개수로 나누겠다는 넘파이 함수이다.
# np.linespace

>>> np.linespace(1,3,3)

array([1., 2., 3.])

>>> np.linspace(4,6,3)

array([4., 5., 6.])


### meshgrid
# 격자를 만드는 것. x축과 y축의 격자를 만든 것이라고 생각 하면 됨.
# np.meshgrid

>>> a = np.meshgrid([1,2,3] ,[4,5,6])
>>> a

[array([[1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]]), array([[4, 4, 4],
        [5, 5, 5],
        [6, 6, 6]])]
