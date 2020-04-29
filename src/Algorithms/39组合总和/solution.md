# 39.组合总和 —— 数组、回溯算法

### 题目内容与要求

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。candidates 中的数字可以无限制重复被选取。

说明：

- 所有数字（包括 target）都是正整数。

- 解集不能包含重复的组合。

> 来源：力扣（LeetCode）\
链接：https://leetcode-cn.com/problems/combination-sum

### 题解

本题的设计思路是，遍历candidates数组，当目前数组和小于target时进入递归，进行下一层遍历，当数组和等于target时将结果排序，添加到返回列表中。

本题解存在一个明显的缺点在于做了过多无意义的遍历，比如`candidates=[6, 2, 2, 4]`、`target=9`，若此时在数组中的数据为`[6, 2]`，那么就会进入下一层递归，增多一层无意义的遍历。或者当`candidates=[6, 4, 3, 2]`、`target=9`时，若此时数组中的数据为`[6, 4]`，此时是需要继续遍历不能返回上一层的，因为`[6, 3]`是正解，所以会导致过多遍历。

因此在最开始时，先将candidates进行排序，这样子当其中一个组合的总和超过target时即可return。

经过此步改良后执行时间从700ms缩短至180ms，不过这样的时间复杂度依然远远不够，因此还可以参考 [leetcode大神的回溯+剪枝法](https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/)
