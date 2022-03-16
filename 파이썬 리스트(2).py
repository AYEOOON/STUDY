a=[10,20,30,40,50]
i=0
while i<len(a):           #리스트 안의 값들이 세로로 나열됨
  print(a[i])          
  i=i+1
  
b#리스트 안의 값들의 전체 합 구하기

s=0
i=0
while i<len(a):     #len은 리스트의 길이를 알려주는 것
  s=s+a[i]        
  i=i+1
print(s)


#1부터 10까지의 합 구하기

s=0 #1.2.3.4를 한번에 담을 변수
i=1
while i<10:
  s=s+i
  i=i+1
print(s)
