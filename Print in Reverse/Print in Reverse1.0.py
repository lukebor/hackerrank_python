

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    rev=[]
    while head:
        rev.append(head.data)
        head=head.next
    for i in range (len(rev)-1,-1,-1):
        print(rev[i])
