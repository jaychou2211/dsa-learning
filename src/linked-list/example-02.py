# LeetCode #21: Merge Two Sorted Lists

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://imgur.com/Jjdqi1x
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 建立虛擬頭節點
        dummy = ListNode(0)
        prev = dummy
        
        # 當兩個串列都還有節點時
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        # 處理剩餘節點
        prev.next = list1 if list1 else list2
        
        return dummy.next

# 時間複雜度：O(n + m)，其中 n 和 m 是兩個串列的長度
# 空間複雜度：O(1)，只使用固定的額外空間


# 測試用例
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    values = []
    curr = head
    while curr:
        values.append(str(curr.val))
        curr = curr.next
    return "->".join(values)

# 測試
test_cases = [
    ([1,2,3,4,5], [1,3,4,5]),
    ([1], []),
    ([], [1,3,4,5]),
]

for list1, list2 in test_cases:
    linked_list1 = create_linked_list(list1)
    linked_list2 = create_linked_list(list2)
    merged_list = Solution().mergeTwoLists(linked_list1, linked_list2)
    print(print_linked_list(merged_list))