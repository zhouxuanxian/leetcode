# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast is not None:
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                return None
                
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                print(slow.val)    
                return slow


    def detectCycle1(self, head: ListNode) -> ListNode:

        cur = head
        res = set()
        while cur is not None:
            if cur in res:
                print(cur.val)
                return cur
            else:
                res.add(cur)

            cur =  cur.next


        return None
    
    def createListNode(self) -> ListNode:     
        n1 = ListNode(1)
        n2 = ListNode(2, n1)
        n3 = ListNode(3, n2)
        n4 = ListNode(4, n3)
        n5 = ListNode(5, n4)
        n6 = ListNode(6, n5)
        n1.next = n4
        # curNode = n6
        # while curNode is not None:
        #     print(curNode.val)
        #     curNode = curNode.next

        return n6    
    
s = Solution()  
head = s.createListNode()
s.detectCycle(head)