'''
백준 2164 [카드2]
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다.
마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

[출력]
첫째 줄에 남게 되는 카드의 번호를 출력한다.
'''
# case 1 : 시간 초과
import sys
N = int(sys.stdin.readline())
cards = [i for i in range(1, N+1)]
# print(cards)

while True:
    # cards가 한 개가 될 때까지 반복
    if len(cards) == 1:
        break
    cards.pop(0)
    cards.append(cards.pop(0))

print(*cards)  # unpacking


# --------------------------------------------------------------
# case 2 : collections의 deque 활용하기
from collections import deque
import sys
N = int(sys.stdin.readline())
cards = deque()
for i in range(1, N+1):
    cards.append(i)
# print(cards)

while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())

print(*cards)  # deque도 *으로 unpacking이 가능함


# --------------------------------------------------------------
# case 3 : 규칙을 이용한 풀이(풀이 참고 : https://pacific-ocean.tistory.com/61)
'''
입력:1 -> 출력:1
입력: 2 -> 출력: 2
입력: 3 -> 출력: 2
입력: 4 -> 출력: 4
입력: 5 -> 출력: 2
입력: 6 -> 출력: 4
입력: 7 -> 출력: 6
입력: 8 -> 출력: 8
입력: 9 -> 출력: 2
입력: 10 -> 출력: 4
입력: 11 -> 출력: 6
입력: 12 -> 출력: 8
입력: 13 -> 출력: 10
입력: 14 -> 출력: 12
입력: 15 -> 출력: 14
* 규칙 : ((입력값) - (2의 n제곱(입력값보다 작은것의 최댓값))) * 2
'''
import sys
N = int(sys.stdin.readline())
s = 1

while True:
    if s * 2 > N:
        break
    else:
        s *= 2

if N == s:
    print(s)

else:
    print(N - (s - (N - s)))
