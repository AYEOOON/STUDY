# python REPL을 실행 후 아래의 코드를 실행합니다.
# math는 수학 연산 기본 라이브러리이며, sqrt는 제곱근을 구합니다.

import math
math.sqrt(81)

# REPL상태에서 help메소드를 사용하면 import한 라이브러리의 document를 볼 수 있습니다.

help(math)

# factorial메소드를 실행해봅니다.

math.factorial(5)

# 아래와 같이 factorial 메소드만 import해서 사용할 수 있습니다.

from math import factorial
factorial(5)


# 메소드를 import할 때 별칭을 줄 수 있습니다.

from math import factorial as fac
fac(5)
