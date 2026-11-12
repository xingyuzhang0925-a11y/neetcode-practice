"""
Valid Anagram (Easy · Arrays & Hashing)
笔记见 valid_anagram.md / Notes: valid_anagram.md
"""

from typing import List


# ---------- 写法 1：排序 Sorting · O(n log n) time, O(1)/O(n) space ----------
class SolutionSorting:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)           # 排好序以后应该一模一样


# ---------- 写法 2：哈希表数个数 Hash map · O(n) time, O(1) space ✅ ----------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):                    # 长度不一样，肯定不是
            return False

        countS, countT = {}, {}                 # 两个"计数本"
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1   # s 里这个字母 +1
            countT[t[i]] = countT.get(t[i], 0) + 1   # t 里这个字母 +1
        return countS == countT                 # 两本账一样 → 是


# ---------- 写法 3：26 个格子的数组 Array of 26 · O(n) time, O(1) space ----------
class SolutionArray:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26                        # a~z 每个字母一个格子
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1    # s 的字母 +1
            count[ord(t[i]) - ord('a')] -= 1    # t 的字母 -1
        for c in count:
            if c != 0:                          # 加减不平 → 不是
                return False
        return True


# ---------- 自己测一下 / Quick tests ----------
if __name__ == "__main__":
    for cls in [SolutionSorting, Solution, SolutionArray]:
        sol = cls()
        assert sol.isAnagram("racecar", "carrace") is True
        assert sol.isAnagram("jar", "jam") is False
        assert sol.isAnagram("a", "ab") is False
        assert sol.isAnagram("aacc", "ccac") is False
    print("All tests passed ✅")
