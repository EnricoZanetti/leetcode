class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        index = mid
                    right = mid - 1
            return index

        def find_right():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[mid] == target:
                        index = mid
                    left = mid + 1
            return index

        return [find_left(), find_right()]
