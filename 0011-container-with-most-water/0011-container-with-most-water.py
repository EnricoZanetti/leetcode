class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        if n < 2:
            return 0
        
        left = 0
        right = n - 1
        areas = []

        while left < right:
            h = min(height[left], height[right])
            b = right - left
            area = b * h
            areas.append(area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max(areas)
