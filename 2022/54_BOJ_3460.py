# 3460 이진수 : https://www.acmicpc.net/problem/3460
# case 1 : 메모리 30840KB / 시간 64ms
T = int(input())

# 내장함수인 bin()을 활용하여 이진수로 바꾸는 방법 활용
for _ in range(T):
    # 순서 거꾸로
    bnum = list(reversed(bin(int(input()))[2:]))  # 0b 제거 / string type
    # print(bnum)
    for i in range(len(bnum)):
        if bnum[i] == '1':
            print(i, end = ' ')


# -------------------------------------------------------------
# case 2 : 메모리 30840KB / 시간 68ms
T = int(input())

# 내장함수인 bin()을 활용하여 이진수로 바꾸는 방법 활용
for _ in range(T):
    bnum = bin(int(input()))[2:]  # 0b 제거 / string type
    for i in range(len(bnum)):
        # 순서 거꾸로
        if bnum[-i -1] == '1':
            print(i, end = ' ')

# -------------------------------------------------------------
# case 3 : 메모리 29284KB / 시간 52ms
T = int(input())
for _ in range(T):
    # f-string 활용하여 2진수로 바꿔주고 순서 거꾸로
    bnum = f'{int(input()):2b}'[::-1]
    # bnum = format(int(input()), 'b')  # 같은 표현
    # print(bnum)
    G = (b for b in range(len(bnum)) if bnum[b] == '1')  # list comprehension
    print(*G)  #unpacking


# -------------------------------------------------------------
# case 4 : 메모리 30840KB / 시간 72ms
# 이진수로 바꾸면서 나머지로 바로 확인하고 출력
T = int(input())
for _ in range(T):
    n = int(input())
    i = 0
    while n > 0:
        if n % 2 == 1:  # 나머지가 1이면 출력
            print(i, end=' ')
        n = n // 2  # 몫
        i += 1

# -------------------------------------------------------------
# cf) 이진수로 만드는 함수 직접 구현
def getBinaryNum(num, result = []):
    a = num // 2
    b = num % 2
    result.append(b)
    if a == 0: return result[::-1]
    else: return getBinaryNum(a, result)

T = int(input())
for _ in range(T):
    bnum = getBinaryNum(int(input()))[::-1]  # 거꾸로
    # print(bnum)
    # enumerate 활용하여 index 번호 프린트하기 & Unpacking
    print(*(i for i, x in enumerate(bnum) if int(x)))  # if int(x) = if 1 = if True

