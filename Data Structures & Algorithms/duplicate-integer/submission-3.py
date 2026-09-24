class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set = []
        for n in nums:
            if n in set:
                return True
            else:
                set.append(n)
        return False