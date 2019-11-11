

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):

    s = SinglyLinkedList()
    c = s
    while head1 and head2:
        if head1.data > head2.data:
            s.next = head2
            head2 = head2.next
        else:
            s.next = head1
            head1 = head1.next
        s = s.next
    s.next = head1 or head2
    return c.next

