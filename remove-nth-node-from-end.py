"""
Problem: Remove Nth Node From End of List
Approach: Two-pass length calculation
Time: O(n)
Space: O(1)
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        
        
        temp, curr = head, head
        i = 0
        while(temp != None):
            temp = temp.next
            i += 1

        a = i - n + 1
        
        if a == 1:
            head = head.next 
            return head
        

        for j in range(a - 2):
            curr = curr.next 
            print(j)

        curr.next = curr.next.next
        return head
