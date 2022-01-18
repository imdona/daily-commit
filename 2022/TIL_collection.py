'''
[python collections와 친해지기 review]
part1 : 제곱수
'1부터 101 사이에 있는 모든 제곱수'를 하나의 리스트에 출력하는 코드를 작성해주세요.
    제곱수 : 1, 4, 9, 16,...,81, 100
    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    입력값:
        없음
    출력값:
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
import re
from struct import unpack


def part1():
    result = []

    for i in range(1, 101):
        # type(i**0.5) == int 이렇게 하면 float타입이라 풀 수 없음
        # 1로 나누어서 나머지가 0이다로 접근 가능
        if (i**0.5) % 1 == 0:
            result.append(i)

    return result

'''
part2 : lambda
람다라는 개념이 기본적으로 어떤 상황에서 활용되고 효율적인지 생각하면서 풀기
    문제 1.
        매개변수로 들어온 리스트 요소들의 제곱수를 가지고 있는 리스트를 반환해주세요.
        단 매개변수로 들어오는 리스트는 1이상의 자연수로만 구성되어있습니다.
        람다키워드를 함수 내부에서 사용해야 합니다.

        *예시 1*
            입력값:
                [1, 2, 3, 4, 5]
            출력값:
                [1, 4, 9, 16, 25]

        *예시 2*
            입력값:
                [2, 4, 6, 8, 10, 12]
            출력값:
                [4, 16, 36, 64, 100, 144]

    문제 2.
        매개변수로 들어온 리스트 요소들이 홀수인지 짝수인지 리스트를 통해 반환해주세요.
        (반환되는 리스트 내부에는 '홀수', '짝수'만 있어야합니다.)
        단 매개변수로 들어오는 리스트는 1이상의 자연수로만 구성되어있습니다.
        람다키워드를 함수 내부에서 사용해야 합니다.

        *예시 1*
            입력값:
                [1, 4, 9, 16, 25]
            출력값:
                ['홀수', '짝수', '홀수', '짝수', '홀수']

        *예시 2*
            입력값:
                [2, 3, 6, 7, 10, 12]
            출력값:
                ['짝수', '홀수', '짝수', '홀수', '짝수', '짝수']
'''
## lambda 사용하지 않고 풀기(1)
def part2_is_square_num(list):
    return [x**x for x in list]

# test code
# print(part2_is_square_num([2, 4, 6, 8, 10, 12]))

## lambda 사용하지 않고 풀기(2)
def part2_is_odd_num(list):
    result = []
    for i in list:
        if (i % 2) == 0:
            result.append('짝수')
        else:
            result.append('홀수')
    return result

# test code
print(part2_is_odd_num([1, 4, 9, 16, 25]))
print(part2_is_odd_num([2, 3, 6, 7, 10, 12]))

## lambda를 사용해서 풀기(1)
# type hinting을 위한 import
# from typing import List

# def part2_is_square_num(list: List[int]) -> List:
#     return list(map(lambda x : x**2, list))

# # test code
# # print(part2_is_square_num([2, 4, 6, 8, 10, 12]))

# ## lambda를 사용해서 풀기(2)
# def part2_is_odd_num(a: List[int]) -> List:
#     return list(map(lambda x: '짝수' if (x%2) == 0 else '홀수', list))

# # test code
# print(part2_is_odd_num([1, 4, 9, 16, 25]))
# print(part2_is_odd_num([2, 3, 6, 7, 10, 12]))

'''
part3 : 컬렉션 자료형의 기본특징과 내장함수를 이해하고 활용하기
    자유롭게 문자를 입력받아 알파벳순서대로(A~Z, a~z) 정렬하세요.
    문자를 정렬하기 위한 값의 비교는 아스키코드의 십진법을 기준으로 합니다.
    중복되는 문자열을 처리해줄 수 있도록 기능을 구현해주세요.
    영어 소문자와 대문자에 대해서만 정렬을 진행하도록 합니다.

    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    *예시 1*
        입력값:
            'a T C'
        출력값:
            'C T a'

    *예시 2*
        입력값:
            'z X y D c A b U'
        출력값:
            'A D U X b c y z'
'''
def part3(string):
    # set : 중복제거, split() : string타입 문자 나눠서 리스트로 저장
    result = list(set(string.split()))
    result.sort()
    # 리스트에 " "를 추가
    return " ".join(result)

# sorted로 더 간단하게
def part3(string):
    return " ".join(sorted(list(set(string.split()))))

# unpacking 사용해보기 : return으로 하니까 error가 남 (can't use starred expression here)
def unpacking(string):
    result = sorted(list(set(string.split())))
    print(*result)
    # return *result

# test code
print(part3('a T C'))
print(part3('z X y D c A b U'))
unpacking('a T C')
# print(unpacking('a T C')) # can't use starred expression here


'''
part4 : part3 + 대문자 소문자 바꾸기
    *예시 1*
        입력값:
            'c t A'
        출력값:
            'a C T'

    *예시 2*
        입력값:
            'z X y W v U t S'
        출력값:
            's u w x T V Y Z'
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
def part4(string):
    origin = sorted(list(set(string.split())))
    result = []
    for i in origin:
        if i.isupper():
            result.append(i.lower())
        else:
            result.append(i.upper())

    return " ".join(result)

# 짧게 시도
def part4(string):
    return " ".join([i.lower() if i.isupper() else i.upper() for i in sorted(list(set(string.split())))])

# 다른 메소드 사용해보기: swapcase()
def part4(string):
    return " ".join((sorted(set(string.split(' '))))).swapcase()

# test code
print(part4('c t A'))
print(part4('z X y W v U t S'))

