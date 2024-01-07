from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Potential improvement: use a linkedlist instead of a list here
    # Here I have the ref to the node so inserting is O(1)
    def insert(self, lists, element):
        index = 0
        while index < len(lists) and element.val > lists[index].val:
            index += 1

        lists.insert(index, element)

    def list_update(self, lists):
        lists[0] = lists[0].next
        if not lists[0]:
            lists.pop(0)
        else:
            el = lists[0]
            lists.pop(0)
            self.insert(lists, el)

    def rev(self, linked_list):
        if not linked_list:
            return None
        rev_list = ListNode(linked_list.val)
        linked_list = linked_list.next
        while linked_list:
            rev_list = ListNode(linked_list.val, rev_list)
            linked_list = linked_list.next
        return rev_list

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [el for el in lists if el]
        lists = sorted(lists, key=lambda x: x.val)

        # Initialization
        if not lists:
            return None
        merged = ListNode(lists[0].val)
        self.list_update(lists)

        while lists:
            merged = ListNode(lists[0].val, next=merged)
            self.list_update(lists)

        return self.rev(merged)