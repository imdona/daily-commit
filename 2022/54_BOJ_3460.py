# 3460 이진수 : https://www.acmicpc.net/problem/3460
# case 1 : 메모리 KB / 시간 ms
T = int(input())

# 내장함수인 bin()을 활용하여 이진수로 바꾸는 방법 활용
for _ in range(T):
    bnum = bin(int(input()))[2:]  # 0b 제거 / string type
    for i in range(len(bnum)):
        if bnum[-i -1] == '1':
            print(i, end = ' ')

# -------------------------------------------------------------
# case 2 : 메모리 KB / 시간 ms
# 이진수로 만드는 함수 정의
# def change_num(num):