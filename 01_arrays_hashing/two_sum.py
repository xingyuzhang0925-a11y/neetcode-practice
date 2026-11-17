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


# ---------- 写法 2：排序 + 双指针 Sorting · O(n log n) time, O(n) space ----------
class SolutionSorting:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, n in enumerate(nums):
            A.append([n, i])                    # 记下 [数字, 原来的下标]
        A.sort()                                # 按数字从小到大排

        left, right = 0, len(A) - 1             # 一个指最左（最小），一个指最右（最大）
        while left < right:
            cur = A[left][0] + A[right][0]
            if cur == target:
                return [min(A[left][1], A[right][1]),
                        max(A[left][1], A[right][1])]
            elif cur < target:
                left += 1                       # 太小 → 左边往右挪，换个大一点的
            else:
                right -= 1                      # 太大 → 右边往左挪，换个小一点的
        return []


# ---------- 写法 3：哈希表（两遍）Hash map, two pass · O(n) time, O(n) space ----------
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


# ---------- 写法 4：哈希表（一遍）Hash map, one pass · O(n) time, O(n) space ✅ ----------
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
    for cls in [SolutionBruteForce, SolutionSorting, SolutionTwoPass, Solution]:
        sol = cls()
        assert sorted(sol.twoSum([3, 4, 5, 6], 7)) == [0, 1]
        assert sorted(sol.twoSum([4, 5, 6], 10)) == [0, 2]
        assert sorted(sol.twoSum([5, 5], 10)) == [0, 1]
        assert sorted(sol.twoSum([3, 2, 4], 6)) == [1, 2]
        assert sol.twoSum([5, 1, 3], 4) == [1, 2]
    assert Solution().twoSum([3, 4, 5, 6], 7) == [0, 1]
    print("All tests passed ✅")
