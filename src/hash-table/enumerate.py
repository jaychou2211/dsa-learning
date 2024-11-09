# reference: example-01.py

# enumerate() 是 Python 的一個內建函數，
# 它可以同時獲取迭代對象的索引和值。
# 讓我用幾個簡單的例子來說明：

# 基本用法
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f"索引: {i}, 值: {fruit}")

# 輸出:
# 索引: 0, 值: apple
# 索引: 1, 值: banana
# 索引: 2, 值: cherry

# 可以指定起始索引
for i, fruit in enumerate(fruits, start=1):
    print(f"索引: {i}, 值: {fruit}")

# 輸出:
# 索引: 1, 值: apple
# 索引: 2, 值: banana
# 索引: 3, 值: cherry

# 轉換為列表查看內部結構
print(list(enumerate(fruits)))
# 輸出: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]