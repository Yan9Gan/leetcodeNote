# -*- coding:utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_num = 0
        cur_s = ''
        for item in s:
            if item not in cur_s:
                cur_s += item
            else:
                if len(cur_s) > max_num:
                    max_num = len(cur_s)
                idx = cur_s.index(item)
                cur_s = cur_s[idx+1:] + item
        else:
            if cur_s and len(cur_s) > max_num:
                max_num = len(cur_s)

        return max_num


if __name__ == '__main__':
    S = Solution()
    s = " "
    num = S.lengthOfLongestSubstring(s)
    print(num)
