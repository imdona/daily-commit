'''
백준 1259 [팰린드롬수] - bronze 1
어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다.
각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.
입력의 마지막 줄에는 0이 주어지며, 이 줄은 문제에 포함되지 않는다.
'''

while True:
    num = str(input())
    if num == '0':
        break
    print('yes') if num == num[::-1] else print('no')

# 위의 삼항연산자를 풀어서 쓰면 아래와 같이 표현할 수도 있다
while True:
    num = str(input())
    if num == '0':
        break
    elif num == num[::-1]:
        print('yes')
    else:
        print('no')


