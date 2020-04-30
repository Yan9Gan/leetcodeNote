# 84.柱状图中最大的矩形 —— 栈、数组

### 题目内容与要求

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

![示例图一](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram.png)

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

![示例图二](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram_area.png)

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

```
输入: [2,1,5,6,2,3]
输出: 10
```

> 来源：力扣（LeetCode）\
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram

### 题解

本题代码是参考了 [leetcode题解](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhao-liang-bian-di-yi-ge-xiao-yu-ta-de-zhi-by-powc/) 中的思路二。

首先是本人的思路：

思路一：按照每一个出现过的高度去计算各自的最大面积，求得最大面积。这个算法的最坏时间复杂度会达到O(n^2)，无法通过 _leetcode_ 的测试用例。

思路二：计算每一个 _height_ 向左右延伸的最大面积，这个算法依然无法通过 _leetcode_ 的测试用例。

正解：

该思路是通过维护单调递增的栈动态计算各个 _height_ 的最大面积。

1. 首先在给定 _heights_ 前后加上0，为了使当后面没有 _height_ 时可以计算出最大面积。
2. 当出现某个 _height_ 比栈顶元素对应的 _height_ 大时，说明目前栈顶元素可以继续向右延伸，因此将当前索引入栈。
3. 当出现某个 _height_ 比栈顶元素对应的 _height_ 小时，说明当前栈顶元素对应的柱无法向右延展，即可计算当前索引-1与栈顶元素的距离乘以当前栈顶元素的 _height_，即得到对应列的最大面积。
