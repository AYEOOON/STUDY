#함수의 반환

def han(maegae):
  a=10
  b=a+maegae
  return b

print(han(4))


#사용자에게서 정수를 입력받아 반환해주는 함수

def han():
  print('정수를 입력하세요.')
  n=input()
  n=int(n)
  return n

a=han()
b=han()
c=a+b
print(c)
