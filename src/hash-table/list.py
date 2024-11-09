# reference: example-02.py

from collections import defaultdict

# 以下三種寫法效果相同：

# 1. 使用 list 作為工廠函數
d1 = defaultdict(list)
d1['key'].append(1)  # 自動創建空列表 []，然後添加 1

# 2. 使用 lambda 返回空列表
d2 = defaultdict(lambda: [])
d2['key'].append(1)  # 自動創建空列表 []，然後添加 1

# 3. 使用普通函數
def create_list():
    return []
d3 = defaultdict(create_list)
d3['key'].append(1)  # 自動創建空列表 []，然後添加 1

print(d1)
print(d2)
print(d3)

# 當我們寫 defaultdict(list)，這裡的 list 是作為一個工廠函數（factory function）傳給 defaultdict。
# list 在 Python 中不只是一個類型名稱，
# 它也是一個可調用的類（callable class）。
# 當我們把 list 傳給 defaultdict 時，每當需要創建新值時，defaultdict 會調用 list() 來創建一個新的空列表。
# 所以 list 在這裡是作為一個函數被傳入，用來生成默認值。
# 這是 Python 中很優雅的設計之一，因為它讓我們可以直接使用內建的 list 類作為工廠函數。
