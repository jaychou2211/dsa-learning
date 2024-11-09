# reference: example-03.py

from collections import Counter

# 創建 Counter 對象
nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4]
count = Counter(nums)
print(count)  # Counter({3: 5, 1: 3, 2: 2, 4: 1})
print(count[5])  # 0  # 不存在的元素返回0而不是報錯
print(count[1])  # 3  # 存在的元素返回出現次數

# 自動統計每個元素出現的次數
letters = Counter('mississippi')
print(letters)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})