# 11399 [ATM] : https://www.acmicpc.net/problem/11399
# case 1 : 메모리 30840KB / 시간 128ms
T = int(input())
people = sorted(list(map(int, input().split())))  # 오름차순 정렬
# print(people)

# 각각 사람별로 걸리는 시간 합계 구하기
result = 0
for i in range(T):
    for j in range(i + 1):
        result += people[j]
print(result)



# -------------------------------------------------------------
# case 2 : 메모리 30840KB / 시간 68ms
T = int(input())
people = sorted(list(map(int, input().split())))  # 오름차순 정렬

result = people[0]  # 초기값 정의

# 각각 사람별로 걸리는 시간 합계 구하기
for i in range(1, T):
    people[i] += people[i-1]
    result += people[i]

print(result)