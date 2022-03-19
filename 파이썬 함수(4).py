#positinal argument는 입력된 값의 위치에 따라 출력되는 값이 다름

def f(x,y):
  return x-y
f(4,1)
f(1,4)      #안의 숫자의 위치에 따라 나오는 값이 달라짐

#keyword argument는 직접 변수에 대합하는 형식을 사용함

def f(x,y):
  return x-y
f(x=4,y=1)    

f(3,y=1)     #keyword argument 뒤에 positinal는 쓸 수 없음


#positinal argument만 사용하도록 하려면 뒤에 /를 붙이면 됨
def f(x,y,/):
  return x-y
f(4,5)

#keyword argument만 사용하도록 하려면 앞에 *를 붙이면 됨
def f(*,x,y):
  return x-y
f(x=4,y=5)

#두 가지를 혼용해서 쓸 때는 f(포지셔널,/,두가지다써도됨,*,키워드)defㅇ
def f(a,b,/,h,i,*,x,y):
  print(a-b)
  print(h-i)
  print(x-y)
  
f(a=1,b=2,h=1,i=1,x=6,y=7)


