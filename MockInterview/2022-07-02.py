
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = 
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

"""
# [[none],[none],[none]]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# res = 1->1->2->3->4->4->5->6
# time: O(K*N)
# space: O(K*N)

# node.val
# node.next()

# extra space? res = node(),  
# min heap for each header of linked lists in lists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def k_linked_lists(self, lists: list[listNode]) -> listNode:
    






# O(kn)
# O(kn)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        
        heap = []
        # [[1,2,3],[2,4],[]]
        for list in lists:
            
            while list:
                heapq.heappush(heap, list.val)
                list = list.next
                
        
        init = ListNode(0)
  
        trail = init
        
        while heap:
            
            trail.next = ListNode(heappop(heap))
            
            trail = trail.next
        
        trail.next = None
        
        return init.next


# T: O(nlogk)
# S: O(1)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) < 1:
            return None
        
        while len(lists) > 1:
            
            merged_list = []
            
            for i in range(0, len(lists), 2):
                
                l1 = lists[i]
                l2 = lists[i+1] if i + 1  < len(lists) else None
                
                merged_list.append(self.mergeTwoLists(l1, l2))
                
            lists = merged_list
            
            
        return lists[0]
        
    def mergeTwoLists(self, l1, l2):
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

