class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean string
        # create 2 pointers one for start one for end
        # iterate till they pass each other
        # at each step check if they are equal
        s = ''.join(c for c in s.lower() if c.isalnum())
        i, j = 0, len(s)-1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
        
