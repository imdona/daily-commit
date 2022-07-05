
# 1931 [회의실 배정] : https://www.acmicpc.net/problem/1931
# case 1 : 메모리 53664KB / 시간 4272ms
# 회의시간 리스트안의 리스트로 입력받기 - 형식 : [회의시작, 회의끝]
meeting = []
for _ in range(int(input())):
    start, end = map(int, input().split())
    meeting.append([start, end])

# 끝나는시간 - 시작하는시간 오름차순으로 정렬
meeting.sort(key = lambda x: (x[1], x[0]))
# print(meeting)

# 회의개수 카운트
count = end = 0  # 종료시간 0으로 정의
for s, e in meeting:
    if s >= end:
        # 회의 시작시간 >= 이전 회의
        count += 1  # 회의 진행 카운트
        end = e  # 종료시간 재정의

print(count)




# -------------------------------------------------------------
# case 2 : 메모리 52400KB / 시간 4096ms
# short coding!!
meeting = sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x:(x[1], x[0]))

count = end = 0

for s, e in meeting:
    if s >= end:
        count += 1
        end = e

print(count)