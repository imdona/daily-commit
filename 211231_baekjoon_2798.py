'''
백준 2798 [블랙잭] - 브루트포스 알고리즘
카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.
한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

[입력]
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

[출력]
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
'''
# 최종 제출 코드
# 입력 받기
import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

# 5개 중 3개 조합의 모든 합계를 담는 리스트 만들기
permutation3 = list(permutations(cards, 3))
sum_list = list(map(sum, permutation3))

result = 0
for i in sum_list:
    if M >= i:
        result = max(result, i)
print(result)

# 풀이
# 입력 받기
import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

# 5개 중 3개 조합의 모든 합계를 담는 리스트 만들기
permutation3 = list(permutations(cards, 3))
# print(permutation3)
sum_list = list(map(sum, permutation3))
# print(sum_list)
# print(len(permutation3) == len(sum_list)) # True

# for문 첫번째 시도 - 오답(문제를 잘못 이해함) -> M을 넘지 않아야하는데, 차이가 작은 것에만 고려해서 생각함
# M을 넘지 않으면서 최대한 가까운 수 출력 - 차이가 최소인 값 찾기
# # diff, result 임의로 첫번째 값으로 지정
# diff, result = abs(M - sum_list[0]), sum_list[0]
# print(diff, result)
# for i in sum_list:
#     if abs(M - i) < diff:
#         diff = abs(M - i)
#         result = i
#         print(diff, result)
# print(result)

# sum_list를 for문으로 돌면서 M보다 작거나 같으면 result와 비교해서 최댓값으로 바꿔주기
result = 0
for i in sum_list:
    if M >= i:
        result = max(result, i)
print(result)

## 다른 풀이방법
import sys
N, M = map(int, sys.stdin.readline().split())
cards = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)
sum_list = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M:
                sum_list.append(sum)
                break
print(max(sum_list))



################################################################
"""
🔍 python에서 조합 구하기
1. 하나의 리스트의 모든 조합 구하기 : combinations
    from itertools import combinations
    list(combinations(items, n))

    🥕 예제
    items = [1, 2, 3, 4, 5]
    list(combinations(items, 3))
    # [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]

2. 두개 이상의 리스트의 모든 조합 구하기 : product
    from itertools import product
    list(product(*items))

    🥕 예제
    items = [['1', '2', '3', '4'], ['a', 'b', 'c,']]
    # ('1', 'a'), ('1', 'b'), ('1', 'c,'), ('2', 'a'), ('2', 'b'), ('2', 'c,'), ('3', 'a'), ('3', 'b'), ('3', 'c,'), ('4', 'a'), ('4', 'b'), ('4', 'c,')]

🔍 python에서 절댓값을 구해주는 함수 : abs(x) -> import 필요없이 바로 사용 가능!
"""
