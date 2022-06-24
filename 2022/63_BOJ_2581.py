# 2581 [소수] : https://www.acmicpc.net/problem/2581
# case 1 : 메모리 30840	KB / 시간 84ms
start = int(input())  # 시작하는 수
end = int(input())  # 끝나는 수
primes = []  # 소수 들을 담을 리스트

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

for j in range(start, end + 1):
    if check_prime(j) == True: primes.append(j)

# print(primes)  # check

if primes:
    # 소수가 있을 때
    print(sum(primes))
    print(min(primes))
else:
    # 소수가 없을 때
    print(-1)


# -------------------------------------------------------------
# case 2 : 메모리 30840KB / 시간 76ms
# 소수 리스트 숏코딩으로 구현 (메모리는 동일, 시간 조금 더 빠름)
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

start = int(input())  # 시작하는 수
end = int(input())  # 끝나는 수

# 소수리스트
primes = [p for p in range(start, end + 1) if check_prime(p) == True]

# print(primes)  # check

if primes:
    # 소수가 있을 때
    print(sum(primes))
    print(min(primes))
else:
    # 소수가 없을 때
    print(-1)



# -------------------------------------------------------------
# case 3 : 메모리 29056KB / 시간 60ms
# best sol 참고
# 10000이하의 자연수에 대한 소수 확인 테이블 생성
arr = [False, False] + [True] * 9999

for i in range(2, 101):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False

start = int(input())
end = int(input())
nums = [i for i in range(start, end + 1) if arr[i]]

print(sum(nums)if len(nums) else -1)
print(min(nums) if len(nums) else '')