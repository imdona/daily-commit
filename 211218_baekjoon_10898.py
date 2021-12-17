'''
백준 10989 [수 정렬하기 3] - silver 5 & 메모리 제한 문제!
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

[입력]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

[출력]
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

# 첫번째 방법 - 메모리 초과
N = int(input())
nums = [int(input()) for _ in range(N)]
for i in nums:
    print(i)

# 두번째 방법 - 메모리 초과
import sys
N = int(sys.stdin.readline())
nums = [sys.stdin.readline() for _ in range(N)]
for i in nums:
    print(i)



