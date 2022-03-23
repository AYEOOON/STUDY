# for문으로 홀수 찾는 방법

numbers=[1,2,3,4,5,6,7,8,9,10]
odd_numbers=[]

for number in numbers:
  if number%2==1:
    odd_numbers.append(number)
print(odd_numbers)


#comprehension 사용해서 홀수 찾기

[num for number in numbers if number%2==1]

