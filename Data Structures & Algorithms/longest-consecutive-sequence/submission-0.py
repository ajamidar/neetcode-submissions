class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1 = set(nums)
        longest = 0
        
        for num in s1:
            if (num - 1) not in s1:
                length = 1
                while (num + length) in s1:
                    length += 1
                longest = max(length, longest)
        
        return longest
        