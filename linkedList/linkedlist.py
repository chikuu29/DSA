
class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def createLinkedList(a):
    dummy=Node(0)
    current=dummy
    for i in a:
        current.next=Node(i)
        current=current.next
    return dummy.next



def addTwoLinkedList(l1,l2):
    result = Node(0)
    current=result
    carry=0
    while l1 or l2:
        val1=l1.val if l1 else 0
        val2 =l2.val if l2 else 0
        totalSum=val1 +val2+carry
        # print(val1)
        # print(val2)
        # print(carry)
        carry=totalSum // 10
        # print(totalSum//10)
        current.next=Node(totalSum%10)
        current=current.next
        l1=l1.next if l1 else None
        l2=l2.next if l2 else None
    return result.next




        


# Input lists
l1 = createLinkedList([2, 4, 3])
l2 = createLinkedList([5, 6, 4])


result=addTwoLinkedList(l1,l2)

def convertLinkedListToList(head):
    result=list()
    while head is not None:
        result.append(head.val)
        head=head.next
    return result

print("result",convertLinkedListToList(result))

# current = l1
# while current is not None:
#     print(current.val) 
#     current=current.next
    



    