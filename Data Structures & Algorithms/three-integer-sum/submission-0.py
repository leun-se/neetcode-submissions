class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Triplets that equal 0:
        # if 2 nums sum to 0 and 3 is 0
        # or 2 nums sum to x and 3 is -x
        # or 2 nums sum to -x and 3 is x

        # sort array
        # iterate through each val using index i
        # have 2 pointers j and k, j is i+1, k is len(nums)-1
        # nums[j]+nums[k] should = nums[i]
        # use 2sum 2 logic to decrement/increment, but also keep incrementing/decrementing if values are the same
        # if a pair works add it to answer set and keep going till j > k

        res = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            j, k = i + 1, n - 1
            while j < k:
                s = nums[j] + nums[k]
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res
        