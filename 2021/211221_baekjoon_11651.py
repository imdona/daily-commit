'''
백준 11651 [좌표 정렬하기 2]
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000)
좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
'''
# 일단 간단하게 작동부터 하도록 만들어보기
N = int(input())
coordinate_list = []

for i in range(N):
    x, y = map(int, input().split())
    coordinate_list.append((x, y))

# y좌표 먼저 -> x좌표 정렬
coordinate_list.sort(key = lambda x: (x[1], x[0]))

for i in coordinate_list:
    print(i[0], i[1])

################################################################
# stdin으로 풀어보기

from sys import stdin

coordinate_list = [stdin.readline() for _ in range(int(stdin.readline()))]

coordinate_list.sort(key=lambda x: (int(x.split()[1]), int(x.split()[0])))

for i in coordinate_list:
    print(i[0], i[1])

# print 같은 표현
print(''.join(coordinate_list))

"""
[🔍 join 함수]
- 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환해주는 함수!

📎 ''.join(리스트)
''.join(리스트)를 이용하면 매개변수로 들어온 리스트를 문자열로 합쳐서 리턴해준다
ex) ['a', 'b', 'c'] 라는 리스트를 'abc'로 반환해준다!

문제에서 정렬된 coordinate_list를 문자열로 반환해준다.
1) print(coordinate_list)
    -> ['1 -1\n', '1 2\n', '2 2\n', '3 3\n', '0 4\n']

2) print(''.join(coordinate_list))
    ->  1 -1
        1 2
        2 2
        3 3
        0 4
"""

