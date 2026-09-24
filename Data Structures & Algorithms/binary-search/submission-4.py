class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, l = 0, len(nums)-1

        while (s <= l):
            i = (l + s) // 2 
            if(nums[i] == target):
                return i
            if(nums[i] > target):
                l = i - 1
            if(nums[i] < target):
                s = i + 1
        return -1