#My Solution to problem 1 on leetcode.com
#two sums
#I tried brute forcing on my first attempt but was given time limit exceeded
#Tried using dictionaries instead 

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,j in enumerate(nums):
            if j in d.keys():
                return [d[j],i]
            else:
                d[target-j] = i
