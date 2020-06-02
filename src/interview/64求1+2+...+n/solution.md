# 64.求1+2+...+n

### 题目内容与要求

求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
```
输入: n = 3
输出: 6
```

示例 2：
```
输入: n = 9
输出: 45
```

> 来源：力扣（LeetCode）\
链接：https://leetcode-cn.com/problems/qiu-12n-lcof

### 题解

本题可通过递归求解，每次数字减一进去递归至数字等于0
