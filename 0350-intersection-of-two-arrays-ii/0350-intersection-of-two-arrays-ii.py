class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        arr = []

        for num in nums2:
            # If the number is available in our count budget
            if counts[num] > 0:
                arr.append(num)
                counts[num] -= 1  # Reduce the budget by one
                
        return arr
        