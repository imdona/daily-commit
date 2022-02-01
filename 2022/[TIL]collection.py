'''
[python collections와 친해지기 review]

1. 제곱수 : 1부터 101사이에 있는 모든 제곱수를 하나의 리스트에 출력하기
    - 제곱수 : 1, 4, 9, 16,...,81, 100
'''
import re
from struct import unpack



result = []

for i in range(1, 101):
    # type(i**0.5) == int 이렇게 하면 float타입이라 풀 수 없음
    # 1로 나누어서 나머지가 0이다로 접근 가능
    if (i**0.5) % 1 == 0:
        result.append(i)

print(f"result: {result}")


'''
2. lambda
    1) 매개변수로 들어온 리스트 요소들의 제곱수를 가지고 있는 리스트를 반환하기
        (매개변수로 들어오는 리스트는 1이상의 자연수로만 구성)

        *예시*
            입력값:
                [1, 2, 3, 4, 5]
            출력값:
                [1, 4, 9, 16, 25]

    2) 매개변수로 들어온 리스트 요소들이 홀수인지 짝수인지 리스트를 통해 반환하기
        (매개변수로 들어오는 리스트는 1이상의 자연수로만 구성)

        *예시*
            입력값:
                [1, 4, 9, 16, 25]
            출력값:
                ['홀수', '짝수', '홀수', '짝수', '홀수']
'''
## lambda 사용하지 않고 풀기(1)
def square_num(list):
    return [x**x for x in list]

# test code
# print(square_num([2, 4, 6, 8, 10, 12]))

## lambda 사용하지 않고 풀기(2)
def odd_or_even(list):
    result = []
    for i in list:
        if (i % 2) == 0:
            result.append('짝수')
        else:
            result.append('홀수')
    return result

# test code
print(odd_or_even([1, 4, 9, 16, 25]))
print(odd_or_even([2, 3, 6, 7, 10, 12]))

# --------------------------------------------------------------
## lambda를 사용해서 풀기(1)
# type hinting을 위한 import
# from typing import List

# def is_square_num(list: List[int]) -> List:
#     return list(map(lambda x : x**2, list))

# # test code
# # print(is_square_num([2, 4, 6, 8, 10, 12]))

# ## lambda를 사용해서 풀기(2)
# def odd_or_even(a: List[int]) -> List:
#     return list(map(lambda x: '짝수' if (x%2) == 0 else '홀수', list))

# # test code
# print(odd_or_even([1, 4, 9, 16, 25]))
# print(odd_or_even([2, 3, 6, 7, 10, 12]))

'''
3. 문자열 정렬 : 문자를 입력받아 알파벳순서대로(A~Z, a~z) 정렬하기
    (아스키코드의 십진법을 기준, 중복되는 문자열은 처리, 영어 소문자와 대문자에 대해서만 정렬)
'''
def sort_alpha(string):
    # set : 중복제거, split() : string타입 문자 나눠서 리스트로 저장
    result = list(set(string.split()))
    result.sort()
    # 리스트에 " "를 추가
    return " ".join(result)

# sorted로 더 간단하게
def sort_alpha(string):
    return " ".join(sorted(list(set(string.split()))))

# unpacking 사용해보기 : return으로 하니까 error가 남 (can't use starred expression here)
def unpacking(string):
    result = sorted(list(set(string.split())))
    print(*result)
    # return *result

# test code
print(sort_alpha('a T C'))
print(sort_alpha('z X y D c A b U'))
unpacking('a T C')
# print(unpacking('a T C')) # can't use starred expression here


'''
4. 문자열 정렬(2) : sort_alpha + 대문자 소문자 바꾸기
'''
## 메소드 학습
# 소문자인지 확인하는 함수
print("islower: ", "a".islower())  # True
# 대문자인지 확인하는 함수
print("isupper: ", "a".isupper())  # False
# 소문자 -> 대문자로 바꾸는 함수
a = "a"
print("upper: ", a.upper())  # A
# 대문자 -> 소문자로 바꾸는 함수
A = "A"
print("lower: ", A.lower())  # a
# swapcase
string = "i AM dONA!"
print("swapcase: ", string.swapcase())  #I am Dona!


# 문제 풀이
def sort_alpha_2(string):
    origin = sorted(list(set(string.split())))
    result = []
    for i in origin:
        if i.isupper():
            result.append(i.lower())
        else:
            result.append(i.upper())

    return " ".join(result)

# 짧게 시도
def sort_alpha_2(string):
    return " ".join([i.lower() if i.isupper() else i.upper() for i in sorted(list(set(string.split())))])

# 다른 메소드 사용해보기: swapcase()
def sort_alpha_2(string):
    return " ".join((sorted(set(string.split(' '))))).swapcase()

# test code
print(sort_alpha_2('c t A'))
print(sort_alpha_2('z X y W v U t S'))
