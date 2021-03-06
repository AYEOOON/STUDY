# for문을 이용해서 비어있는 2차원 리스트를 만들어 보자.

a = []

for i in range(3):
    line = []
    for j in range(2):
        line.append(0)   # 값이 들어 있는 리스트가 아니라 값이 비어있는 리스트가 생성되었다.  append를 통해 값을 추가하고
    a.append(line)       # 1차원 for문의 append를 통해 값을 담은 리스트를 추가해서 만드는 방식이다.
print(a)
>>>[[0,0],[0,0],[0,0]]   # a의 입장에서는 [리스트, 리스트, 리스트] 이기 때문이다.

 
# 리스트 표현식으로 2차원 리스트 만들기

a = [[0 for j in range(2)] for i in range(3)]
>>>[[0,0],[0,0],[0,0]]

 
# 위의 리스트가 길게 느껴진다면 한 줄로도 설명이 가능하다. 이제 이는 파이썬에 능숙해졌다면 사용할 수 있는 기술이다.
# 이제 이를 응용한다면.

a = [[0]* i for i in [3, 1, 3, 2, 5]]      # 가로의 길이(열)을 알고 있다는 가정에 한에서 그에 맞게 행의 열이 결정되는 리스트다.
>>>[[0,0,0,] , [0], [0,0,0], [0,0], [0,0,0,0,0]]

# 이처럼 파이썬을 응용할 수 있다면 코딩의 줄 길이가 점차 짧아짐을 느낄 수가 있다.

 

 # 이차원 리스트를 복사하기

a = [[10, 20], [30, 40]]
import copy            # 그냥 copy를 사용 할 경우 앞서 배운 것 처럼 a의 리스트를 copy를 할 수 있다.
b = copy.deepcopy(a)   #그러나 a값 안에 또 다른 리스트는 copy 대상에 되지 않고. 만약 하지 않을 경우, b의 값을 변경해도 a의 값이 변경되는 상황이 발생한다.

# 그래서 1차원이 아닌, 다중 배열을 사용하게 될 경우에는 copy.deepcopy를 사용해야한다.



