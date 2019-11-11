

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if head == None:
        return SinglyLinkedListNode(data)
    curr_node = head
    while curr_node.next != None:
        curr_node = curr_node.next
    curr_node.next = SinglyLinkedListNode(data)
    return head
    
