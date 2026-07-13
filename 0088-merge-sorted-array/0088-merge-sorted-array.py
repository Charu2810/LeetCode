class Solution(object):
    def merge(self, nums1, m, nums2, n):
        new_arr=nums1[:m]+ nums2[:n]
        new_arr.sort()
        nums1[:]=new_arr
        