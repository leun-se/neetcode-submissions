class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if (row[0] <= target <= row[-1]):
                l, r = 0, len(row) - 1
                while (l <= r):
                    j = (l + r) // 2 
                    if(row[j] == target):
                        return True
                    if(row[j] > target):
                        r = j - 1
                    if(row[j] < target):
                        l = j + 1 
                return False
        return False

