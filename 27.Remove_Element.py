class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        arr_len=len(nums)
        count=0
        i=0
        if arr_len == 0:
                return i
        if arr_len == 1:
            if nums[i] == val:
…
