#my solution to problem 3 on leetcode
#

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        aInList=list(s)
        m=[]
        count=[]
        for i in aInList:
            if len(count)==0:
                count.append(i)
            elif i in count:
                if len(count) > len(m):
                    m=count
                a=count.index(i)
                count = count[a+1:]
                count.append(i)
            else:
                count.append(i)
        if len(count)>len(m):
            m=count
        return len(m)
