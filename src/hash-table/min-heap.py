# reference: example-03.py

import heapq

# 創建一個空堆
heap = []

# 添加元素
heapq.heappush(heap, 3)
print("添加 3:", heap)  # [3]

heapq.heappush(heap, 1)
print("添加 1:", heap)  # [1, 3]  # 1 比 3 小，自動調整到堆頂

heapq.heappush(heap, 4)
print("添加 4:", heap)  # [1, 3, 4]

heapq.heappush(heap, 2)
print("添加 2:", heap)  # [1, 2, 4, 3]  # 自動調整保持最小堆特性

# 移除元素
min_val = heapq.heappop(heap)
print(f"移除的最小值: {min_val}")  # 1
print("移除後的堆:", heap)  # [2, 3, 4]