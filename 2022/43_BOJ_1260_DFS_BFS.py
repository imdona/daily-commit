'''
백준 1260 [DFS와 BFS]
문제 - https://www.acmicpc.net/problem/1260
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

[입력]
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

[출력]
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

* 개념정리
    1. DFS(Depth First Search, 깊이 우선 탐색)
        : 한 방향으로 갈 수 있는만큼 깊게 탐색한다.
        -> 후입선출(LIFO)인 스택(stack) 활용하면 쉽게 구현 가능
    2. BFS(Breadth First Search, 너비 우선 탐색)
        : 시작점인 루트노트와 같은 거리에 있는 노드를 우선 방문한다
        -> 선입선출(FIFO, First in first out) 방식인 큐(Queue)를 활용하면 쉽게 구현 가능!
        -> 덱(Deque) : 왼쪽과 오른쪽에서 모두 삽입과 삭제가 가능한 큐! collections 모듈에 내장되어있음
'''
# case 1
from collections import deque
import queue
import sys


def DFS(graph, root):
    '''Depth First Search, 깊이 우선 탐색'''
    visited = []  # 방문 경로
    stack = [root]  # 루트노드
    # print(stack)  # [1]

    while stack:  # stack이 빌 때까지
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))  # graph에서 해당 노드(키)와 연결된 값 - 방문한 값 빼기(차집합)
                temp.sort(reverse = True)  # 내림차순으로 정렬(pop은 뒤에서부터 빼온다, 작은 수부터 방문해서)
                stack += temp  #list append

    return " ".join(str(i) for i in visited)


def BFS(graph, root):
    '''Breadth First Search, 너비 우선 탐색'''
    visited = []  # 방문 경로
    queue = deque([root])  # 루트노드
    # print(queue)  # deque([1])

    while queue:  # 덱이 빌 때까지
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))  # graph에서 해당 노드(키)와 연결된 값 - 방문한 값 빼기(차집합)
                temp.sort()  # 오름차순으로 정렬(popleft로 앞부터 빼온다)
                queue += temp  #list append

    return " ".join(str(i) for i in visited)


node, edge, start = map(int, sys.stdin.readline().split())
graph = {}

for _ in range(edge):
    '''그래프 만들기'''
    n1, n2 = map(int, sys.stdin.readline().split())
    # graph dict에 n1이 없으면, 키와 값 추가 -> {1 : [2]}
    if n1 not in graph:
        graph[n1] = [n2]
    # graph dict에 n1 키값이 이미 있으면, 값만 리스트에 추가 -> {1 : [2, 3]}
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

# print(graph)  # {1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}

print(DFS(graph, start))
print(BFS(graph, start))
