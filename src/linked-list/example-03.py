# LeetCode #2: Add Two Numbers

from utils import create_linked_list, print_linked_list, ListNode

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # 建立虛擬頭節點
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    # 當還有節點需要處理時繼續
    while l1 or l2 or carry:
        # 取得當前節點的值，如果節點為空則為0
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        # 計算總和與進位
        total = x + y + carry
        carry = total // 10
        
        # 創建新節點存放結果
        current.next = ListNode(total % 10)
        current = current.next
        
        # 移動到下一個節點
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

# test
l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])
print(print_linked_list(addTwoNumbers(l1, l2)))


# 1. 整體思路過程

# 1.1 分析題目
# 輸入是兩個 LinkedList，每個節點存放一個 0-9 的數字
# 數字是反向存放的（個位數在前）
# 需要考慮進位情況
# 兩個輸入串列長度可能不同
# 結果也需要用 LinkedList 返回

# 1.2 破解關鍵/重點
# 反向儲存是優勢：
# 加法本來就是從個位數開始計算
# 不需要反轉串列就可以直接計算
# 進位處理：
# 需要一個變數記錄進位值
# 每次計算時要考慮：當前兩節點值 + 上次的進位值
# 邊界處理：
# 當其中一個串列結束時，繼續處理另一個串列
# 最後還要檢查是否有進位需要增加新節點

# 1.3 程式碼轉換思路
# 建立虛擬頭節點（dummy node）方便操作
# 同時遍歷兩個串列，處理：
# 兩個當前節點的值
# 上一次的進位值
# 建立新節點存放計算結果
# 處理剩餘節點和最後可能的進位

# 2. 資料結構選擇的 Trade-offs
# LinkedList 解法
# 優點：
# 符合題目輸入輸出格式
# 空間複雜度是 O(max(N,M))，只需要存放結果
# 可以直接按位處理，不需要轉換格式
# 缺點：
# 需要處理較多指針操作
# 需要特別處理串列長度不同的情況

# Array 解法
# 優點：
# 實作較簡單，不需要處理指針
# 存取元素更直接
# 缺點：
# 需要先轉換格式
# 可能需要額外空間來存儲中間結果
# 最後還需要轉回 LinkedList 格式

# Stack 解法
# 優點：
# 符合從個位數開始處理的特性
# 處理進位方便
# 缺點：
# 需要額外空間存儲中間結果
# 多了一步轉換過程