class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=list()
        i=0
        while(i<k):
            arr.append(nums[len(nums)-i])
            i=i+1
        i=k
        count=0
        while (i<len(nums)):
            nums[len(nums)-count]=nums[i]
            i=i+1
            count=count+1
        i=0
        while(i<k):
            nums[i]=arr[i]

        