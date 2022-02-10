'''
백준 10816 [숫자 카드2] - 정렬 & 이분탐색 & 자료구조
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

[출력]
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
'''
# test
# origin_cards = sorted([6, 3, 2, 10, 10, 10, -10, -10, 7, 3])
# check_cards = [10, 9, -5, 2, 3, 4, 5, -10]


# ----------------------------------------------------------------
# case 1 : dict를 이용한 Hashing 알고리즘 방식 / 메모리 11452KB, 시간 972ms
import sys
_ = int(sys.stdin.readline())  # 숫자카드의 개수
origin_cards = list(map(int, sys.stdin.readline().split()))  # 숫자 카드에 적혀있는 정수 리스트
M = int(sys.stdin.readline())  # 확인해야할 정수의 개수
check_cards = list(map(int, sys.stdin.readline().split()))  # 확인해야할 카드에 적혀있는 정수 리스트

# count number of each card
count_card = dict()
for i in origin_cards:
    if i in count_card.keys():
        count_card[i] += 1
    else:
        count_card[i] = 1

# print(count_card)  # {-10: 2, 2: 1, 3: 2, 6: 1, 7: 1, 10: 3}

# card check
for card in check_cards:
    if card in count_card.keys():
        print(count_card[card], end = " ")
    else:
        print(0, end = " ")
# out : 3 0 0 1 2 0 0 2


# ----------------------------------------------------------------
# case 1- 2: 결과값 출력 다른 방법
'''
* ' '.join(list) 공백을 구분자로 하여 합쳐 반환하는 함수
    - '구분자'.join(list) : '구분자'로 구분하여 리스트의 문자열을 합쳐 반환
    - ''.join(list) : 공백이나 구분자 없이, 즉 리스트를 바로 이어 붙여서 반환
'''
print(' '.join(str(count_card[i]) if i in count_card else '0' for i in check_cards))


# ----------------------------------------------------------------
# case 2 : Counter 활용 / 메모리 146784KB, 시간 536ms -> 가장 빠른 방법이었다
from collections import Counter
import sys
_ = sys.stdin.readline()
origin_cards = sys.stdin.readline().strip().split()
_ = sys.stdin.readline()
check_cards = sys.stdin.readline().strip().split()

count_card = Counter(origin_cards)
# print(count_card)  # Counter({10: 3, -10: 2, 3: 2, 2: 1, 6: 1, 7: 1})
print(' '.join([f'{count_card[i]}' if i in count_card else '0' for i in check_cards]))


# ----------------------------------------------------------------
# case 3 : 이분탐색 활용 / 메모리 132984KB, 시간 3516ms
'''(참고 블로그 : https://chancoding.tistory.com/45)'''
from sys import stdin
_ = stdin.readline()
origin_cards = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
check_cards = map(int,stdin.readline().split())

def binary_search(element, some_list, start_index, end_index):
    if start_index > end_index:
        return 0

    mid = (start_index + end_index) // 2

    if element == some_list[mid]:
        i, j = 1, 1

        while mid - i >= start_index:
            if some_list[mid-i] != some_list[mid]:
                break
            else: i += 1

        while mid + j <= end_index:
            if some_list[mid+j] != some_list[mid]:
                break
            else: j += 1
        return i + j - 1

    elif element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)

    else:
        return binary_search(element, some_list, mid + 1, end_index)

count_card = {}
for n in origin_cards:
    start = 0
    end = len(origin_cards) - 1
    if n not in count_card:
        count_card[n] = binary_search(n, origin_cards, start, end)

print(' '.join(str(count_card[x]) if x in count_card else '0' for x in check_cards))


# ----------------------------------------------------------------
# case 4 : 파이썬 내장 모듈인 bisect 활용 / 메모리 	113284KB, 시간 1708ms
'''bisect : 파이썬에 내장되어있는 이진탐색 모듈
bisect_left(list, value)는 list에서 value가 들어갈 가장 왼쪽 인덱스,
bisect_right(list, value)는 list에서 value가 들어갈 가장 오른쪽 인덱스를 알려준다.

-> count_by_range 함수
    이 함수의 인자인 left_value와 right_value 사이에 존재하는 숫자들의 갯수를 반환하는 함수이다.
    따라서 left_value와 right_value에 같은 값을 주게 되면 그 숫자의 갯수를 세게 되는 것이다.

(참고 블로그 : https://hongcoding.tistory.com/12)'''

from bisect import bisect_left, bisect_right
from sys import stdin

_ = stdin.readline().rstrip()
origin_cards = sorted(list(map(int,stdin.readline().split())))
_ = stdin.readline().rstrip()
check_cards = list(map(int,stdin.readline().split()))

def count_by_range(li, left_value, right_value):
    right_index = bisect_right(li, right_value)
    left_index = bisect_left(li, left_value)
    return right_index - left_index


for i in range(len(check_cards)):
    print(count_by_range(origin_cards, check_cards[i], check_cards[i]), end=' ')



