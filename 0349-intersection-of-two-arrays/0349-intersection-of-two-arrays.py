class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=set(nums1)
        arr=[]

        for i in range(len(nums2)):
            if nums2[i] in seen:
                arr.append(nums2[i])
                seen.remove(nums2[i])
        return arr


