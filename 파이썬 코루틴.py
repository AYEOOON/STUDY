# 하위 코루틴의 반환 값 가져오기
# 다음 코드는 코루틴에서 숫자를 누적한 뒤 합계를 yield from으로 가져옴


def accumulate():
  total = 0
  while True:
    x = (yield)            # 코루틴 바깥에서 값을 받아옴
    if x is None:          # 받아온 값이 None 이면
      return total         # 합계 total을 반환
    total += x
    
def sum_coroutine():
  while True:
    total = yield from accumulate()   # accumulate의 반환값을 가져옴
    print(total)
    
co = sum_coroutime()
next(co)

for i in range(1,11):      # 1부터 10까지 반복
  co.send(i)               # 코루틴 accumulate에 숫자를 보냄
co.send(None)              # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

for i in range(1,101):    # 1부터 100까지 반복
  co.send(i)              # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄
