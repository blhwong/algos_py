from typing import List


class Solution:

    def compress(self, chars: List[str]) -> int:
        c = chars[0]
        count = 1
        j = 0
        for i in range(1, len(chars)):
            if c != chars[i]:
                chars[j] = c
                j += 1
                if count > 1:
                    for k in str(count):
                        chars[j] = k
                        j += 1
                c = chars[i]
                count = 1
            else:
                count += 1

        chars[j] = c
        j += 1
        if count > 1:
            for k in str(count):
                chars[j] = k
                j += 1

        return j
