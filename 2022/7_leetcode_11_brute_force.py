'''
leetcode [11. Container With Most Water] - Brute-force search
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two rightpoints of the line i is at (i, ai) and (i, 0).
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

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''높이 left, right, 넓이 area 정의'''
        left = 0
        area = 0
        right = len(height) - 1

        while right > left:
            # 넓이 = 가로 * 세로
            temp = (right - left) * min(height[left], height[right])
            area = max(area, temp)

            if height[left] < height[right]:
                # 왼쪽 높이가 오른쪽 높이보다 짧을 때
                left += 1
            else:
                # 오른쪽 높이가 왼쪽 높이 보다 짧을 때
                right -= 1
        return area


# test
sol = Solution()
print(sol.maxArea([1,1]))
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))

