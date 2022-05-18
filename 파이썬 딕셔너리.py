# for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당됩니다.
# 순서는 임의적이다.같은 순서를 보장할 수 없다.

>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> for key in a:
...     print(key)
... 
alice
bob
tony
suzy


# value값으로 for문을 반복하기 위해서는 values() 를 사용해야합니다.

>>> for val in a.values():
...     print(val)
... 
[1, 2, 3]
20
15
30    


# key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용합니다.

>>> for key, val in a.items():
...     print("key = {key}, value={value}".format(key=key,value=val))
... 
key = alice, value=[1, 2, 3]
key = bob, value=20
key = tony, value=15
key = suzy, value=30
