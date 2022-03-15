def han():
  print('hello')
  i=0
  while i<5:
    print('*',end='')    #end=는 줄바꿈이 일어나지 않게 하는 것이다.
    i=i+1
han()                    #함수를 호출하는 것
print('중간고사는 5주 뒤')
han()
han()



#매개변수가 있는 경우

def han(maegae):
  print('hello')
  i=0
  while i<maegae:
    print('*',end='')  
    i=i+1
  print()
  
han(5)                    
print('중간고사는 5주 뒤')
han(1)
han(17)
