# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(val=2, next=ListNode(val=5, next=ListNode(val=6)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))

def mergeTwoLists(list1, list2):
    output = ListNode()
    current = output
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        
    current.next = list1 if list1 else list2
    
    return output.next

print(mergeTwoLists(list1, list2))