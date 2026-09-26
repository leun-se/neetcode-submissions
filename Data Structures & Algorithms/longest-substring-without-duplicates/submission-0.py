class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start with l, r where l = 0, r = 0
        # create hashset
        # while s[r] is in hashset, remove s[l] and l += 1
        # otherwise, add s[r] to hashset
        # compute max(res, len of current substring) each time and store in res

        if len(s) == 0:
            return 0

        l, res = 0, 0
        hashset = set()

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            res = max(res, (r - l) + 1)
        
        return res

