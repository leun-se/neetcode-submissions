class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Create 2 pointers
        # one at start one at end
        # do target - val at first pointer
        # if that value is less than the val at 2nd pointer, decrement 2nd pointer
        # if it's greater increment first pointer
        # if that value is equal, return index of first and last
        # potential issues?

        pt1,pt2 = 0, len(numbers) - 1
        while pt1 < pt2:
            if (target - numbers[pt1] < numbers[pt2]):
                pt2 -= 1
            elif (target -numbers[pt1] > numbers[pt2]):
                pt1 += 1
            else:
                return [pt1+1, pt2+1]
        return []