

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if position==0:
        return head.next
    temp=head
    for _ in range(position-1):
        temp=temp.next
        next_temp=temp.next

    temp.next=temp.next.next
    return head
