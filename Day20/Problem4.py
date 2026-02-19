class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
         nums1_last_index = m - 1
         nums2_last_index = n - 1
         merge_position = m + n - 1
         while nums1_last_index >= 0 and nums2_last_index >= 0:
             if nums1[nums1_last_index] > nums2[nums2_last_index]:
                 nums1[merge_position] = nums1[nums1_last_index]
                 nums1_last_index -= 1
             else:
                 nums1[merge_position] = nums2[nums2_last_index]
                 nums2_last_index -= 1
             merge_position -= 1
         while nums2_last_index >= 0:
             nums1[merge_position] = nums2[nums2_last_index]
             nums2_last_index -= 1
             merge_position -= 1
        