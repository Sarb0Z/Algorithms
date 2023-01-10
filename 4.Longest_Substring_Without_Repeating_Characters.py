#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest=0
        index=0        
        for current in s:
            count=1
            while (index+count<len(s)):
                if s[index+count]==current:
                    break
                if count>largest:
                    largest=count
                count=count+1
            index=index+1
        return largest

        

            


        
