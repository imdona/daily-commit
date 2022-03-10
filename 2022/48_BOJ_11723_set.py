'''
백준 11723 [집합] - 구현
문제 : https://www.acmicpc.net/problem/11723

[입력]
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

[출력]
check 연산이 주어질때마다, 결과를 출력한다.
'''
# case 1 : 메모리 30864KB / 시간 4464ms
import sys
M = int(sys.stdin.readline())  # 횟수
S = set()  # 빈 set 정의

for _ in range(M):
    command = sys.stdin.readline().split()  # 명령어

    # 명령어가 2개 이상일때(즉, x가 있을 때) x가 string이므로 int로 바꿔준다.
    if len(command) == 2: command[1] = int(command[1])

    if command[0] == 'add': S.add(command[1])

    elif command[0] == 'remove': S.discard(command[1])  # discard : 있으면 삭제, 없으면 pass

    elif command[0] == 'check': print(1) if command[1] in S else print(0)

    elif command[0] == 'toggle':
        S.remove(command[1]) if command[1] in S else S.add(command[1])

    elif command[0] == 'all': S = set(range(1,21))

    elif command[0] == 'empty': S = set()


# case 2 : 메모리 30864KB / 시간 4024ms -> 공간복잡도는 동일, 시간은 조금 더 빠름
# 파라미터 x가 필요 없는 명령어끼리 구분하여 작성하기
import sys
M = int(sys.stdin.readline())  # 횟수
S = set()  # 빈 set 정의

for _ in range(M):
    command = sys.stdin.readline().split()  # 명령어

    # 파라미터 x가 필요없는 명령어
    if len(command) == 1:
        if command[0] == 'all': S = set(range(1,21))
        else: S = set()

    # 명령어가 2개 이상일때(즉, x가 있을 때) x가 string이므로 int로 바꿔준다.
    else:
        com, x = command[0], int(command[1])  # 자주 쓰니까 변수로 아예 정의해서 쓰기

        if com == 'add': S.add(x)

        elif com == 'remove': S.discard(x)  # discard : 있으면 삭제, 없으면 pass

        elif com == 'check': print(1) if x in S else print(0)

        elif com == 'toggle':
            S.remove(x) if x in S else S.add(x)

