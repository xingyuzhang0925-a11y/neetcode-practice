# 基础概念：列表、字典、集合 / Basic Data Structures

数组、列表、哈希表、字典、集合……名字很多，**本质上只有三种东西**，只是不同场合叫法不一样。

---

## 一张表看懂

| 本质 | Python 里叫 | 面试 / 题目里常叫 | 长相 | 比喻 |
|---|---|---|---|---|
| 一排按位置放的东西 | **list**（列表） | **array**（数组） | `[5, 1, 3]` | 一排编了号的储物柜 |
| 一本"名字 → 内容"的本子 | **dict**（字典） | **hash map / hash table**（哈希表） | `{'a': 2, 'b': 1}` | 通讯录 |
| 一袋不重复的东西 | **set**（集合） | **hash set**（哈希集合） | `{5, 1, 3}` | 签到名单 |

- **数组 = 列表**：别的语言（Java、C）叫 array，Python 里叫 list
- **哈希表 = 字典**：哈希表是通用叫法，dict 是 Python 里的名字

---

## 1. 列表 list（= 数组 array）：一排储物柜

```python
nums = [5, 1, 3]
```

一排编了号的储物柜，编号从 0 开始：

```
编号：  0   1   2
内容：  5   1   3
```

- 按**编号（下标 index）**取：`nums[0]` → `5`
- **有顺序**，可以**重复**：`[5, 5, 3]` 没问题
- 查"里面有没有 3"要**从头一个个看**，慢，O(n)

**做过的题里：**每道题的输入 `nums`；Valid Anagram 的 26 格数组 `[0] * 26`；Two Sum 方法 2 的列表 `A`

---

## 2. 字典 dict（= 哈希表 hash map）：通讯录

```python
countS = {'a': 2, 'b': 1}
```

按**名字**查电话，不用管排在第几页。

- 冒号左边是 **key（键）**，冒号右边是 **value（值）**
- 按 key 取：`countS['a']` → `2`
- key **不能重复**，再存一次同一个 key 会**覆盖**旧的
- 查"有没有某个 key"**很快**，一步到位，O(1)
- 查不到的 key 直接取会报错（KeyError），可以用 `.get(key, 默认值)` 安全地取

**做过的题里：**
- Valid Anagram：`{字母: 出现次数}`
- Two Sum：`{数字: 下标}`

---

## 3. 集合 set（= 哈希集合 hash set）：签到名单

```python
seen = {5, 1, 3}
```

只关心"**这个东西有没有出现过**"，不记别的。

- 只有东西本身，**没有编号，也没有 value**
- **自动去重**：`set([5, 5, 3])` → `{5, 3}`
- 查"在不在里面"**很快**，O(1)：`3 in seen` → `True`
- 加东西用 `.add()`：`seen.add(4)`

**做过的题里：**Contains Duplicate 的 `seen = set()`

---

## 怎么选？问自己一个问题

| 我需要…… | 用 |
|---|---|
| 按**位置**存一排东西 | **list** |
| 只想知道某个东西**有没有出现过** | **set** |
| 不光要知道有没有，还要**记一个附带信息**（次数、下标……） | **dict** |

对照做过的题：

| 题目 | 需要知道什么 | 用了 |
|---|---|---|
| Contains Duplicate | 这个数见没见过 | **set** |
| Valid Anagram | 这个字母出现了**几次** | **dict**（字母 → 次数） |
| Two Sum | 这个数见没见过，**在哪一位** | **dict**（数字 → 下标） |

---

## ⚠️ 小心：dict 和 set 都用大括号

```python
{'a': 2}     # 有冒号 → dict
{5, 1, 3}    # 没冒号 → set
{}           # ⚠️ 空的大括号是 dict，不是 set！
set()        # 空 set 要这样写
```

所以 Contains Duplicate 写的是 `seen = set()`，不能写 `seen = {}`。

---

## 常用操作对照

| 想做的事 | list | dict | set |
|---|---|---|---|
| 新建空的 | `[]` | `{}` | `set()` |
| 加东西 | `a.append(x)` | `d[key] = value` | `s.add(x)` |
| 查有没有 | `x in a`（慢，O(n)） | `key in d`（快，O(1)） | `x in s`（快，O(1)） |
| 取东西 | `a[i]`（按位置） | `d[key]`（按 key） | 不能按位置取 |
| 长度 | `len(a)` | `len(d)` | `len(s)` |

---

## 面试英文

写代码用 Python 的名字（list / dict / set），**说话**时用通用的叫法：

| 说 | 写 |
|---|---|
| array | `list` |
| hash map | `dict` |
| hash set | `set` |

> *"I'll use a **hash map** to store each number and its index."*
> *"I'll use a **hash set** to keep track of the numbers I've seen."*
