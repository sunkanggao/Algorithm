# -*- coding:utf-8 -*-

"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution1(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        r = ''
        flag = True
        for i in range(min([len(s) for s in strs])):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    flag = False
                    break
            if flag:
                r += strs[0][i]
            else:
                break
        return r


class Solution2(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


if __name__ == '__main__':
    s1 = Solution1()
    print s1.longestCommonPrefix(['cabvv', 'cabvs', 'cabs'])
    s2 = Solution2()
    print s2.longestCommonPrefix(['cabvv', 'cabvs', 'cabs'])