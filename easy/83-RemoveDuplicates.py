class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
mylist = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3)))))

def deleteDuplicates(head):
        dummy = ListNode(val=head.val)
        current = dummy
        while head:
            if head.val != current.val:
                current.next = ListNode(val=head.val)
                current = current.next
            head = head.next
        return dummy

print(deleteDuplicates(mylist))