# Two Sum
# 給定一個整數數組 nums 和一個目標值 target，
# 請你返回兩個數字的索引，使得它們的和等於目標值。

# 解法一:雙迴圈
def twoSum1(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append([i, j])
    return result

# 解法二:Hash Table
def twoSum2(nums, target):
    result = []
    num_to_indices = {}
    
    # 先建立「陣列元素值」到「索引[0..*]」的 Hash Table
    for i, num in enumerate(nums):
        if num in num_to_indices:
            num_to_indices[num].append(i)
        else:
            num_to_indices[num] = [i]
    
    # 尋找所有可能的組合
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_indices:
            # 對於每個互補數的索引
            for j in num_to_indices[complement]:
                # 確保不會使用同一個索引，且不會重複添加
                if j > i:  # 只添加索引較大的組合，避免重複
                    result.append([i, j])
    
    return result

# 解法比較
# 解法一:雙迴圈
# 優點:
# - 空間複雜度低,只需 O(1) 的額外空間
# 缺點:
# - 時間複雜度高,需要 O(n^2) 的時間
# - 對於大數列,效率很低

# 解法二:Hash Table
# 優點:
# - 時間複雜度低,只需 O(n) 的時間
# - 對於大數列,效率很高
# 缺點: 
# - 空間複雜度高,最壞情況下需要 O(n) 的額外空間
# - 需要額外的 hash table 來存儲元素和索引

# 總結:
# 在這題中,使用 hash table 是更好的選擇,因為它可以將時間複雜度降到 O(n)。
# 雖然 hash table 需要額外的空間,但在實際情況中,這並不是大問題,因為 hash table 中存的是數列元素的值和索引,而不是整個數列。
# 除非空間非常緊張,否則使用 hash table 可以獲得更好的效率。

# need to test
nums = [2, 7, 2, 15]
target = 9
print(twoSum1(nums, target))
print(twoSum2(nums, target))