H, W = map(int, input().split())
buildings = list(map(int, input().split()))

def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 제일 마지막 인덱스는 빼고 반복문을 돈다
    for i in range(1, len(buildings) - 1):
        # 물이 안차기때문에 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i]) #  현재 인덱스의 왼쪽에서 가장 높은 건물의 높이
        max_right = max(buildings[i:]) # 현재 인덱스의 오른쪽에서 가장 높은 건물의 높이

        # 현재 인덱스에 빗물이 담길 수 있는 높이 : 그 중 더 낮은 건물의 높이
        upper_bound = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 상한 높이에서 현재 인덱스에 있는 건물의 높이를 빼서 물의 높이를 구하고 total에 더해준다
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height

print(trapping_rain(buildings))


'''sys를 이용해서 input 입력 받을 때(2)'''
import sys
H, W = map(int, sys.stdin.readline().split())
buildings = list(map(int, sys.stdin.readline().split()))