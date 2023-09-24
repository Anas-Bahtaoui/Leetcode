# define a class of ListNode

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
    
# test
list1 = ListNode(1)
list1.next = ListNode(4)

list2 = ListNode(3)
list2.next = ListNode(2)

list3 = mergeTwoLists(list1, list2)

while list3:
    print(list3.val)
    list3 = list3.next