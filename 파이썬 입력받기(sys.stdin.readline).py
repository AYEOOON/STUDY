# 한 개의 정수를 입력받을 때

import sys
a = int(sys.stdin.readline())    #변수 타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 한다.


# 정해진 개수의 정수를 한줄에 입력받을 때

import sys
a,b,c = map(int,sys.stdin.readline().split())   # map()은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수이다.


# 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때

import sys
data = list(map(int,sys.stdin.readline().split()))


# 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때

import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))   #각 요소의 길이가 동일한 2차원 리스트도 만들 수 있고, 각각 길이가 다른 2차원 리스트도 입력 받을 수 있다.
