# LeetCode 347: Top K Frequent Elements

# 給定一個整數陣列 nums 和一個整數 k，回傳出現頻率最高的 k 個元素。
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

#  解題思路分析

# 1.1 題目分析
# 需求：找出陣列中出現次數最多的 k 個元素
# 輸入：整數陣列 nums 和整數 k
# 輸出：長度為 k 的陣列，包含前 k 個高頻元素
# 限制：
# 1 ≤ nums.length ≤ 10^5
# k的值合法（1 ≤ k ≤ 不重複數字的數量）
# 答案可以按任意順序返回

# 1.2 解題關鍵
# 需要統計每個元素出現的頻率 → Hash Table ⭐️
# 需要找出頻率最高的k個元素 → 排序或最小堆 ⭐️⭐️⭐️
# 時間複雜度需要優化，因為數據規模可達10^5 ⭐️⭐️

# 1.3 程式碼轉換思路
# 使用Counter或dict統計頻率
# 根據頻率排序
# 取前k個元素

from collections import Counter
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 計算每個元素出現頻率
        count = Counter(nums)
        
        # 2. 使用最小堆維護k個最大值
        heap = []
        for num, freq in count.items():
            # 如果堆的大小小於k，直接加入
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            # 否則，只有當前頻率大於堆頂元素時才更新
            # 補充: min-heap 的特性，heap[0] 是最小的元素
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))
        
        # 3. 提取結果
        return [
            num 
            for _, num in heap
        ]

    def topKFrequent_sort(self, nums: List[int], k: int) -> List[int]:
        # 排序解法
        count = Counter(nums)
        return [
            num 
            for num, _ in count.most_common(k)
        ]
    

# 測試
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3,3,3,3,3,4], 2))
print(sol.topKFrequent_sort([1,1,1,2,2,3,3,3,3,3,4], 2))