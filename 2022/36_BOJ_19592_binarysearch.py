'''
백준 19592 [장난감 경주]
문제 : https://www.acmicpc.net/problem/19592

[입력]
첫 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 줄에 N, X, Y가 공백으로 구분되어 주어진다.
둘째 줄에 N개의 정수가 공백으로 구분되어 주어지는데 이는 각 장난감 자동차의 속도 V[i]를 나타낸다.

[출력]
각 테스트 케이스에 대해 단독 우승을 위해 부스터를 사용해서 이동해야하는 최소한의 거리를 출력한다.
만약 부스터를 쓰지 않고도 단독 우승이 가능하다면 0을 출력한다.
부스터를 최대치로 사용하고도 단독 우승이 불가능하다면 -1을 출력한다.

[제한]
1 ≤ T ≤ 10
2 ≤ N ≤ 1,000
1 ≤ Y ≤ X ≤ 1,000,000
1 ≤ V[i] ≤ 1,000,000
'''
# case 1
import sys
T = int(sys.stdin.readline())  # test case

# 함수 정의
def solution(N, X, Y, V):
    lap_time = [ X/speed for speed in V]  # 한바퀴 시간 = 트랙 길이/자동차 속도 (시간 = 거리/속도)
    best_lap = min(lap_time)  # 가장 짧은 시간이 최고

    # 부스터를 사용하지 않아도 단독우승이 가능한 상황 : 마지막 인덱스(나)가 최적의 시간일 때 & 그 개수가 1개일 때
    # if lap_time[N-1] == best_lap
    if lap_time[-1] == best_lap and lap_time.count(best_lap) == 1:
        return 0

    # 부스터를 사용해서 이동해야하는 최소한의 거리 = 시간*속력
    minimum = int(X - ((best_lap-1) * V[-1]) + 1)
    if minimum <= Y: return minimum
    else: return -1  # 최대치를 사용하고도 단독우승이 불가능

for _ in range(T):
    N, X, Y = map(int, sys.stdin.readline().split())  # 참가자 수, 트랙 길이, 부스터 한계치
    speeds = list(map(int, sys.stdin.readline().split()))  # 자동차 속도
    print(solution(N, X, Y, speeds))


# ----------------------------------------------------------------
# case 2 : binary search
import sys

T = int(sys.stdin.readline())  # test case

for _ in range(T):
    N, X, Y = map(int, sys.stdin.readline().split())  # 참가자 수, 트랙 길이, 부스터 한계치
    speeds = list(map(int, sys.stdin.readline().split()))  # 자동차 속도

    # 마지막 인덱스(나) 속도가 가장 빠를 때 & 그 개수가 1개일 때
    if speeds.count(max(speeds)) == 1 and max(speeds) == speeds[-1]:
        print(0)
        continue

    # target(시간) : 나를 뺜 속도 중 최대값으로 트랙길이 나눠주기 (시간 = 거리/속도)
    target = X / max(speeds[:-1])
    velocity = speeds[-1]  # 나의 속도

    #  최대치를 사용하고도 단독우승이 불가능할 때
    # 시간 = (트랙길이 - 부스터한계치) / 속도 + 1
    if ((X - Y) / velocity) + 1 >= target:
        # print((X - Y) / velocity)
        print(-1)
        continue

    start = 1
    end = Y  # 트랙 길이
    answer = 0

    # binary search
    while start <= end:
        mid = (start + end) // 2
        temp = ((X - mid) / velocity) + 1

        if temp < target:
            answer = mid
            end = mid - 1

        else:
            start = mid + 1

    print(answer)