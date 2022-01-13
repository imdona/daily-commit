'''
leetcode [11. Container With Most Water]
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.

[korean]
음이 아닌 정수 a1, a2, ..., an n이 주어지면 여기서 각각은 좌표 (i, ai)의 점을 나타냅니다.
선 i의 두 끝점이 (i, ai)와 (i, 0)에 있도록 n개의 수직선을 그립니다.
컨테이너에 가장 많은 물이 포함되도록 x축과 함께 컨테이너를 형성하는 두 개의 선을 찾으십시오.
용기를 기울이면 안 됩니다.

[problem url]
https://leetcode.com/problems/container-with-most-water/

[Example]
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        total = 0

        for i in range(1, len(height) - 1):
            max_left = max(height[:i])
            max_right = max(height[i:])

            upper_bound = min(max_left, max_right)

            total += max(0, upper_bound - height[i])

        return total



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

