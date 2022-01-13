'''첫번째 풀이 - 시간초과'''
M, N = map(int, input().split())
prime_num = []
for i in range(M, N+1):
    condition = True
    if i == 1 : continue
    for j in range(2, i):
        if i % j == 0:
            condition = False
            break
    if condition:
        prime_num.append(i)
print(*prime_num, sep='\n')

'''두번째 풀이 - 혹시나해서 sys로 해봤지만, 동일하게 시간초과. for문을 고쳐야할 것 같다.'''
import sys
M, N = map(int, sys.stdin.readline().split())
prime_num = []
for i in range(M, N+1):
    condition = True
    if i == 1 : continue
    for j in range(2, i):
        if i % j == 0:
            condition = False
            break
    if condition:
        prime_num.append(i)
print(*prime_num, sep='\n')

'''세번째 풀이 - 에라토스테네스의 체 활용하기
시간을 줄이기 위해서 루트한 부분까지만 for 반복문'''
# 기존코드
import sys
M, N = map(int, sys.stdin.readline().split())
prime_num = []
for i in range(M, N+1):
    condition = True
    if i == 1 : continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            condition = False
            break
    if condition:
        prime_num.append(i)
print(*prime_num, sep='\n')

'''네번째 풀이 - 에라토스테네스의 체 활용하기
사용자정의함수 만들어서 풀이하기'''
import sys
M, N = map(int, sys.stdin.readline().split())

def check_prime(num):
    if num == 1: return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

for i in range(M, N + 1):
    if check_prime(i):
        print(i)





