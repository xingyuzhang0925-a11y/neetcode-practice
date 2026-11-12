"""
Contains Duplicate (Easy · Arrays & Hashing)
笔记见 contains_duplicate.md / Notes: contains_duplicate.md
"""

from typing import List


# ---------- 写法 1：暴力 Brute force · O(n^2) time, O(1) space ----------
class SolutionBruteForce:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):   # 只和后面的数比
                if nums[i] == nums[j]:
                    return True
        return False


# ---------- 写法 2：排序 Sorting · O(n log n) time, O(1) space ----------
class SolutionSorting:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()                             # 重复的数会挨在一起
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:          # 和前一个比
                return True
        return False


# ---------- 写法 3：哈希集合 Hash set · O(n) time, O(n) space ✅ ----------
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()                            # 记事本
        for num in nums:
            if num in seen:                     # 见过 → 重复
                return True
            seen.add(num)                       # 没见过 → 记下来
        return False


# ---------- 写法 4：一行写法 One-liner · O(n) time, O(n) space ----------
class SolutionOneLiner:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)       # 去重后变短 → 有重复


# ---------- 自己测一下 / Quick tests ----------
if __name__ == "__main__":
    for cls in [SolutionBruteForce, SolutionSorting, Solution, SolutionOneLiner]:
        s = cls()
        assert s.hasDuplicate([1, 2, 3, 3]) is True
        assert s.hasDuplicate([1, 2, 3, 4]) is False
        assert s.hasDuplicate([]) is False
        assert s.hasDuplicate([-1, -1]) is True
    print("All tests passed ✅")
