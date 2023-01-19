#  Given two sorted arrays nums1 and nums2 of size m and n respectively,
#  return the median of the two sorted arrays.

#  The overall run time complexity should be O(log (m+n)).


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s1=len(nums1)
        s2=len(nums2)
        arr_size=s1+s2
        i=0, j=0, k=0
        nums3: List[int]
        while (i<s1||j<s2):
            if (nums1[i]<nums2[j]):
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
            k+=1

        while (i<s1):
            nums3.append(nums1[i])
            i+=1
            k+=1

        while (j<s1):
            nums3.append(nums1[j])
            j+=1
            k+=1
        while (i<s1):
            nums3.append(nums1[i])
            i+=1
            k+=1
        if arr_size%2==0:
            median_index=arr_size/2
            return nums3[median_index-1]+nums3[median_index]
        else:
            median_index=floor(arr_size/2)
            return nums3[median_index]
