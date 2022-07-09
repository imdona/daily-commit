# 1021 [회전하는 큐] : https://www.acmicpc.net/problem/1021
# case 1 : 메모리 32432KB / 시간 92ms
# collections 라이브러리의 내장함수 덱 활용
from collections import deque
N, M = map(int, input().split())
idx = list(map(int ,input().split()))  # 뽑아내려고 하는 수의 인덱스
que = deque([i for i in range(1, N + 1)])  # 큐
count = 0

for i in range(len(idx)):
    # 1번
    if idx[i] == que[0]:
        que.popleft()
        continue

    que_idx = que.index(idx[i])
    # 2번이 이득일 때
    if  que_idx > len(que)//2:
        que.rotate(len(que) - que_idx)
        count += (len(que) - que_idx)
    # 3번이 이득일 때
    else:
        que.rotate(-que_idx)
        count += que_idx

    que.popleft()

print(count)


# -------------------------------------------------------------
# case 2 : 메모리 32432KB / 시간 88ms
# 더 간단하게
from collections import deque

N, M = map(int, input().split())
idx = list(map(int ,input().split()))  # 뽑아내려고 하는 수의 인덱스
que = deque([i for i in range(1, N + 1)])  # 큐
count = 0

for num in idx:
    while True:
        if que[0] == num:
            que.popleft()  # 1번
            break
        else:
            if que.index(num) <= len(que)//2:
                que.rotate(-1)  # 2번 연산(왼쪽)
            else:
                que.rotate(1)  # 3번 연산(오른쪽)
            count += 1

print(count)


# -------------------------------------------------------------
# case 3 : 메모리 29284KB / 시간 52ms
# 공간 시간 1등 풀이법
n, m = map(int, input().split())
que = [i for i in range(1, n+1)]  # 큐

count = 0

for find in map(int, input().split()):
    ix = que.index(find)
    count += min(len(que[ix:]), len(que[:ix]))  # 더 가까운 쪽 찾기
    que = que[ix+1:] + que[:ix]  # 뽑아낸 수는 없애고 위치바꿔주기

print(count)


# -------------------------------------------------------------
# case 4 : 메모리 29284KB / 시간 52ms
# 큐 구현
class Queue(object):
    def __init__(self, n):
        # 큐 생성자 함수
        self.q = []
        for i in range(1, n+1):
            self.q.append(i)


    def pop(self, x):
        for i in range(len(self.q)):
            if self.q[i] == x:
                idx = i
        f = idx
        r = len(self.q) - idx
        while self.q[0] != x:
            self.q.append(self.q[0])
            del self.q[0]
        del self.q[0]
        return min(f, r)

n, m = map(int, input().split())
idx = list(map(int, input().split()))
que = Queue(n)
count = 0

for i in idx:
    count += que.pop(i)

print(count)