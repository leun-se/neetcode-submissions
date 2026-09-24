class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, r ,mid
        # if only l, mid in same sorted segment, l, mid are both rotated
        # move l pointer to mid + 1 and recalc mid
        # if mid and r are in the same sorted segment, l is rotated but mid isn't
        # move l pointer to mid
        # keep going until they are all in the same sorted segment
        # return l
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if (nums[l] <= nums[mid] <= nums[r]):
                return nums[l]
            elif (nums[l] <= nums[mid]):
                l = mid + 1
            else:
                r = mid
        return nums[l]


        