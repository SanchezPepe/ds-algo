import sys
sys.path.append('/home/user/ds-algo/Classes')
import LinkedList

# TC = O(n) - We only traverse the list once
# SC = O(1) - We only need three pointers to keep track of the nodes
def reverseLL(list):
    prev = list.head
    current = list.head.next
    prev.next = None

    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    
    list.head = prev
    return list

mll = LinkedList.LinkedList()
for i in range(10):
    mll.append(i)

mll.print()
reverseLL(mll)
mll.print()

