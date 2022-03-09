#나이가 20살 이상이면 영화관람 가능합니다. 출력
#15살이 아니면 영화관람 불가
#15살 이상이면 부모님이랑 있으면 관람가능


print('나이를 입력하세요.')

age=input()
age=int(age)

if age>=20:
    print('영화관람 가능합니다.')
else:
    if age>=15:
        print('부모님과 함께 관람 가능합니다.')
    else:
        print('영화관람이 불가능합니다.')
print('Thank you')
