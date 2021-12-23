'''
백준 1026 [보물] - silver4 : 수학, 정렬, 그리디 알고리즘
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
S = A[0] × B[0] + ... + A[N-1] × B[N-1]
S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
S의 최솟값을 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 N이 주어진다.
둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다.
N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

[출력]
첫째 줄에 S의 최솟값을 출력한다.
'''
'''
첫번째 풀이
순서를 무작위로 바꿀 수 있는데 차례로 넘어가는 상황만 고려를 했다.
OMG.. numpy array를 써보고싶어서 많은 도전을 해봤는데 그걸로 만족하자..
'''
import numpy as np

N = int(input())
A = list(map(int, list(input().split())))
B = list(map(int, list(input().split())))
# print(A, B)

A, B = np.array(A), np.array(B)
# print(A, B)

S = []
for i in range(N):
    print(A, B)
    S.append(sum(A*B))
    num = A[0]
    A = A[1:]
    A = np.append(A, num)
    i += 1
print(S)
print(min(S))


## numpy array 연구
# A = np.array([1,2,3])
# B = np.array([1,2,3])
# print(sum(A*B))
# # np.delete(A, 0)
# print(A)
# num = A[0]
# print(A[1:])
# A = A[1:]
# print(np.append(A, num))

'''
두번째 풀이
문제를 다시 읽고 생각을 해보았다.
A list의 가장 작은 값과 B list의 가장 큰 값을 매칭해주어야 A*B의 값이 최솟값이 되는 방향
알고리즘을 다시 만들어보자
A.pop(A.index(min(A))) : A원소의 최솟값의 인덱스번호를 pop메소드에 넘겨 삭제하고, 삭제된 원소를 return으로 받음
'''
N = int(input())
A = list(map(int, list(input().split())))
B = list(map(int, list(input().split())))

result = 0
for _ in range(N):
    result += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
print(result)

'''
세번째 풀이
원래는 B list의 원소 순서를 바꾸면 안되지만, 해당 제약이 없어지면
문제는 더 간단하게 풀 수 있다.
한 리스트는 오름차순, 다른 리스트는 내림차순으로 정렬하여 서로 곱해주면 된다.
'''

N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))[::-1]

result = 0
for i in range(N):
    result += A[i] * B[i]
print(result)