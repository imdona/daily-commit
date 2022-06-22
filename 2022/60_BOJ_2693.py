# 2693 [N번째 큰 수] : https://www.acmicpc.net/problem/2693
# case 1 : 메모리 30840KB / 시간 236ms
T = int(input())

for _ in range(T):
    array = list(map(int, input().split()))
    array.sort()  # 오림차순 정렬
    print(array[-3])  # 세번째로 큰 수 출력

# -------------------------------------------------------------
# case 2 : 메모리 29440KB / 시간 56ms
import sys

T = int(sys.stdin.readline())

for t in range(T):
	array = sorted(list(map(int, sys.stdin.readline().split())))
	print(array[-3])