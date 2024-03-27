# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre    


    def reverseList(self, head: ListNode) -> ListNode:

        newNode = None
        curNode = head
        while curNode is not None:
            print(curNode.val)
            newNode = ListNode(curNode.val, newNode)
            curNode = curNode.next

        while newNode is not None:
            print(newNode.val)
            newNode = newNode.next

        return newNode

    def createListNode(self) -> ListNode:     
        n1 = ListNode(1)
        n2 = ListNode(2, n1)
        n3 = ListNode(3, n2)
        n4 = ListNode(4, n3)
        n5 = ListNode(5, n4)
        n6 = ListNode(6, n5)
        curNode = n6
        while curNode is not None:
            curNode = curNode.next

        return n6    
    
s = Solution()  
s.reverseList(s.createListNode())  