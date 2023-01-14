#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest=0
        index=0        
        for current in s:
            count=1 #index for searching ahead in loop
            while ((index+count)<len(s)):
                if count>largest:
                    largest=count
                if s[index+count]==current:
                    break
                count=count+1
            index=index+1 #index of current pointer
        return largest