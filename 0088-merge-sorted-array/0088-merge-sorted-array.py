class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n==0:
            return nums1
        elif m==0:
            for i in range(len(nums2)):
                nums1[i]=nums2[i]
            return nums1
        k=0
        
        for i in range(len(nums1)-len(nums2),len(nums1)):
            nums1[i]=nums2[k]
            k+=1
        return nums1.sort()
        