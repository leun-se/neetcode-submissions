class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all non-alphanumeric characters
        # create two pointers one at the start and end
        # compare the values at each pointer until l pointer is > r pointer
        # if at any point s[l] != r[l] return False
        # can also iterate past non-alphnumeric characters until both l and r are alphanumeric

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
            
    def alphanum(self, c):
        # if c is between
        # ASCII values of 
        # 0-9
        # A-Z
        # a-z
        # use ord function
        return (ord('0') <= ord(c) <= ord('9') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z'))