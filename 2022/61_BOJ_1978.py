# 1078 [소수 찾기] : https://www.acmicpc.net/problem/1978
# case 1 : 메모리 30840KB / 시간 68ms
N = int(input())
nums = list(map(int, input().split()))

def check_prime(n):
    '''소수를 확인하는 함수'''
    if n == 1:
        return False  # 1은 소수가 아님
    else:
        # for문 도는 범위 루트로 줄여주기
        for i in range(2, int(n**0.5) + 1):
            # 0으로 나누어떨어지는 수가 있으면 소수 X
            if n % i == 0: return False
        # for문을 다 돌고 나오면(0으로 나누어지는 수가 없으므로) 소수 O
        return True

result = 0

for n in nums:
    result += int(check_prime(n))  # True : 1 / False : 0

print(result)


# -------------------------------------------------------------
# case 2 : 메모리 30840KB / 시간 68ms
n = int(input())
nums = list(map(int,input().split()))
cnt = 0

for i in nums:
    # 바로 하나씩 확인
    cond = True
    if i <= 1: continue  # 1보다 작으면 소수x
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            cond = False  # 0으로 나누어 떨어지면 소수x
            break
    # 정상적으로 반복문 나오면 count + 1
    if cond:
        cnt += 1

print(cnt)