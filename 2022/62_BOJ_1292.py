# 1292 [쉽게 푸는 문제] : https://www.acmicpc.net/problem/1292
# case 1 : 메모리 30840KB / 시간 68ms
# 수열 개수 1000개 넘는 n값 구하기
# n = 1
# while n**2 - n - 2000 < 0:
#     n += 1
# print(n)  # n = 46

# 수열 리스트로 만들기
arr = []
for i in range(1, 47):
    for _ in range(i):
        arr.append(i)
# print(arr)  # 확인

start, end = map(int, input().split())
total = 0

for j in range(start-1, end):
    # index는 0부터 시작하니까
    total += arr[j]

print(total)


# -------------------------------------------------------------
# case 2 : 메모리 29284KB / 시간 52ms
# 더 간단하게 코드 작성하기!
arr = []
for i in range(1, 46):
    arr += [i] * i

start, end = map(int, input().split())
print(sum(arr[start-1 : end]))