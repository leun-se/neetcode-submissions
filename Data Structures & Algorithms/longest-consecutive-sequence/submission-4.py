class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert array into a set
        # iterate through each number
        # check if then number-1 exists in set, if not then it is the start of a sequence
        # check if the number+1 exists in set, if not then go to next sequence
        # if number isn't start of sequence, go next
        numSet = set(nums)
        longest, length = 0, 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length+=1
                longest = max(length, longest)
        
        return longest
