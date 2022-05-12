'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

----

Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

'''


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #count length of linked list
        #set count implicitly to one (not zero this time)...
        count = 1
        
        #...because we count this declaration where last starts as the value of head #TODO if this doesn't work, set last = head.next or adjust count
        last = head
        
        #while last.next is not None (the indicative of the final node in the linked list)
        while last.next != None:
            
            #set last equal to the next node
            last = last.next
            
            #increment count by one
            count +=1
        
        #set a variable k back to be equal to count - (k-1) (k steps back from final entity, -1 counting the final node itself)
        k_back = count - (k-1)
        
        #set the value of hold to be that of head
        hold = head
        
        #set i to be one (one-indexed list)
        i = 1
        
        #declare empty nodes to hold swapping value
        swap_one = ListNode()
        swap_two = ListNode()
        
        #while not at the final node
        while i <= count:
            
            #if we have arrived at the first stop indicated by k
            if i == k:
                #set swap_one to be equivalent to the current node
                swap_one = hold
                
            #if we have arrived at the second stop indicated by k_back
            if i == k_back:
                #set swap_one to be equivalent to the current node
                swap_two = hold
                                
            #set hold to next node and continue traversal
            hold = hold.next
            
            #increment
            i+=1
            
        #reinitialize hold
        hold = ListNode()
        
        #and swap the values of the node
        hold.val = swap_one.val
        swap_one.val = swap_two.val
        swap_two.val = hold.val
        
        return head