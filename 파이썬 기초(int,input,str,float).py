#두 개의 실수를 입력받아 그 합을 출력하는 프로그램

print('enter your name:')
name=input()
print(name)

print('enter:num1')
num1=input()                          #input()은 입력을 무조건 문자열로 받는다.
num1=float(num1)                      #int()함수는 input()을 쓸때 무조건 쓰는것이 아니라 정수형으로 바꾸고자 할때.
print('enter:num2')

num2=input()
num2=float(num2)
num3=num1+num2

print('두 수의 합은 '+str(num3))           #print()에서 여러개의 값을 같이 출력하고자 + 기호를 사용할때는 자료형을 맞춰야함
