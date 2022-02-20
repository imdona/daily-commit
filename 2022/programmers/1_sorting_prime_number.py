'''
프로그래머스 완전탐색 [소수 찾기]
문제 : https://programmers.co.kr/learn/courses/30/lessons/42839

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

[제한사항]
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
'''
# case 1 : 최초 풀이
from itertools import permutations

def solution(numbers):
    num_li = list(numbers)  # 리스트로 만들어주기(하나씩 잘림)
    per = []  # 숫자 순열을 담을 리스트
    per_int = []  # str 붙이고 int로 변환한 리스트
    answer = []  # 정답 리스트

    for i in range(len(numbers)+1):
        per += list(permutations(numbers, i))
        # [[],["1"],["7"],["1","7"],["7","1"]]

    # int로 바꿔주는 함수 정의
    def change_int(li):
        if len(li) == 0: return 0  # 길이 0인 원소 처리
        stick = "".join(li)  # 문자열 원소인 리스트 붙이기
        return int(stick)  # 정수로 변환

    for j in per:
        per_int.append(change_int(j))
        # per_int : [0,1,7,17,71]

    # 소수 확인하는 함수 정의
    def check_prime(num):
        if num == 1 or num == 0:
            return False
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

    for k in per_int:
        if check_prime(k) == True:
            answer.append(k)

    return len(set(answer))


# --------------------------------------------------------------------
# case 1  : 정리
from itertools import permutations

def solution(numbers):
    num_li = list(numbers)  # 리스트로 만들어주기(하나씩 잘림)
    per = []  # 숫자 순열을 담을 리스트
    answer = []  # 정답 리스트

    for i in range(len(numbers)+1):
        per += list(permutations(numbers, i))

    # str 붙이고 int로 변환한 리스트
    per_int = [int(("").join(p)) for p in per]

    # 소수 확인하는 함수 정의
    def check_prime(num):
        if num == 1 or num == 0:
            return False
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

    for k in per_int:
        if check_prime(k) == True:
            answer.append(k)

    return len(set(answer))

# --------------------------------------------------------------------
# case 2 : programmers 1위 풀이 set를 활용함
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        # 조합들 set에 합치기(| : set 합집합)
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
        # print(f"a: {a}")  # {1, 7} -> {1, 71, 17, 7}
    # - : set 차집합 : 0, 1 은 소수가 아니므로 뺀다
    a -= set(range(0, 2))
    # print(f"set(range(0, 2)) : {set(range(0, 2))}")  # {0, 1}
    # print(f"a 차집합 : {a}")  # a 차집합 : {71, 17, 7}

    # 소수 찾기 : 에라토스테네스의 체
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
        # print(a)
    return len(a)

print(solution("17"))
print(solution("011"))