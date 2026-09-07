class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            numcount=0
            for i in range(len(nums)):
                if nums[i] == num:
                    numcount += 1

                if numcount > 1:
                    return True
        
        return False