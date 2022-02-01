'''
백준 4949 [균형잡힌 세상]
세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.
정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

<조건>
모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.

정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

[입력]
하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.
입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

[출력]
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
'''
# case 1
'''
의사 코드
1. if i == "[", "(": stack.append(i)  # 좌측 괄호면, stack에 append
2. if i == "]", ")": stack.pop()  # 우측 괄호면, stack의 원소와 비교하고 pop
3. if input == ".": break  # "."이 입력되면 종료
4. condition 조건을 나타내는 변수를 만들어서 True일 때만 "yes" 출력
'''
import sys

while True:
    # sentence = input()
    sentence = sys.stdin.readline().rstrip()  # rstrip() : 오른쪽 제거

    # "."이 입력되면 종료
    if sentence == ".":
        break

    stack = []
    condition = True

    for i in sentence:
        # 좌측 괄호가 나오면 stack에 append
        if i == "[" or i == "(":
            stack.append(i)

        # 우측 괄호가 나오면 좌측 괄호가 있으면 stack pop, 없으면 break
        elif stack and (i == ")" or i == "]"):  # stack의 원소가 있고, 우측 괄호가 나오는 경우
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            else:
                condition = False

        elif not stack and (i == ")" or i == "]"):  # stack이 비어있고, 우측 괄호가 나오는 경우
            condition = False

    # 조건 True 상태이고, stack이 비어있을 때 yes
    print("yes" if condition and not stack else "no")


# --------------------------------------------------------------
# case 2
import sys

def is_valid(s: str) -> bool:
    stack = []

    for i in s:
        # 좌측 괄호 (, [ 한번에 체크
        if i in '([':
            stack.append(i)

        elif i in ')]':
            if len(stack) == 0 or (stack.pop() + i) not in ('()', '[]'):
                return False

    return len(stack) == 0

while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break
    print('yes' if is_valid(s) else 'no')