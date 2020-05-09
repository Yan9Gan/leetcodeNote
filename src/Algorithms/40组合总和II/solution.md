# 40.组合总和 II —— 数组、回溯算法

### 题目内容与要求

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：
- 所有数字（包括目标数）都是正整数。
- 解集不能包含重复的组合。 

示例:
```
输入: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8,
所求解集为:
[
    [1, 7],
    [1, 2, 5],
    [2, 6],
    [1, 1, 6]
]
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

> 来源：力扣（LeetCode）\
链接：https://leetcode-cn.com/problems/combination-sum-ii

### 题解

本题是第39题【**组合总和**】的延伸，题目要求中唯一的区别就是本题的 _candidates_ 是不可以重复选取的，这里的不重复选取不是只每个数字只出现一个，而是数字出现的个数不超过 _candidates_ 中给出的数字个数。

因此思路是依然可以先将 _candidates_ 进行排序，递归方法一样传入三个参数：候选集、当前结果集、总结果集。由于限定了数字不可重复选取，因此在进入下一层递归时，_candidates_ 参数传入的值应该是当前取出候选值之后的候选集。
