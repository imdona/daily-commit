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
'''

# 초안 - 문제 이해가 잘 안감
class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = len(height) - 1
        for i in height:
            max_area = width * 