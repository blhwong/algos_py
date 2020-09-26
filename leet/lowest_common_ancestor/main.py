from data_structures.tree_node import TreeNode


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(curr, p, q):
            if not curr:
                return 0, None
            reports = 1 if curr in [p, q] else 0
            for child in [curr.left, curr.right]:
                r, lca = solve(child, p, q)
                if lca:
                    return r, lca
                reports += r

            if reports == 2:
                return r, curr
            return reports, None


        return solve(root, p, q)[1]
