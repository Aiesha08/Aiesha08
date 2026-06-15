class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        left=0
        ans=float(inf)

        for right in range(len(nums)):
            sum=sum+nums[right]

            while sum>=target:
                print(right-left+1)
                ans=min(ans,right-left+1)
                sum-=nums[left]
                left=left+1
            
        if ans==float(inf):
            return 0
        else :
            return ans

        