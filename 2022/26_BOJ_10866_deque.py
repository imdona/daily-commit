'''
백준 10866 [덱]
정수를 저장하는 덱(deq)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

[입력]
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

[출력]
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''
# case 1
import sys
from collections import deq

N = int(sys.stdin.readline())  # test case
deq = deq()

for _ in range(N):
    command = sys.stdin.readline().split()
    # print(command)  # list type 확인
    order = command[0]

    if order == 'push_front': deq.appendleft(command[1])

    elif order == 'push_back': deq.append(command[1])

    elif order == 'pop_front':
        if deq: print(deq.popleft())
        else: print(-1)

    elif order == 'pop_back':
        if deq: print(deq.pop())
        else: print(-1)

    elif order == 'size': print(len(deq))

    elif order == 'empty':
        if deq: print(0)
        else: print(1)

    elif order == 'front':
        if deq: print(deq[0])
        else: print(-1)

    elif order == 'back':
        if deq: print(deq[-1])
        else: print(-1)


# -------------------------------------------------------------------------
# case 2 : if & else comprehension
import sys
N = int(sys.stdin.readline())
deq = []

for _ in range(N):
    command = sys.stdin.readline().rstrip()

    if 'push_front' in command:
        deq.insert(0, int(command.split()[1]))

    elif 'push_back' in command:
        deq.append(int(command.split()[1]))

    elif command == 'pop_front':
        print(deq.pop(0)) if deq else print(-1)

    elif command == 'pop_back':
        print(deq.pop()) if deq else print(-1)

    elif command == 'size':
        print(len(deq))

    elif command == 'empty':
        print(0) if deq else print(1)

    elif command == 'front':
        print(deq[0]) if deq else print(-1)

    elif command == 'back':
        print(deq[-1]) if deq else print(-1)