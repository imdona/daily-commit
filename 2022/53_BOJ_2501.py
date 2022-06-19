# 2501 약수 구하기 : https://www.acmicpc.net/problem/2501
# case 1 : 메모리 30848KB / 시간 68ms
N, K = map(int, input().split())
divisor_list = []  # 약수 리스트

for i in range(1, N+1):
    if N % i == 0:
        divisor_list.append(i)

if len(divisor_list) >= K:
    print(divisor_list[K-1])
else:
    print(0)

# print(divisor_list)
# print(divisor_list[K-1])


# -------------------------------------------------------------
# case 2 : 메모리 29056KB / 시간 56ms
N, K = map(int, input().split())
divisor_list = [i for i in range(1, N+1) if N % i == 0]
print(0 if len(divisor_list) < K else divisor_list[K-1])