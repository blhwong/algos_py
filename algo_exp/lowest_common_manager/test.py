from unittest import TestCase, main
from algo_exp.lowest_common_manager.main import getLowestCommonManagerByCommonAncestor, getLowestCommonManagerByOrgInfo, OrgChart

a = OrgChart('A')
b = OrgChart('B')
c = OrgChart('C')
d = OrgChart('D')
e = OrgChart('E')
f = OrgChart('F')
g = OrgChart('G')
h = OrgChart('H')
i = OrgChart('I')
a.directReports.append(b)
a.directReports.append(c)
b.directReports.append(d)
b.directReports.append(e)
d.directReports.append(h)
d.directReports.append(i)
c.directReports.append(f)
c.directReports.append(g)

class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(getLowestCommonManagerByCommonAncestor(a, e, i), b)

    def test_2(self):
        self.assertEqual(getLowestCommonManagerByOrgInfo(a, e, i), b)



if __name__ == '__main__':
    main()
