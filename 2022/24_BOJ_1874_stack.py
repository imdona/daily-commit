'''
백준 1874 [스택 수열]
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
이를 계산하는 프로그램을 작성하라.

[입력]
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

[출력]
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
'''
'''
스택의 직관적 이해 : 팬케이크를 위로 쌓아서, 꺼낼 때 가장 위에 있는 팬케이크부터 꺼내는 구조!

* 예제 1번은 8 4 3 6 8 7 5 2 1 순으로 입력이 되는데 문제를 먼저 이해해보면,
1. 8은 8이하의 숫자가 8개 입력됨을 알려준다.
2. 오름차순 수열을 push & pop을 해서 [4, 3, 6, 8, 7, 5, 2, 1]으로 만들어주어야한다.
    1) push 4번 -> [1, 2, 3, 4] / result = []
    2) pop 2번 -> [1, 2] / result = [4, 3]
    3) push 2번 -> [1, 2, 5, 6] / result = [4, 3]
    4) pop 1번 -> [1, 2, 5] / result = [4, 3, 6]
    5) push 2번 -> [1, 2, 5, 7, 8] / result = [4, 3, 6]
    6) pop 5번 -> [] / result = [4, 3, 6, 8, 7, 5, 2, 1]
    result = [4, 3, 6, 8, 7, 5, 2, 1]
3. 결론 : 1부터 n까지에 수에 대해 차례로 [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.

*예제 2번은
1. 5는 5개 이하의 숫자 5개가 입력됨을 알려준다.
2. [1, 2, 5, 3, 4]로 만들 수 없는 이유는, pop으로 맨 위의 데이터가 나오게되는데 수열이 오름차순이기 때문에 5 다음으로 [3, 4] 빼올 수가 없음
    1) push 1번 -> [1] / result = []
    2) pop 1번 -> [] / result = [1]
    3) push 1번 -> [2] / result = [1]
    4) pop 1번 -> [] / result = [1, 2]
    5) push 1번 -> [5] / result = [1, 2]
    6) pop 1번 -> [] / result = [1, 2, 5]
3. 하면 5보다 작은 수인 3, 4를 넣을 수 없음
'''
# case 1
import sys
n = int(sys.stdin.readline())  # test case
stack = []
result = []
count = 1
condition = True

# test case만큼 반복하여 정수를 입력받음
for _ in range(n):
    num = int(sys.stdin.readline())

    # num보다 작은 수까지 stack에 넣어주고, result에 "+" 추가
    while count <= num:
        stack.append(count)
        result.append("+")
        count += 1
    # print(stack)
    # print(result)

    # stack의 마지막원소가 num이면, 없애고 result에 "-" 추가
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    # 그것이 아니라면(순서가 오름차순이 아니면) False
    else:
        condition = False

# 숫자 입력은 우선 다 받고 마지막에 확인해서 출력하기
if condition == False:
    print("NO")
else:
    print(*result, sep = '\n')  # unpacking & 줄바꿈


# -----------------------------------------------------------------------------------
# case 2 : deque 활용(https://devchopin.com/blog/86/)
from collections import deque
import sys

n = int(sys.stdin.readline())  # test case

deq = deque()
stack = []
result = []

# test case만큼 반복하여 정수를 입력받음
for _ in range(n):
    num = int(sys.stdin.readline())
    deq.append(num)
# print(deq)  # deque([4, 3, 6, 8, 7, 5, 2, 1])

for i in range(1, n+1):
    stack.append(i)
    result.append('+')
    # print(stack)
    # print(result)

    while True:
        if stack and stack[-1] == deq[0]:
            stack.pop()
            deq.popleft()
            result.append('-')
        else:
            break
if deq:
    print('NO')
else:
    print(*result, sep = '\n')  # unpacking & 줄바꿈