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


# -------------------------------------------------------------
# 15650 [N과 M(2)] - 백트래킹
# case 1
'''
깊이 우선 탐색(DFS)
참고 : https://zidarn87.tistory.com/331
추후 다시 풀이
'''
N, M = map(int, input().split())
permu = []

def dfs(start):
    # 리스트의 개수가 M개이면 탈출 후 출력
    if len(permu) == M:
        print(" ".join(map(str, permu)))

    for i in range(start, N+1):
        if i not in permu:
            permu.append(i)
            dfs(i+1)
            permu.pop()

dfs(1)