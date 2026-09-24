class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, l = 0, len(nums)-1

        while (s <= l):
            i = (l + s) // 2 
            if (nums[i]) > target:
                l = i - 1
            elif (nums[i]) < target:
                s = i + 1
            else:
                return i
        return -1