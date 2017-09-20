# -*- coding:utf-8 -*-

def longestSubstringK(s, k):
    """
    给定字符串s，计算最多包括k个不同字符的最长子串。
    如给定'eceba'，k=3，则最长子串为'eceb'。
    双指针法。
    :param s: 字符串
    :param k: 规定的不同字符的个数
    :return:
    """
    size = len(s)
    if size <= 0:
        return 0
    dict = {}
    left = mx = 0
    for right in range(size):
        if not dict.has_key(s[right]):
            dict[s[right]] = 1
        else:
            dict[s[right]] += 1
        while len(dict) > k:
            dict[s[left]] -= 1
            if dict[s[left]] == 0:
                dict.pop(s[left])
            left += 1
        mx = max(right - left + 1, mx)
    return mx


if __name__ == '__main__':
    s = 'eceba'
    print longestSubstringK(list(s), 3)