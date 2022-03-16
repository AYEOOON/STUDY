#리스트에 값 추가하기(append())

a=[]
print(a)
a.append(879)
print(a)
a.append('hello')
print(a)


#리스트에 다섯개의 값을 입력받아 저장하기

a=[]
i=0
while i<5:
  n=input()
  n=int(n)
  a.append(n)
  i=i+1
print(a)


#1부터100까지 숫자를 랜덤으로 출력하여 리스트에 나열

import random
a=[]
i=0
while i<5:
  n=random.randint(1,100)
  a.append(n)
  i=i+1
print(a)

