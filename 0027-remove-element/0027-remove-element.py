class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n=len(nums)
        for n in nums[:]:
            if val==n:
                nums.remove(n)
        return len(nums)

        