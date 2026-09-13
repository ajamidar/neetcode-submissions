class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        prefix = 1
        for i in nums:
            output.append(prefix)
            prefix *= i

        postfix = 1
        length = len(output) - 1
        for i in nums[::-1]:
            output[length] *= postfix
            postfix *= i
            length -= 1
        
        return output        