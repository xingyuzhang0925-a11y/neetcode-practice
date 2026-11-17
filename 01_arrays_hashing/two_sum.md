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
| 1 暴力 | 两层循环，把每一对数加起来看等不等于 target | *Use two nested loops to check every pair, and return their indices if they add up to the target.* |
| 2 排序 + 双指针 | 先记下每个数原来的下标再排序，左指针指最小、右指针指最大，和太小左边右移，和太大右边左移 | *Store each number with its original index, then sort. Put one pointer at the smallest number and one at the largest. If the sum is too small, move the left pointer right; if it's too big, move the right pointer left.* |
| 3 哈希表（两遍） | 第一遍把所有数和下标存进哈希表，第二遍对每个数找"还差的那个数"在不在表里（不能是自己） | *First pass: store every number and its index in a hash map. Second pass: for each number, check if the difference is in the map and isn't the same index.* |
| 4 哈希表（一遍）✅ | 边走边记，每个数先算还差多少，差的数见过就返回，没见过就把自己记下来 | *Loop through the array once. For each number, work out the difference from the target. If the difference is already in the hash map, return both indices. Otherwise, store the number and its index.* |

---

## 四种写法 / Four approaches（按 NeetCode 顺序）

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

### 写法 2：排序 + 双指针 Sorting (two pointers)

**思路：**排好序以后，最左边是最小的数，最右边是最大的数。两个手指一左一右：
- 加起来**太小** → 左手指往右挪，换一个大一点的数
- 加起来**太大** → 右手指往左挪，换一个小一点的数
- **刚好** → 找到了

**为什么要先记下原来的下标？**题目要返回原来的下标，一排序位置就乱了，所以排序前先把 `[数字, 原来的下标]` 绑在一起。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, n in enumerate(nums):
            A.append([n, i])            # [数字, 原来的下标]
        A.sort()                        # 按数字从小到大排

        left, right = 0, len(A) - 1
        while left < right:
            cur = A[left][0] + A[right][0]
            if cur == target:
                return [min(A[left][1], A[right][1]),
                        max(A[left][1], A[right][1])]
            elif cur < target:
                left += 1               # 太小，左边右移
            else:
                right -= 1              # 太大，右边左移
        return []
```

**走一遍：`nums = [5, 1, 3]`，`target = 4`**

排序后 `A = [[1, 1], [3, 2], [5, 0]]`

| left 指向 | right 指向 | 和 | 做什么 |
|---|---|---|---|
| 1（原下标 1） | 5（原下标 0） | 6 | 太大，right 左移 |
| 1（原下标 1） | 3（原下标 2） | 4 | 刚好！返回 `[1, 2]` |

**最后为什么用 `min` 和 `max`？**排序后原下标的大小顺序可能反了，用 min、max 保证小的下标在前。

> 双指针（two pointers）是 NeetCode 第二大类的核心方法，这里先混个眼熟。

### 写法 3：哈希表（两遍）Hash map, two pass

**思路：**第一遍先把所有数和下标都存进哈希表；第二遍对每个数算"还差多少"，去表里查。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}                    # 数字 -> 下标
        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
```

**为什么要 `indices[diff] != i`？**因为所有数已经提前存进去了，包括自己。`target = 6, n = 3` 时，表里的 3 可能就是它自己，同一个数不能用两次。

### 写法 4：哈希表（一遍）Hash map, one pass ✅ 面试主答案

**思路：**把写法 3 的两遍合成一遍，边走边记。

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

**为什么先查、再记？**
查的时候自己还没进表，所以不会找到自己，也就不用像写法 3 那样判断 `!= i`。

**走一遍：`nums = [3, 4, 5, 6]`，`target = 7`**

| i | n | diff = 7 - n | diff 在 seen 里吗？ | 做什么 | seen |
|---|---|---|---|---|---|
| 0 | 3 | 4 | ❌ | 记下 3 | `{3: 0}` |
| 1 | 4 | 3 | ✅ 3 的下标是 0 | 返回 `[0, 1]` | |

---

## 复杂度 / Complexity

| 写法 Approach | 时间 Time | 空间 Space | 为什么 |
|---|---|---|---|
| 1 暴力 | O(n²) | O(1) | 两层循环；只用了 i、j |
| 2 排序 + 双指针 | O(n log n) | O(n) | 排序 n log n + 双指针走一遍 n，只留大的；新建了列表 A 存 n 对 |
| 3 哈希表（两遍） | O(n) | O(n) | 走两遍是 2n，常数 2 忽略；表里存 n 个数 |
| **4 哈希表（一遍）** | **O(n)** | **O(n)** | 只走一遍；最坏要把 n 个数都存进去 |

**为什么这里空间是 O(n)，上一题是 O(1)？**
这题存的是**数字**，数字种类没有上限，最坏情况 n 个数全要存。上一题存的是小写字母，最多 26 种。

**为什么两遍也是 O(n)？**走两遍是 2n 次，跟第三题（26 格数组）那里一样，前面的常数 2 不管，还是 O(n)。

---

## 英文讲解 / How I explain it in the interview

> The brute-force way is to check every pair, which is O(n squared). A better way is to use a **hash map**. I loop through the array once. For each number, I work out the **difference** between the target and that number. If the difference is already in the hash map, I've found the pair, so I return both indices. If not, I store the current number and its index in the map. This runs in **O(n) time** and uses **O(n) space** for the hash map.

## 本题词汇 / Key words

| 英文 | 中文 |
|---|---|
| two pointers | 双指针 |
| pointer | 指针（指着某个位置的"手指"） |
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
