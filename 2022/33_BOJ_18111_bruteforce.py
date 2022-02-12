'''
백준 18111 [마인크래프트] - 구현 & 브루트포스 알고리즘
문제 : https://www.acmicpc.net/problem/18111
1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다. 밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다. ‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.
단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다. 또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

[입력]
첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107)
둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다. (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.

[출력]
첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.
'''
'''
* defaultdict() : 유사 딕셔너리, 기본 값을 지정한 딕셔너리
    1. 미리 삽입하지 않은 key도 호출과 동시에 지정할 수 있다. 기존에 없던 key를 호출하면, key에 대한 값이 0으로 자동 초기화 된다.
    2. 심지어 미리 선언하지 않은 key에 값을 더해주는 것도 가능함!
    3. lambda식을 함께 사용해 원하는 초기값도 정할 수 있음 : defaultdict(lambda: '원하는 초기값')
'''
# case 1 : defaultdict
import sys
from collections import defaultdict

N, M, B = map(int, sys.stdin.readline().split())
lands = defaultdict(int)

for _ in range(N):
    for i in list(map(int, sys.stdin.readline().split())):
        lands[i] += 1
# print(lands)  # defaultdict(<class 'int'>, {0: 11, 1: 1})

answer = [N * M * 2 * 256, 0]
key_li = list(lands.keys())
# print(key_li)  # [0, 1]

# 가잔 낮은 높이 ~ 가장 높은 높이의 범위에서 반복문
for value in range(min(key_li), max(key_li) + 1):
    count, block = 0, B

    for key in key_li:
        if key > value:
            count += 2 * (key - value) * lands[key]
            block += (key - value) * lands[key]

        elif key < value:
            count += (value - key) * lands[key]
            block -= (value - key) * lands[key]

    if block >= 0:
        if count < answer[0]:
            answer[0] = count
            answer[1] = value
        if count == answer[0] and answer[1] < value:
            answer[1] = value

print(answer[0], answer[1])


# ----------------------------------------------------------------
# case 2 : best 시간복잡도 풀이 방법
import sys
N, M, B = map(int, sys.stdin.readline().split())
lands = [0] * 257

total = 0
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    total += sum(temp)
    for j in temp:
        lands[j] += 1

h1 = round(total / (N*M))
h2 = (total+B) // (N*M)
result = []

for target in range(h1 - 1, h2 + 1):
    X, Y = 0, 0
    for j in reversed(range(257)):
        if j > target:
            X += (j-target) * lands[j]
        elif j < target:
            Y += (target-j) * lands[j]
    result.append((2*X + Y, target))
print(' '.join(map(str, sorted(result, key = lambda x: (x[0], -x[1]))[0])))