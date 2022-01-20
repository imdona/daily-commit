
# import 모듈명
'''import 모듈명 을 사용할 때, 모듈명.변수, 모듈명.함수(), 모듈명.클래스() 형태로 불러와서 사용가능'''
import my_function

print(my_function.my_divide())

# import 모듈명 as 별명
import my_function as mf

print(mf.my_divide())

# from 모듈명 import 함수명
'''해당 방식의 형태로 변수, 함수, 클래스 를 불러오면 모듈명. 없이 바로 변수/함수/클래스를 사용가능'''
from my_function import my_divide

print(my_divide())

# 불러온 변수/함수/클래스 명도 별명을 붙여서 사용할 수 있다.
from my_function import my_divide as md

print(md())

# 모듈 내의 모든 변수, 함수, 클래스를 사용하고자 할 때는 from 모듈명 import * 를 사용한다.
from my_function import *

print(my_divide())
print('writer:', writer)