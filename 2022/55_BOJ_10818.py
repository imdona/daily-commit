# 10818 최소, 최대 : https://www.acmicpc.net/problem/10818
# case 1 : 메모리 155084KB / 시간 408ms
N = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))

# -------------------------------------------------------------
# case 2 : 메모리 148396KB / 시간 412ms
import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))