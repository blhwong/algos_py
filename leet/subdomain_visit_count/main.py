from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        tracker = {}

        for pair in cpdomains:
            count_string, domain = pair.split(' ')
            parts = domain.split('.')
            for i in range(len(parts)):
                joined = '.'.join(parts[-1 - i:])
                if joined not in tracker:
                    tracker[joined] = 0
                tracker[joined] += int(count_string)

        for domain, count in tracker.items():
            ans.append(f'{count} {domain}')

        return ans
