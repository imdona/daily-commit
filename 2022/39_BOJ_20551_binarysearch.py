'''
백준 20551 [Sort 마스터 배지훈의 후계자] - 정렬 & 이분탐색 & 트리를 사용한 집합과 맵
지훈이는 Sort 마스터다. 오랫동안 Sort 마스터 자리를 지켜온 지훈이는 이제 마스터 자리를 후계자에게 물려주려고 한다.
수많은 제자들 중에 후계자를 고르기 위해서 지훈이는 제자들에게 문제를 준비했다. 먼저 제자들에게 N개의 원소를 가진 배열A를 주고, A의 원소들이 오름차순으로 정렬된 배열B를 만들게 한다.
그다음 M개의 질문을 한다. 각 질문에는 정수 D가 주어진다. 제자들은 주어진 정수D가 B에서 가장 먼저 등장한 위치를 출력하면 된다. 단, D가 B에 존재하지 않는 경우에는 -1를 출력한다.
Sort 마스터의 자리를 너무나도 물려받고 싶은 창국이를 위해 지훈이의 문제를 풀 수 있는 프로그램을 만들어 주자.

[입력]
첫째 줄에 배열A의 원소의 개수 N과 질문의 개수 M이 공백으로 구분되어 주어진다.
다음 줄부터 N줄에 걸쳐 정수 A_0, A_1, ... , A_{N-1}이 주어진다.
다음 줄부터 M줄에 걸쳐 정수 D가 주어진다.

[출력]
M개의 질문에 대해서 주어진 D가 B에서 처음으로 등장한 위치를 출력한다. 단, 존재하지 않는다면 -1를 출력한다. (배열에서 가장 앞의 원소의 위치는 0이다.)
'''
# case 1 (메모리 63240KB, 시간 528ms)
import sys
N, M = map(int, sys.stdin.readline().split())
A = sorted([int(sys.stdin.readline()) for _ in range(N)])
B = [int(sys.stdin.readline()) for _ in range(M)]

# binary search function
def binary_search(element, some_list, start = 0, end = None):
    if end == None: end = len(some_list) - 1
    result = -1  # 초기 인덱스 -1(가장 왼쪽)으로 지정(point!)

    while start <= end:
        mid = (start + end) // 2

        # 중간 값 < 찾는 값 -> 리스트 오른쪽 탐색
        if some_list[mid] < element: start = mid + 1
        # 중간값 >= 찾는 값 -> 리스트 왼쪽 탐색 : 같을 때까지 줄인다(point!)
        elif some_list[mid] >= element: result = mid; end = mid - 1

    if some_list[result] == element: return result
    else: return -1  # 없으면 -1 리턴

for num in B:
    print(binary_search(num, A))


# ------------------------------------------------------------------------------
# test
if __name__ == '__main__':
    for i in [-1, 10, 5, 9, 0]:
        print(binary_search(i, [-1, 0, 2, 3, 9]))

    print("----------------------------------------------------")

    for j in [3, 10, 4, 2]:
        print(binary_search(j, sorted([3, 3, 4, 9, 2, 5, 3, 4])))


# ------------------------------------------------------------------------------
# case 2 : 파이썬에 내장되어있는 이진 검색 함수 bisect_left 활용 (메모리 43000KB, 시간 588ms)
'''
1. bisect_left(list, x) : 정렬된 list에 x를 삽입할 위치를 리턴해준다. x가 이미 있으면, 기존 항목의 왼쪽 위치를 반환
2. bisect_right(list, x) : bisect_left와 거의 같은 함수인데, x가 이미 있으면, 기존 항목의 오른쪽의 위치를 반환
    * python documentation : https://docs.python.org/ko/3/library/bisect.html
'''
from bisect import bisect_left
import sys

N, M = map(int, sys.stdin.readline().split())
A = sorted([int(sys.stdin.readline()) for _ in range(N)])

for _ in range(M):
    num = int(sys.stdin.readline())

    index = bisect_left(A, num)
    if index >= N or A[index] != num:
        print(-1)
    else:
        print(index)


