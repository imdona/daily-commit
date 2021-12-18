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
nums.sort()
for i in nums:
    print(i)

# 두번째 방법 - 메모리 초과
import sys
N = int(sys.stdin.readline())
nums = [sys.stdin.readline() for _ in range(N)]
nums.sort()
for i in nums:
    print(i)

# 세번째 시도
'''
sort를 쓰는 방식으로는 메모리 초과문제를 해결할 수 없음
1. input하는 숫자는 10000보다 작은수이므로 0이 10000개인 리스트를 만든다.
2. input되는 숫자의 자리에 리스트를 0 -> 해당 숫자로 바꿔준다.
3. 1부터 10000까지 돌면서 0이 아닌 녀석들에 대해서만 프린트를 한다.
    이 때 해당 숫자의 수만큼 출력한다

🔥 10001인 이유는 인데그사 0부터 세리기때문에 계산하기 편하라고!
'''
import sys

N = int(sys.stdin.readline())

# 10001인 이유는 인데그사 0부터 세리기때문에 계산하기 편하라고!
nums = [0] * 10001
for _ in range(N):
    num = int(sys.stdin.readline())
    nums[num] += 1

for i in range(1, 10001):
    if nums[i] != 0:
        # print(i )
        '''여기에 프린트문을 쓰면, 중복되는 값을 1번만 출력함
        그래서 for 문을 하나 더 만들어서 2이면 두 번 프린트하도록!'''
        for j in range(nums[i]):
            print(i)


################################################################
# 정리된 코드
import sys

N = int(sys.stdin.readline())

nums = [0] * 10001
for _ in range(N):
    num = int(sys.stdin.readline())
    nums[num] += 1

for i in range(1, 10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)



