# 클래스를 작성하기 위해서는 class 키워드 사용하여 새로운 클래스를 작성합니다.
# Python의 대부분 네이밍컨벤션이 단어와 단어사이에 _ 를 넣는 다면 클래스의 네이밍컨벤션은 CamelCase 를 사용합니다.

class CustomClass:
    def __init__(self, param):
        .......

# 클래스 생성 연습
# 클래스 생성은 아래와 같이 class 키워드 및 클래스의 이름을 입력하여 생성.

class Flight:
    pass

# 생성한 클래스는 REPL에서 아래와 같이 import할 수 있습니다.

>>> from airtravel import Flight
>>> Flight
<class 'airtravel.Flight'>

# 클래스 객체 생성 및 변수에 할당
# 새로운 객체를 생성하기, java나 C# 등의 다른 언어와 다르게 new 키워드가 없다.

>>> f = Flight()
>>> type(f)
<class 'airtravel.Flight'>


# 클래스 메소드 작성
# 메소드란 클래스 내의 함수
# 메소드 작성하기

class Flight:
    def number(self):
        return 'SN060'

# 인스턴스 메소드의 접근
# 인스턴스 메소드란 객체에서 호출되어질수 있는 함수
# 인스턴스의 메소드 사용

>>> from airtravel import Flight
>>> f = Flight()
>>> f.number()
'SN060'

# 파이썬 메서드의 첫번째 파라미터명은 관례적으로 self라는 이름을 사용합니다.
# 호출 시 호출한 객체 자신이 전달되기 때문에 self라는 이름을 사용하게 된 것
# 이를 이용하여 클래스에서 바로 메소드로 접근하면서 위에서 할당한 Flight의 객체 f를 파라미터로 전달함으로써 똑같은 결과값 얻습니다.
# 클래스의 내부에 self 파라미터가 포함되는데 이를 이용한 접근법

>>> Flight.number(f) # f는 Flight객체
'SN060'
