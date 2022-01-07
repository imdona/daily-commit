def consecutive_sum(start, end):
    # base case : start와 end가 같을 때 예를 들어, 1에서 1까지의 합이라면 1을 리턴!
    if end == start:
        return start

    # Divide : 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다
    mid = (start + end) // 2

    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine)
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))

# 답
55
5050
32131
75466