# Two Sum

**Easy · Arrays & Hashing** · [NeetCode 题目链接](https://neetcode.io/problems/two-integer-sum) · 代码文件：[`two_sum.py`](two_sum.py)

---

## 一句话题意 / Problem in one line

数组里找**两个数加起来等于 target**，返回这两个数的**下标**（小的下标在前）。题目保证一定有且只有一个答案。

*Find two numbers that add up to `target` and return their indices.*

例子：`nums = [3, 4, 5, 6]`，`target = 7` → `3 + 4 = 7`，返回 `[0, 1]`

## 我第一反应 / 卡在哪 / Where I got stuck

- （复习时自己填）

## 关键思路 / Key idea

看到一个数 `n`，就想：**"我还差多少？"** 差的那个数是 `target - n`。
用一个哈希表当记事本，记下**之前见过的数和它的下标**。如果差的那个数之前见过，答案就找到了。

*For each number, ask: what number do I need to reach the target? Use a hash map to remember the numbers I've already seen and their indices.*

## 每种写法一句话 / Each approach in one sentence

| 写法 | 中文 | English |
|---|---|---|
| 暴力 | 两层循环，把每一对数加起来看等不等于 target | *Use two nested loops to check every pair, and return their indices if they add up to the target.* |
| 哈希表（一遍）✅ | 边走边记，每个数先算还差多少，差的数见过就返回，没见过就把自己记下来 | *Loop through the array once. For each number, work out the difference from the target. If the difference is already in the hash map, return both indices. Otherwise, store the number and its index.* |

---

## 写法 / Approaches

### 写法 1：暴力 Brute force

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

和第一题的暴力几乎一样，只是把 `nums[i] == nums[j]` 换成了 `nums[i] + nums[j] == target`。

### 写法 2：哈希表（一遍）Hash map, one pass ✅ 面试主答案

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                       # 数字 -> 它的下标
        for i, n in enumerate(nums):
            diff = target - n           # 还差多少
            if diff in seen:            # 差的那个数之前见过
                return [seen[diff], i]
            seen[n] = i                 # 没见过，把自己记下来
        return []
```

**`enumerate(nums)` 是什么？**
一次同时拿到**下标**和**数字**。`for i, n in enumerate([3, 4, 5])` 会依次得到 `(0, 3)`、`(1, 4)`、`(2, 5)`。
它等于 `for i in range(len(nums)): n = nums[i]`，只是写起来更短。

**为什么先检查、再记录？**
如果先把自己记进去再检查，像 `target = 6, n = 3` 这种情况，3 会找到它自己（3 + 3 = 6），但同一个数不能用两次。

**走一遍：`nums = [3, 4, 5, 6]`，`target = 7`**

| i | n | diff = 7 - n | diff 在 seen 里吗？ | 做什么 | seen |
|---|---|---|---|---|---|
| 0 | 3 | 4 | ❌ | 记下 3 | `{3: 0}` |
| 1 | 4 | 3 | ✅ 3 的下标是 0 | 返回 `[0, 1]` | |

### （了解）写法 3：哈希表（两遍）Two pass

第一遍把所有数和下标都存进哈希表，第二遍再找差的那个数。要额外判断"差的数不是自己"。复杂度和一遍一样，但一遍更简洁，面试写一遍的就行。代码见 [`two_sum.py`](two_sum.py)。

---

## 复杂度 / Complexity

| 写法 Approach | 时间 Time | 空间 Space | 为什么 |
|---|---|---|---|
| 暴力 Brute force | O(n²) | O(1) | 两层循环；只用了 i、j |
| **哈希表 Hash map** | **O(n)** | **O(n)** | 只走一遍，哈希表查找是一步；最坏要把 n 个数都存进去 |

**为什么这里空间是 O(n)，上一题是 O(1)？**
这题存的是**数字**，数字种类没有上限，最坏情况 n 个数全要存。上一题存的是小写字母，最多 26 种。

---

## 英文讲解 / How I explain it in the interview

> The brute-force way is to check every pair, which is O(n squared). A better way is to use a **hash map**. I loop through the array once. For each number, I work out the **difference** between the target and that number. If the difference is already in the hash map, I've found the pair, so I return both indices. If not, I store the current number and its index in the map. This runs in **O(n) time** and uses **O(n) space** for the hash map.

## 本题词汇 / Key words

| 英文 | 中文 |
|---|---|
| target | 目标值 |
| index / indices | 下标 |
| difference / complement | 差值（还差的那个数） |
| add up to | 加起来等于 |
| pair | 一对 |
| exactly one solution | 有且只有一个答案 |
| one pass | 只遍历一遍 |

## 容易错的地方 / Common mistakes

- 返回的是**下标**，不是数字本身。
- 哈希表要存 **数字 → 下标**（key 是数字），这样才能用 `diff in seen` 去查。
- 要**先检查、再记录**，不然同一个数可能被用两次。
- 返回顺序：`[seen[diff], i]`，之前见过的下标更小，放前面。
