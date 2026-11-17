"""
Two Sum (Easy · Arrays & Hashing)
笔记见 two_sum.md / Notes: two_sum.md
"""

from typing import List


# ---------- 写法 1：暴力 Brute force · O(n^2) time, O(1) space ----------
class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# ---------- 写法 2：哈希表（两遍）Hash map, two pass · O(n) time, O(n) space ----------
class SolutionTwoPass:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}                            # 数字 -> 下标
        for i, n in enumerate(nums):
            indices[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:   # 不能用自己
                return [i, indices[diff]]
        return []


# ---------- 写法 3：哈希表（一遍）Hash map, one pass · O(n) time, O(n) space ✅ ----------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                               # 记事本：数字 -> 它的下标
        for i, n in enumerate(nums):
            diff = target - n                   # 还差多少
            if diff in seen:                    # 差的那个数之前见过
                return [seen[diff], i]
            seen[n] = i                         # 没见过 → 把自己记下来
        return []


# ---------- 自己测一下 / Quick tests ----------
if __name__ == "__main__":
    for cls in [SolutionBruteForce, SolutionTwoPass, Solution]:
        sol = cls()
        assert sorted(sol.twoSum([3, 4, 5, 6], 7)) == [0, 1]
        assert sorted(sol.twoSum([4, 5, 6], 10)) == [0, 2]
        assert sorted(sol.twoSum([5, 5], 10)) == [0, 1]
        assert sorted(sol.twoSum([3, 2, 4], 6)) == [1, 2]
    assert Solution().twoSum([3, 4, 5, 6], 7) == [0, 1]
    print("All tests passed ✅")
