#my solution to problem 2 on leetcode
#adding two numbers and returns in a list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = []
        r=0
        while (l1 is not None or l2 is not None or r!=0):
            if l1 is not None:
                n1=l1.val
                l1=l1.next
            else:
                n1=0
            if l2 is not None:
                n2=l2.val
                l2=l2.next
            else:
                n2=0
            s = n1+n2+r
            if s>=10:
                r=1
                answer.append(s-10)
            else:
                r=0
                answer.append(s)
        return answer
        
