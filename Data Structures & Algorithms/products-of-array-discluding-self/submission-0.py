class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        pref = 1
        for i in range(len(nums)):
            out[i] = pref
            pref = nums[i] * pref
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * post
            post = nums[i] * post
        
        return out
