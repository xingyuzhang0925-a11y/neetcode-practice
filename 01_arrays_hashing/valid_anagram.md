# Valid Anagram

**Easy · Arrays & Hashing** · [NeetCode 题目链接](https://neetcode.io/problems/is-anagram) · 代码文件：[`valid_anagram.py`](valid_anagram.py)

---

## 一句话题意 / Problem in one line

两个字符串用的字母一样、每个字母的个数也一样（顺序可以不同），就返回 `True`。

*Return `True` if `s` and `t` use exactly the same letters the same number of times.*

例子：`"racecar"` 和 `"carrace"` → 都是 r×2、a×2、c×2、e×1 → `True`

## 我第一反应 / 卡在哪 / Where I got stuck

- （复习时自己填）

## 关键思路 / Key idea

给两个字符串各记一本账：每个字母出现了几次。最后比较两本账是不是一模一样。

*Count how many times each letter appears in both strings, then compare the counts.*

先检查长度：长度不一样，肯定不是，直接返回 `False`。

## 每种写法一句话 / Each approach in one sentence

| 写法 | 中文 | English |
|---|---|---|
| 排序 | 先判断长度，再把两个字符串排序，排完一模一样就返回 True | *First check if the lengths are the same. Then sort both strings. If they're exactly the same after sorting, return true.* |
| 哈希表 ✅ | 先判断长度，建两个哈希表，遍历两个字符串，记下每个字母出现几次，两个表相等就返回 True | *First check the lengths. Then create two hash maps and loop through both strings to count how many times each letter appears. If the two maps are equal, return true.* |
| 26 格数组 | 先判断长度，建一个 26 格的数组，s 的字母加一，t 的字母减一，最后全是 0 就返回 True | *First check the lengths. Then create an array of 26 zeros. For each letter in s, add one; for each letter in t, subtract one. If every count is zero at the end, return true.* |

---

## 三种写法 / Three approaches

### 写法 1：排序 Sorting

把两个字符串里的字母都排好序。如果是 anagram，排完以后应该一模一样。

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
```

`sorted("racecar")` → `['a','a','c','c','e','r','r']`

### 写法 2：哈希表数个数 Hash map ✅ 面试主答案

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
```

**`countS.get(s[i], 0)` 是什么意思？**
去账本里查这个字母现在记了几次。**如果还没记过，就当成 0。**
然后 `+ 1`，再写回账本。

一步步看 `s = "aab"`：

| 第几步 | 字母 | 查到几次 | +1 后账本 |
|---|---|---|---|
| 1 | a | 0（没记过） | `{'a': 1}` |
| 2 | a | 1 | `{'a': 2}` |
| 3 | b | 0（没记过） | `{'a': 2, 'b': 1}` |

### 写法 3：26 个格子的数组 Array of 26

题目只有小写字母 a~z，所以可以用一个长度 26 的列表当账本。s 里的字母 +1，t 里的字母 -1，最后每个格子都是 0 就说明一样。

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for c in count:
            if c != 0:
                return False
        return True
```

`ord(x) - ord('a')` 把字母变成格子编号：a → 0，b → 1，…，z → 25。

---

## 复杂度 / Complexity

（n 是字符串长度）

| 写法 Approach | 时间 Time | 空间 Space | 为什么 |
|---|---|---|---|
| 排序 Sorting | O(n log n) | O(1) 或 O(n) | 排序要 n log n；`sorted()` 会生成新列表 |
| **哈希表 Hash map** | **O(n)** | **O(1)** | 每个字母只看一次；账本最多 26 种字母，不会随 n 变大 |
| 26 格数组 Array | O(n) | O(1) | 同上，固定 26 个格子 |

**为什么哈希表的空间是 O(1)，不是 O(n)？**
账本里存的是"有哪几种字母"，不是"有多少个字母"。字符串再长，小写字母也只有 26 种，所以账本最多 26 行，是固定的。
如果面试官说"可以是任何字符（比如中文、emoji）"，空间就要说 O(k)，k 是不同字符的种类数。

---

## 英文讲解 / How I explain it in the interview

> First, if the two strings have different lengths, they can't be anagrams, so I return false. Then I use **two hash maps** to count how many times each character appears in `s` and in `t`. I iterate through both strings at the same time and update the counts. At the end, if the two maps are equal, the strings are anagrams. This runs in **O(n) time**. The space is **O(1)**, because there are only 26 lowercase letters, so each map has at most 26 keys.

如果面试官问 *"What if we can't use extra space?"*：

> I could sort both strings and compare them. That's O(n log n) time.

## 本题词汇 / Key words

| 英文 | 中文 |
|---|---|
| anagram | 字母异位词（字母一样、顺序不同的词） |
| character | 字符、字母 |
| frequency / count | 出现次数 |
| hash map | 哈希表（Python 里的 `dict`） |
| lowercase letters | 小写字母 |
| regardless of order | 不管顺序 |

## 容易错的地方 / Common mistakes

- 忘了先判断长度。长度不一样时，写法 2、3 用 `s[i]`、`t[i]` 会越界出错。
- `countS[s[i]] += 1` 会报错（KeyError），因为第一次出现时账本里还没有这个字母。所以要用 `.get(s[i], 0)`。
