'''
백준 14627 [파닭파닭] - 이분탐색
문제 : https://www.acmicpc.net/problem/14627
평소 요리에 관심이 많은 승균이는 치킨집을 개업하였다. 승균이네 치킨집은 파닭이 주메뉴다.
승균이는 가게를 오픈하기 전에 남부시장에 들러서 길이가 일정하지 않은 파를 여러 개 구매하였다.
승균이는 파닭의 일정한 맛을 유지하기 위해 각각의 파닭에 같은 양의 파를 넣는다.
또 파닭 맛은 파의 양에 따라 좌우된다고 생각하기 때문에 될 수 있는 한 파의 양을 최대한 많이 넣으려고 한다.
(하지만 하나의 파닭에는 하나 이상의 파가 들어가면 안 된다.)
힘든 하루를 마치고 승균이는 파닭을 만들고 남은 파를 라면에 넣어 먹으려고 한다. 이때 라면에 넣을 파의 양을 구하는 프로그램을 작성하시오.
승균이네 치킨집 자는 정수만 표현되기 때문에 정수의 크기로만 자를 수 있다.

[입력]
첫째 줄에 승균이가 시장에서 사 온 파의 개수 S(1≤S≤1,000,000), 그리고 주문받은 파닭의 수 C(1≤C≤1,000,000)가 입력된다. 파의 개수는 항상 파닭의 수를 넘지 않는다. (S≤C)
그 후, S 줄에 걸쳐 파의 길이 L(1≤L≤1,000,000,000)이 정수로 입력된다.

[출력]
승균이가 라면에 넣을 파의 양을 출력한다.
'''
import sys
green_onion, order_chicken = map(int, sys.stdin.readline().split())  # 파의 수, 주문받은 파닭의 수
onions = [int(sys.stdin.readline()) for _ in range(green_onion)]  # 파의 길이들 리스트

# 파의 최대 길이 구하기 by binary search
start = 1
end = max(onions)
length = 0

while start <= end:
    mid = (start + end) // 2

    chicken_count = 0
    for onion in onions:
        chicken_count += onion // mid

    if chicken_count < order_chicken:
        end = mid - 1
    else:
        start = mid + 1
        length = mid

print(sum(onions) - order_chicken*length)