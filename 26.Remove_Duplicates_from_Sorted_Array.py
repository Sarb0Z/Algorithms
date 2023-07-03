class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_list=set()

        for item in nums:
            unique_list.add(item)
        k=len(unique_list)
        unique_list=list(unique_list)
        for i in range(0, k):
            nums[i]=unique_list[i]
        
        return k
