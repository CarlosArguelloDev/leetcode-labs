class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:
            res = carry
            if l1: 
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            
            carry = res // 10
            current.next = ListNode(res % 10)
            current = current.next

        return dummy.next

