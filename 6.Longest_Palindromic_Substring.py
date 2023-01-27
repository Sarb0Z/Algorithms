
# Given a string s, return the longest palindromic substring in s.
"""Algorithm"""
    # at each point of the string, we will simultaneously go forward and back
    # until we reach the end or beginning of string or the characters at both 
    # indexes are not the same
    # if at this point, the radius is greater than previous, we will replace
    # the previous substring with this one
    # pivot will center on character for odd palindrome and between characters
    # for even palindrome 
        
def longestPalindrome(self, s: str) -> str:
    if len(s) < 2:
        return s
    pivot=0
    radius=0
    subStr=""
