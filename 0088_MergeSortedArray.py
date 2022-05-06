class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2[:n])):
            nums1[m+i] = nums2[i]
        for i in range(1, len(nums1)):
            key = nums1[i]
            j = i-1
            while j >=0 and key < nums1[j] :
                nums1[j+1] = nums1[j]
                j -= 1
            nums1[j+1] = key 
        return nums1