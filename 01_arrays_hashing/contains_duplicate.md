# Contains Duplicate

**Easy · Arrays & Hashing** · [NeetCode 题目链接](https://neetcode.io/problems/duplicate-integer) · 代码文件：[`contains_duplicate.py`](contains_duplicate.py)

---

## 一句话题意 / Problem in one line

数组里有没有哪个数出现了两次或以上。

*Return `True` if any number appears more than once in the array.*

## 我第一反应 / 卡在哪 / Where I got stuck

- 一开始只想到两层循环（暴力）。
- 不太理解排序为什么是 O(n log n)，空间为什么是 O(1)。

## 关键思路 / Key idea

用一个 set 当"记事本"：一个一个往下看，见过的就记下来。如果某个数已经在记事本里，说明重复了，直接返回 `True`。

*Use a set to remember numbers I have already seen.*

---

## 四种写法 / Four approaches

### 写法 1：暴力 Brute force

拿每个数跟它后面的每个数比一遍。

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):   # 只和后面的数比
                if nums[i] == nums[j]:
                    return True
        return False
```

### 写法 2：排序 Sorting

排好序以后，一样的数会挨在一起，只要比相邻的两个数。

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:          # 和前一个比
                return True
        return False
```

### 写法 3：哈希集合 Hash set ✅ 面试主答案

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()                            # 记事本
        for num in nums:
            if num in seen:                     # 见过 → 重复
                return True
            seen.add(num)                       # 没见过 → 记下来
        return False
```

### 写法 4：一行写法 One-liner

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)       # 去重后变短 → 有重复
```

---

## 复杂度 / Complexity

| 写法 Approach | 时间 Time | 空间 Space | 为什么 |
|---|---|---|---|
| 暴力 Brute force | O(n²) | O(1) | 外层 n 次 × 内层约 n 次；只多了 i、j 两个变量 |
| 排序 Sorting | O(n log n) | O(1)* | 排序 n log n + 扫一遍 n，只留大的；原地排序没新建容器 |
| **哈希集合 Hash set** | **O(n)** | **O(n)** | 每个数只看一次；set 最多存 n 个数 |
| 一行写法 One-liner | O(n) | O(n) | 同上，但一定会把整个数组转一遍，不能提前停 |

\* 不算排序内部用的空间 / *not counting the sort's internal space*

---

## 英文讲解 / How I explain it in the interview

> The brute-force approach would compare every pair of numbers, which is O(n squared). A better idea is to use a **hash set**. I iterate through the array, and for each number I check whether it's already in the set. If it is, I've found a duplicate, so I return true. Otherwise, I add it to the set. If I get to the end of the loop, there are no duplicates, so I return false. This runs in **O(n) time** and uses **O(n) extra space**.

如果面试官问 *"Can you do it without extra space?"*（能不能不用额外空间？）：

> I could sort the array first. Then any duplicates would be next to each other, so I only need to compare neighbours. That's O(n log n) time, but O(1) extra space.

## 本题词汇 / Key words

| 英文 | 中文 |
|---|---|
| duplicate | 重复项 |
| hash set | 哈希集合 |
| iterate through | 遍历 |
| early return | 提前返回 |
| in-place | 原地 |
| neighbours | 相邻的元素 |
| trade-off | 权衡 |

## 容易错的地方 / Common mistakes

- 暴力写法内层是 `range(i + 1, len(nums))`，不是从 `i` 开始（不然会自己和自己比）。
- 排序写法 for 循环从 `1` 开始，这样才能和 `nums[i - 1]` 比较。
