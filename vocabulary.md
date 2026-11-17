# 算法面试必记英文词汇 / Interview Vocabulary

每做完一题，把新学到的词加到最后的"新增词汇"里。

---

## 1. 复杂度 Complexity（每道题都要说）

| 英文 | 中文 | 怎么读 / 例句 |
|---|---|---|
| time complexity | 时间复杂度 | *What's the time complexity of this solution?* |
| space complexity | 空间复杂度 | *The space complexity is O(n).* |
| Big O | 大 O 表示法 | "big oh" · *In Big O terms, this is linear.* |
| O(1) | 常数级 | "O of one" · *constant time / constant space* |
| O(n) | 线性 | "O of n" · *linear time* |
| O(n²) | 平方级 | "O of n squared" · *quadratic time* |
| O(log n) | 对数级 | "O of log n" · *logarithmic time* |
| O(n log n) | 线性对数级（排序常见） | "O of n log n" · *Sorting takes O(n log n) time.* |
| extra space | 额外空间 | *It uses O(n) extra space.* |
| worst case / best case | 最坏 / 最好情况 | *In the worst case, we check every element.* |
| scale | 扩展、变大时的表现 | *This doesn't scale well for large inputs.* |

## 2. 数据结构 Data structures

| 英文 | 中文 | Python |
|---|---|---|
| array / list | 数组 / 列表 | `[]` |
| hash set | 哈希集合 | `set()` |
| hash map / dictionary | 哈希表 / 字典 | `{}` |
| string | 字符串 | `""` |
| stack | 栈（后进先出） | `list` + `append` / `pop` |
| queue | 队列（先进先出） | `collections.deque` |
| linked list | 链表 | `ListNode` |
| tree / binary tree | 树 / 二叉树 | `TreeNode` |
| heap / priority queue | 堆 / 优先队列 | `heapq` |
| graph | 图 | 常用 `dict` 存邻接表 |
| element | 元素 | *each element in the array* |
| index / indices | 下标（单数 / 复数） | *the element at index i* |
| key / value | 键 / 值 | *the number as the key, its count as the value* |

## 3. 动作 Actions（描述代码在做什么）

| 英文 | 中文 | 例句 |
|---|---|---|
| iterate through / loop through | 遍历 | *I iterate through the array.* |
| check whether ... | 检查是否…… | *I check whether it's already in the set.* |
| add ... to ... | 把……加到…… | *I add it to the set.* |
| store | 存 | *I store each number as a key.* |
| look up | 查找 | *Lookups in a set are O(1).* |
| return | 返回 | *I return true.* |
| compare | 比较 | *compare every pair* |
| sort | 排序 | *sort the array first* |
| keep track of | 记录、跟踪 | *keep track of the numbers I've seen* |
| update | 更新 | *update the count* |
| increment / decrement | 加一 / 减一 | *increment the counter* |
| swap | 交换 | *swap the two elements* |
| in-place | 原地（不新建空间） | *sort the array in-place* |

## 4. 解题方法 Approaches

| 英文 | 中文 |
|---|---|
| brute force | 暴力解法 |
| optimal solution | 最优解 |
| trade-off | 权衡 |
| trade space for time | 用空间换时间 |
| early return / exit early | 提前返回 |
| two pointers | 双指针 |
| sliding window | 滑动窗口 |
| binary search | 二分查找 |
| recursion / recursive | 递归 |
| dynamic programming (DP) | 动态规划 |
| edge case | 边界情况 |
| constraint | 约束条件 |

## 5. 面试常用句子 Useful sentences

**开始前，确认题意 Clarifying**
- *Just to make sure I understand, ...* 我确认一下我理解得对不对……
- *Can the input be empty?* 输入可以为空吗？
- *Can there be negative numbers / duplicates?* 会有负数 / 重复吗？
- *Is the array sorted?* 数组是排好序的吗？

**讲思路 Explaining**
- *The brute-force approach would be to ..., which is O(n²).* 暴力解法是……
- *A better idea is to use a hash set.* 更好的办法是用哈希集合。
- *The key observation is that ...* 关键的发现是……
- *This works because ...* 这样可行是因为……

**写代码时 While coding**
- *Let me walk you through the code.* 我带您过一遍代码。
- *Let me test it with an example.* 我用一个例子测一下。

**卡住时 When stuck**
- *Let me think about this for a moment.* 我想一下。
- *Could I get a small hint?* 能给一点提示吗？

**收尾 Wrapping up**
- *This runs in O(n) time and uses O(n) extra space.*
- *If we needed O(1) space, we could sort the array instead.*

---

## 6. 新增词汇 New words（每题做完往下加）

| 题目 | 英文 | 中文 |
|---|---|---|
| Contains Duplicate | duplicate | 重复项 |
| Contains Duplicate | neighbours | 相邻的元素（英式拼写） |
| Valid Anagram | anagram | 字母异位词（字母一样、顺序不同） |
| Valid Anagram | character | 字符、字母 |
| Valid Anagram | frequency | 出现次数、频率 |
| Valid Anagram | lowercase letters | 小写字母 |
| Valid Anagram | regardless of order | 不管顺序 |
| Contains Duplicate | nested loops | 嵌套循环（一个循环套另一个） |
| Valid Anagram | count（动词） | 数、计数 |
| Valid Anagram | subtract | 减去 |
| Two Sum | target | 目标值 |
| Two Sum | difference / complement | 差值（还差的那个数） |
| Two Sum | add up to | 加起来等于 |
| Two Sum | pair | 一对 |
| Two Sum | one pass | 只遍历一遍 |
| Two Sum | two pointers | 双指针 |
| Two Sum | pointer | 指针 |
