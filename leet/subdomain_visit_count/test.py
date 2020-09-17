from unittest import TestCase, main
from leet.subdomain_visit_count.main import Solution


s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        result = s.subdomainVisits(['9001 discuss.leetcode.com'])
        expected = [
            '9001 discuss.leetcode.com',
            '9001 leetcode.com',
            '9001 com',
        ]
        self.assertCountEqual(result, expected)


    def test_2(self):
        result = s.subdomainVisits([
            '900 google.mail.com',
            '50 yahoo.com',
            '1 intel.mail.com',
            '5 wiki.org',
        ])
        expected = [
            '901 mail.com',
            '50 yahoo.com',
            '900 google.mail.com',
            '5 wiki.org',
            '5 org',
            '1 intel.mail.com',
            '951 com',
        ]
        self.assertCountEqual(result, expected)
