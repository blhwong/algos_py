class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev_num = self.reverse(num)
        return num == self.reverse(rev_num)

    def reverse(self, num):
        rev_num = ''
        for char in str(num):
            rev_num = f'{char}{rev_num}'
        return int(rev_num)
