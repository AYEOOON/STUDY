# while 반복문에 continue와 break 사용하기

count = 0

while count < 10:
    count +=1
    if count < 4:     # 1,2,3 은 4보다 작기 때문에 다시 첫줄로 돌아감
        continue
    print('횟수:', count)
    if count == 8:            # 8이 되야 끝남
        break


