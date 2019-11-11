

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    prev = None
    temp = head
    while temp:
        nextnode=temp.next
        temp.next=prev
        prev=temp
        temp=nextnode
    print(prev.data)
    return prev

