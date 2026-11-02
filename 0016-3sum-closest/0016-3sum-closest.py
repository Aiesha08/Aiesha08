class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        diff=float('inf')
        nums.sort()
        ans=0
        

        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1

            while left<right:
                sum=nums[i]+nums[left]+nums[right]

                if abs(sum-target)<diff:
                    ans=sum
                diff=min(abs(target-sum),diff)

                if sum>target:
                    right-=1
                else :
                    left+=1
        return ans





        