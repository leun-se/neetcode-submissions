class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort array
        # have cur = nums[i] len = 1
        # check next value, if nums[i] == cur cur = nums[i] , of nums[i] = cur+1 len++ cur = nums[i]
        # else, max = len if len > max len = 1, cur = nums[i]
        # return max
        if len(nums) == 0:
            return 0
            
        nums.sort()
        cur = nums[0]
        max_len = 0
        length = 1

        for i in range(1, len(nums)):
            if (nums[i] == cur):
                continue
            elif (nums[i] == cur + 1):
                length += 1
            else:
                max_len = max(max_len, length)
                length = 1
            cur = nums[i]

        max_len = max(max_len, length)
        return max_len