class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        chars = set()
        start, end = 0, 0
        while end < len(s):
            if s[end] in chars:
                chars.remove(s[start])
                start += 1
            else:
                chars.add(s[end])
                end += 1
                max_len = max(end - start, max_len)
        return max_len
        