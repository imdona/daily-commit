'''
백준 9012 [괄호]
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

[입력]
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.

[출력]
출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 
'''
# case 1 : stack list 만들기
import sys
T = int(sys.stdin.readline())  # test case

for _ in range(T):
    string = sys.stdin.readline().rstrip()
    # print(f"string: {string}")

    stack = []
    condition = True

    for i in string:
        # 좌측 괄호가 먼저 나오면 stack에 추가
        if i == "(": stack.append(i)

        # stack이 있고, 우측괄호가 나오면
        elif stack and i == ")":
            if stack[-1] == "(": stack.pop()
            else: condition = False

        # stack이 비어있꼬, 우측괄호가 나오면
        elif not stack and i == ")": condition = False

    print("YES" if condition and not stack else "NO")


# --------------------------------------------------------------
# case 2 : stack 변수로 저장
import sys
T = int(sys.stdin.readline())  # test case

for _ in range(T):
    string = sys.stdin.readline().rstrip()
    stack = 0

    for i in string:
        # 좌측 괄호부터 시작해서 + - 로 체크
        if i == "(":
            stack += 1
            # print(stack)
        # 우측괄호부터 시작하면 바로 stack이 0보다 작아지고 반복문 break
        else:
            stack -= 1
            # print(stack)
            if stack < 0:
                break

    print("YES" if stack == 0 else "NO")
