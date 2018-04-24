#my solution to problem 4 on leetcode
#merges the two array in a binary sort type fashion
#finds the middle value
#uses more memory but completes task in O(min(len(nums1,nums2))

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a=[]
        while True:
            if nums1==[]:
                a=a+nums2
                break
            elif nums2==[]:
                a=a+nums1
                break
            else:
                if nums1[0]<nums2[0]:
                    a.append(nums1[0])
                    nums1.pop(0)
                else:
                    a.append(nums2[0])
                    nums2.pop(0)
        if len(a)%2==0:
            return (a[int(len(a)/2)]+a[int(len(a)/2-1)])/2
        else:
            return a[int(len(a)/2)]
