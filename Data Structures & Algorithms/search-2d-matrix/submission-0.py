class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start checks with the first values of each row
        # check if value is within the bounds of the first val of the current and next row, 
        # if so, do binary search on the row
        # else move on to the next row and try again
        for row in matrix:
            if (row[0] <= target <= row[-1]):
                return self.binarySearch(row, target)
        return False

    def binarySearch(self, nums: List[int], target: int):
            l, r = 0, len(nums) - 1
            while (l <= r):
                j = (l + r) // 2 
                if(nums[j] == target):
                    return True
                if(nums[j] > target):
                    r = j - 1
                if(nums[j] < target):
                    l = j + 1 
            return False
        