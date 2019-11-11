

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    new_node=SinglyLinkedListNode(data)
    if llist==None:
        llist = new_node
    else:
        new_node.next,llist = llist, new_node
    print(new_node.next)
    return llist
