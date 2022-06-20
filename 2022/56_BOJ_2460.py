# 2460 지능형 기차 2 : https://www.acmicpc.net/problem/2460
# case 1 : 메모리 30840KB / 시간 68ms
# 최대 사람 수 변수 정의
max_people, people = 0, 0
# 10번 반복
for _ in range(10):
    bye, hi = map(int, input().split())  # 내린 사람 & 탄 사람 변수로 받기
    people = people - bye + hi  # 탑승 사람 수 최신화
    # people += hi - bye  # 같은 표현

    # 최대 사람 수와 비교하고 최신화
    if people > max_people:
        max_people = people

print(max_people)


# -------------------------------------------------------------
# case 2 : 메모리 30840KB / 시간 68ms
# sys로 풀었는데 메모리 시간 모두 동일함
import sys
input = sys.stdin.readline

max_people, people = 0, 0
# 10번 반복
for _ in range(10):
    bye, hi = map(int, input().split())  # 내린 사람 & 탄 사람 변수로 받기
    people = people - bye + hi  # 탑승 사람 수 최신화
    # people += hi - bye  # 같은 표현

    # 최대 사람 수와 비교하고 최신화
    if people > max_people:
        max_people = people

print(max_people)


# -------------------------------------------------------------
# case 3 : 메모리 29284KB / 시간 52ms
# 다른 사람 풀이 : 같은 형식인데 시간 메모리가 짧음
import sys

current = maxpass = 0

for i in range(10):
    A, B = map(int, sys.stdin.readline().split())
    current -= A
    current += B
    if maxpass < current: maxpass=current

print(maxpass)