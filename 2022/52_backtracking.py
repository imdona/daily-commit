'''
백준 단계별 문제 : 백트래킹
* https://www.acmicpc.net/step/34
'''
# 15649 [N과 M(1)] - 백트래킹
# case 1 - 메모리 35268KB / 시간 176ms
from itertools import permutations
N, M = map(int, input().split())
permu = sorted(list(permutations(list(range(1, N+1)), M)))

for per in permu:
    print(*per)


# case 2 - 메모리 31784KB / 시간 60ms
from itertools import permutations

N, M = map(int, input().split())
li = map(str, range(1, N+1))
print('\n'.join(list(map(' '.join, permutations(li, M)))))  # 각 수열을 공백으로 구분하고, 줄바꿈하여 출력
