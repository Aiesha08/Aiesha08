class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        ans=0

        while left < right:
            sum=nums[left]+nums[right]
            ans=max(ans,sum)
            left=left+1
            right=right-1
        return ans
        