class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0

        tracker = {}

        for i in range(len(s)):
            for j in range(i, len(s)):
                ss = s[i:j + 1]
                if len(ss) < 3:
                    continue
                if ss not in tracker:
                    tracker[ss] = self.beauty(ss)
                ans += tracker[ss]

        return ans

    def beauty(self, s):
        tracker = {}
        for char in s:
            if char not in tracker:
                tracker[char] = 0
            tracker[char] += 1

        freq_list = [freq for char, freq in tracker.items()]
        freq_list.sort()
        return freq_list[-1] - freq_list[0]
