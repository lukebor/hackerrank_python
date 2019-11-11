

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    cur=head
    print(new_node.data)

    for _ in  range(position-1):
        cur=cur.next
        cur_next=cur.next
    cur.next,new_node.next=new_node, cur_next
    return head
    
