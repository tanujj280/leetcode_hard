import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    
    # Push the head of each list into the heap so the minimum stay at the top
    for idx, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, idx, node))
    
    dummy = ListNode(-1)
    curr = dummy
    
    while heap:
        val, idx, node = heapq.heappop(heap) #pehle sabse chota element nikala fir uska next element 
        # ko head banake doobara daal diya so now some other will be minimum
        curr.next = node
        curr = node
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    
    return dummy.next