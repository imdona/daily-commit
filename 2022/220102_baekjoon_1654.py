import sys
K, N = map(int, sys.stdin.readline().split())
lan_list = [int(sys.stdin.readline()) for _ in range(K)]
# print("랜선 리스트 : ", lan_list)

# 전체 길이에서 랜선을 자르고 남은 길이는 재사용할 수 없기 때문에 sum // N
low, high = 1, sum(lan_list)//N
# low, high = 1, max(lan_list)

while low <= high:
    # mid = 어떤 크기로 자를 것인지
    mid = (low + high) // 2

    # mid의 크기로 랜선을 자른 개수
    count = 0
    for i in lan_list:
        count += i // mid

    # 랜선 개수 >= N이면, mid보다 더 큰 단위로 잘라서 개수를 줄여도 된다
    if count >= N:
        low = mid + 1
    # 랜선개수 < N이면, mid보다 더 작은 단위로 잘라서 개수를 늘려야 한다.
    else:
        high = mid - 1

# 최대 길이 출력
print(high)
