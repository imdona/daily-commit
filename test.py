N = int(input())  # 개수
cord = list(map(int, input().split()))  # 좌표 입력받기

# 중복 제거 후 정렬
new_cord = sorted(list(set(cord)))

# 정렬 값 key - index 번호 값인 dict 만들기
result = {}
for i in range(len(new_cord)):
    result[new_cord[i]] = i

for i in cord:
    print(result[i], end = ' ')