class Solution:
    def add(self, el, d):
        if el not in d:
            d[el] = 1
        else:
            d[el] += 1
    def remove(self, el, d):
        d[el] -= 1
    def is_valid(self, d):
        for ch in d:
            if d[ch] > 1:
                return False
        return True
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        first = 0
        second = 0
        d = {}
        result = 0
        while second < n:
            self.add(s[second], d)
            while first < second and not self.is_valid(d):
                self.remove(s[first], d)
                first += 1
            length = second - first + 1
            result = max(result, length)
            second += 1
        return result

