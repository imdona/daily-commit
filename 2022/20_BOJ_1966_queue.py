'''
백준 1966 [프린터큐]
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다.
여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

[입력]
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

[출력]
각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
'''
# try 1 : 중복 중요도가 있으면, 큐의 가장 뒤에 재배치하는 점을 간과했음...
# import sys
# N = int(sys.stdin.readline())  # 총 테스트 케이스의 수

# for _ in range(N):
#     '''총 테스트 케이스의 수만큼 input 받는다.
#     doc = 문서의 개수, num = 궁금한 문서의 현재 Queue에서의 위치(맨 왼쪽이 0번째)
#     importance = 해당 문서의 중요도'''
#     doc, num = map(int, sys.stdin.readline().split())
#     # print(doc, num)

#     importance = list(map(int, sys.stdin.readline().split()))
#     # print(list(importance))  # 중요도를 list로 받기 확인

#     result = 1
#     # print(f"target : {importance[num]}")

#     # 중복도가 중복되지 않는다면
#     if len(importance) == len(set(importance)):
#         for i in importance:
#             if i > importance[num]:
#                 # print(f"i: {i}, target: {importance[num]}")
#                 result += 1

#         print(result)

#     # 중복도가 중복된다면
#     else:
#         print("?")


# ----------------------------------------------------------------
# try 2
import sys
N = int(sys.stdin.readline())  # 총 테스트 케이스의 수

for _ in range(N):
    '''총 테스트 케이스의 수만큼 input 받는다.
    doc = 문서의 개수, num = 궁금한 문서의 현재 Queue에서의 위치(맨 왼쪽이 0번째)
    importance = 해당 문서의 중요도'''
    doc, num = map(int, sys.stdin.readline().split())
    # print(doc, num)

    importance = list(map(int, sys.stdin.readline().split()))
    loc = [i for i in range(doc)]  # 문서의 위치를 저장하기 위해 리스트 만들기
    loc[num] = 'target'  # 궁금한 문서의 위치 저장하기
    result = 0

    while True:
        if importance[0] == max(importance):
            result += 1
            if loc[0] == 'target':
                print(result)
                break
            importance.pop(0)
            print(f"importance: {importance}")
            loc.pop(0)
            print(f"loc: {loc}")
        else:
            importance.append(importance.pop(0))
            print(f"importance: {importance}")
            loc.append(loc.pop(0))
            print(f"loc: {loc}")

'''
print문을 일일이 확인해보면 아래와 같이 확인이 가능! (또는 디버그모드로 Run해보면 시각적으로 더 확실하게 확인이 가능!!)
1
6 0
1 1 9 1 1 1
importance: [1, 9, 1, 1, 1, 1]
loc: [1, 2, 3, 4, 5, 'target']
importance: [9, 1, 1, 1, 1, 1]
loc: [2, 3, 4, 5, 'target', 1]
importance: [1, 1, 1, 1, 1]
loc: [3, 4, 5, 'target', 1]
importance: [1, 1, 1, 1]
loc: [4, 5, 'target', 1]
importance: [1, 1, 1]
loc: [5, 'target', 1]
importance: [1, 1]
loc: ['target', 1]
5
'''