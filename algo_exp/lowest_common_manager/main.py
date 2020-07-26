def getLowestCommonManagerByOrgInfo(topManager, reportOne, reportTwo):
    def solve(curr):
        relevant_reports = 0
        for report in curr.directReports:
            ans, lower_reports = solve(report)
            if ans:
                return ans, lower_reports
            relevant_reports += lower_reports

        if curr == reportOne or curr == reportTwo:
            relevant_reports += 1

        ans = curr if relevant_reports == 2 else None
        return ans, relevant_reports


    return solve(topManager)[0]

def getLowestCommonManagerByCommonAncestor(topManager, reportOne, reportTwo):
    def populate_ancestor(curr, prev, level):
        if not curr:
            return
        curr.ancestor = prev
        curr.level = level
        for child in curr.directReports:
            populate_ancestor(child, curr, level + 1)

    populate_ancestor(topManager, None, 0)

    curr1, curr2 = reportOne, reportTwo

    while curr1.level > curr2.level:
        curr1 = curr1.ancestor

    while curr2.level > curr1.level:
        curr2 = curr2.ancestor

    while curr1 != curr2:
        curr1 = curr1.ancestor
        curr2 = curr2.ancestor

    return curr1


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
