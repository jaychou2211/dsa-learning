# LeetCode #49 - Group Anagrams

# 題目描述
# 給定一個字串陣列 strs，將所有的字母異位詞（anagrams）分組。
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# 解題思路過程
# 1. 分析題目
# 需要找出所有互為重組的字串（字母異位詞）
# 字串中只包含小寫英文字母
# 輸出的順序不重要 ⭐️⭐️⭐️
# 需要將結果以群組方式返回

# 2. 破解關鍵重點
# 2.1 如何判斷兩個字串是否為字母異位詞？
# 字母出現次數相同 ?
# 排序後的字串相同 ?
# 2.2 如何有效率地進行分組？
# 需要一個能快速查找的資料結構
# 需要一個可以作為 key 的標準化形式 (這裡先選排序)
# 分組，將相同 key 的字串放入同一個群組

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 使用 defaultdict 避免需要檢查 key 是否存在
        anagram_map = defaultdict(list)
        
        # 遍歷每個字串
        for s in strs:
            # 將字串排序作為 key
            # ''.join(sorted(s)) 會將 "eat" 轉換為 "aet"
            sorted_str = ''.join(sorted(s))
            anagram_map[sorted_str].append(s)
        
        # 返回所有群組
        return list(anagram_map.values())


# 測試
test_cases = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"],
    ["",""],
]

for strs in test_cases:
    result = Solution().groupAnagrams(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}\n")