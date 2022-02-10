'''
백준 10815 [숫자카드] - 정렬 & 이분탐색
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.
셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다.
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

[출력]
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.
'''
# case 1 : 시간 초과 -> 이분탐색으로 풀어서 극복해보자
import sys
N = int(sys.stdin.readline())  # 숫자카드의 개수
origin_cards = list(map(int, sys.stdin.readline().split()))  # 숫자 카드에 적혀있는 정수 리스트
M = int(sys.stdin.readline())  # 확인해야할 정수의 개수
check_cards = list(map(int, sys.stdin.readline().split()))  # 확인해야할 카드에 적혀있는 정수 리스트
# check
# print(origin_cards)
# print(check_cards)

result = []
for card in check_cards:
    if card in origin_cards: result.append(1)
    else: result.append(0)

print(*result)


# ---------------------------------------------------------------
# case 2 : 이분탐색(재귀로 구현) (시간 3928ms)
'''point : 이분탐색 해야할 리스트 정렬해주기!'''
import sys
from unittest import result
N = int(sys.stdin.readline())  # 숫자카드의 개수
origin_cards = sorted(list(map(int, sys.stdin.readline().split())))  # 숫자 카드에 적혀있는 정수 리스트 - 정렬
M = int(sys.stdin.readline())  # 확인해야할 정수의 개수
check_cards = list(map(int, sys.stdin.readline().split()))  # 확인해야할 카드에 적혀있는 정수 리스트

# 이분탐색하는 함수 정의
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스로 정의
    if end_index == None:
        end_index = len(some_list) - 1

    # start_index가 end_index보다 크면 some_list안에 element는 없다
    if start_index > end_index:
        return 0

    # 범위의 중간 인덱스를 찾는다
    mid = (start_index + end_index) // 2

    # base case : 이 인덱스의 값이 찾는 값인지 확인을 해준다
    if some_list[mid] == element:
        return 1

    # recursive case
    # 찾는 항목이 중간 값보다 작으면 리스트 왼쪽을 탐색해준다
    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)

    # 찾는 항목이 중간 값보다 크면 리스트 오른쪽을 탐색해준다
    else:
        return binary_search(element, some_list, mid + 1, end_index)

for card in check_cards:
    # 줄바꿈 제거하는 방법 : end = " "
    print(binary_search(card, origin_cards), end = " ")


# ---------------------------------------------------------------
# case 3 : 다른 사람 풀이 보면서 추가 공부(set로 중복 제거)  (시간: 392ms)
# set : 해시 테이블, 탐색이 빠르다!
'''결과 값을 string +로 출력 -> 시간 제일 짧음!'''
import sys

def solution():
    sys.stdin.readline()  # 사용안하니까 변수에 정의 x
    origin_cards = set(sys.stdin.readline().split())  # 숫자 카드에 적혀있는 정수 set
    sys.stdin.readline()  # 사용안하니까 변수에 정의 x
    check_cards = sys.stdin.readline().split()    # 확인해야할 카드에 적혀있는 정수
    res = ''
    for card in check_cards:
        if card in origin_cards:
            res += '1 '
        else:
            res += '0 '
    print(res)

solution()


# 내 방식으로 바꿔보기 : 결과값을 리스트로 저장(시간 568ms)
'''결과 값을 리스트로 저장하여 unpacking 출력'''
import sys

def solution():
    sys.stdin.readline()  # 사용안하니까 변수에 정의 x
    origin_cards = set(sys.stdin.readline().split())  # 숫자 카드에 적혀있는 정수 set
    sys.stdin.readline()  # 사용안하니까 변수에 정의 x
    check_cards = sys.stdin.readline().split()  # 확인해야할 카드에 적혀있는 정수

    result = []

    for card in check_cards:
        if card in origin_cards:
            result.append(1)
        else:
            result.append(0)
    print(*result)

solution()