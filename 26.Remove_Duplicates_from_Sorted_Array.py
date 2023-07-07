class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        size=len(nums)

        for i in range(1, size):
            if nums[i] != nums[i-1]:
                nums[k]=nums[i]
                k+=1

        return k
