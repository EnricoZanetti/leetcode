class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        merged_array = nums1 + nums2
        sorted_array = sorted(merged_array)

        len_array = len(sorted_array)

        if len_array % 2 == 0:
            num1 = sorted_array[(len_array // 2) - 1]
            num2 = sorted_array[len_array // 2]
            return (num1 + num2) / 2
        else:
            return sorted_array[len_array // 2]