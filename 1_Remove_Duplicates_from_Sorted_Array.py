"""

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. More formally, 
if there are k elements after removing the duplicates, then the first k elements of 
nums should hold the final result. It does not matter what you leave beyond the 
first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying 
the input array in-place with O(1) extra memory.

"""
# a pointer to keep track of current index
# a pointer that goes ahead when next value is same
# if values pointed are different
# current index + 1 is value pointed by unique
# increment current
# repeat  
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cptr=0
        uptr=0
        while (uptr<len(nums)):
            if (nums[cptr]==nums[uptr]):
                uptr=uptr+1
            else:
                cptr=cptr+1
                if (cptr!=uptr):
                    nums[cptr]=nums[uptr]        
        {1,2,3,3,3,4,4,5}
        return cptr
            

