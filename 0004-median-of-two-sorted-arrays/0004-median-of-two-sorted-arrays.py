class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array (binary search on the shorter one)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2          # number of elements on the left side of the partition

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2                 # cut in nums1
            j = total_left - i                 # corresponding cut in nums2

            nums1_left  = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right = float('inf')  if i == m else nums1[i]
            nums2_left  = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right = float('inf')  if j == n else nums2[j]

            # Correct partition found
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2:                # odd length → median is max of left side
                    return max(nums1_left, nums2_left)
                else:                          # even length → average of two middle values
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0

            # nums1 cut is too far right → move left
            elif nums1_left > nums2_right:
                hi = i - 1
            # nums1 cut is too far left → move right
            else:
                lo = i + 1

        # Problem guarantees at least one solution, this should never be reached
        raise ValueError("Input arrays are not valid")
