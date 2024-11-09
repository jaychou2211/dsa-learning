# # LeetCode 206: Reverse Linked List

# ## 1. 整體思路過程

# ### 1.1 題目分析
# 給定一個單向鏈表的頭節點 head，將整個鏈表反轉並返回新的頭節點。

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# ### 1.2 解題關鍵重點
# 1. 需要同時掌握三個節點：
#    - 當前節點 (curr)
#    - 前一個節點 (prev)
#    - 下一個節點 (next)

# 2. 主要步驟：
#    - 保存下一個節點
#    - 改變當前節點的指向
#    - 移動指針
   
# 3. 邊界情況：
#    - 空鏈表
#    - 只有一個節點的鏈表

# ### 1.3 解題步驟轉換成程式邏輯
# 1. 初始化三個指針：prev = None, curr = head
# 2. 遍歷鏈表：
#    - 保存 next = curr.next
#    - 反轉指針 curr.next = prev
#    - 移動 prev = curr
#    - 移動 curr = next
# 3. 返回新的頭節點（prev）

# ## 2. 解法選擇的 Trade-offs

# ### 方法一：迭代（Iterative）
# 優點：
# - 空間複雜度為 O(1)，只需要幾個指針
# - 直觀易懂
# - 實作簡單

# 缺點：
# - 需要維護多個指針，容易出錯
# - 代碼不如遞迴優雅

# ### 方法二：遞迴（Recursive）
# 優點：
# - 程式碼更簡潔優雅
# - 解題思路更符合函數式編程思維

# 缺點：
# - 空間複雜度為 O(n)，因為遞迴調用堆疊
# - 對大型鏈表可能導致堆疊溢出
# - 理解起來較困難

## 3. Python 實作
# Definition for singly-linked list.
from utils import create_linked_list, print_linked_list

# 方法一：迭代
# https://i.imgur.com/bICVnHy.jpeg
def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        # 保存下一個 node
        next_temp = curr.next
        # 把當前 node 的 pointer 逆著指
        curr.next = prev
        # 把追蹤 node 用的 pointer 往後移
        prev = curr
        curr = next_temp
    
    return prev

# 方法二：遞迴
# https://i.imgur.com/qhJgAm7.jpeg
def reverseList_recursive(head):
    # 基本情況：空鏈表或只有一個節點
    if not head or not head.next:
        return head
    
    # 遞迴反轉子鏈表
    new_head = reverseList_recursive(head.next)
    
    # 改變指向
    (head.next).next = head
    head.next = None
    
    return new_head

# 測試
test_cases = [
    [1,2,3,4,5],
    [1],
    []
]

for case in test_cases:
    head = create_linked_list(case)
    print(f"Original: {print_linked_list(head)}")
    reversed_head = reverseList(create_linked_list(case))
    print(f"Reversed: {print_linked_list(reversed_head)}\n")