'''
백준 11650 [좌표 정렬하기] - silver 5
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.(-100,000 ≤ xi, yi ≤ 100,000)
좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
'''
'''x좌표 오름차순 -> y좌표 오름차순으로 정리!
list = [(x, y), ... ] -> 형태로 들어있으면 x 정렬 -> y 정렬 순으로 정렬이 된다! '''
N = int(input())
coordinate_list = []

for i in range(N):
    x, y = map(int, input().split())
    coordinate_list.append((x, y))

coordinate_list.sort()

for i in coordinate_list:
    print(i[0], i[1])


## 숏코딩! 한 줄에 완성 가능
[print(*i) for i in sorted([list(map(int, input().split())) for _ in range(int(input()))])]


## 조금만 더 이해하기 쉽게 풀어서 쓰면 아래와 같다!
x = [list(map(int, input().split())) for _ in range(int(input()))]
for i in sorted(x):
    print(*i)

'''짚고 넘어갈 개념 : *
컨테이너 타입의 데이터를 Unpacking 할 때 *를 사용해주자!

print(test_list)
# [2, 3]

print(*test_list)
# 2 3
'''