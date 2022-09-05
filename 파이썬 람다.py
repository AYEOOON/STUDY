# 람다(lambda)는 함수를 간단하게 사용 가능하게 해준다. 람다는 이름이 없는 함수, 익명함수라고 하기도 한다.
# 매개변수 두개를 받아 두 수의 합을 리턴하는 간단한 함수를 작성하는데 아래와 같이 사용 가능하다.
# 람다함수는 map, filter, reduce 처럼 매개변수로 함수가 필요한곳에 유용하게 쓰입니다.


# 함수를 이용한 코드

def add(n,m):
  return n+m
print(add(2,3))

print((lambda n,m:n+m)(2,3))

# 람다를 변수에 할당하여 재사용할 수도 있다.

lambdaAdd = lambda n,m:n+m
print(lambdaAdd(2,3))

print(lambdaAdd(4,5))

# 람다식 안에서 조건도 사용 가능하다.

print((lambda n,m: n if n%2==0 else m)(1,3))

print((lambda n,m: n if n%2==0 else m)(2,3))


# 람다함수는 map, filter, reduce 처럼 매개변수로 함수가 필요한곳에 유용하게 쓰인다.
# map, filter, reduce 를 람다함수를 이용하여 작성하면...

l = list(range(1,11))
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
m = list(map(lambda n:n*n, l))
print(m)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 
f = list(filter(lambda n:n%2==0, l))
print(f)
# [2, 4, 6, 8, 10]
 
r = reduce(lambda n,m:n*m, l)
print(r)
# 3628800
