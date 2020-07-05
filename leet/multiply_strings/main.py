"""
      2 2
      1 2 3
      9 8 7

      8 6 1
    9 8 4 0
1 1 0 7 0 0

"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def get_sums(num1, num2):
            top, bottom = num1, num2
            if len(num2) > len(num1):
                top, bottom = num2, num1

            to_add = []
            carry = 0

            for i_idx in reversed(range(len(bottom))):
                curr = ''
                for j_idx in reversed(range(len(top))):
                    i = bottom[i_idx]
                    j = top[j_idx]
                    multiplied = int(i) * int(j) + carry
                    if multiplied >= 10 and j_idx != 0:
                        carry = multiplied // 10
                        multiplied %= 10
                    else:
                        carry = 0

                    curr = str(multiplied) + curr

                zeroes = '0' * (len(bottom) - i_idx - 1)
                add = curr + zeroes
                to_add.append(add.lstrip('0') or '0')
            if carry:
                zeroes = '0' * len(bottom)
                to_add.append(str(carry) + zeroes)
            return to_add

        def add(sums):
            ans = sums[0]

            for i in range(1, len(sums)):
                num = sums[i]
                top, bottom = num, ans
                if len(ans) > len(num):
                    top, bottom = ans, num

                rev_top = top[::-1]
                rev_bottom = bottom[::-1]

                carry = False
                curr = ''
                for j in range(len(top)):
                    upper = int(rev_top[j])
                    lower = int(rev_bottom[j]) if j < len(bottom) else 0

                    res = upper + lower
                    if carry:
                        res += 1

                    if res >= 10:
                        res -= 10
                        carry = True
                    else:
                        carry = False

                    curr = str(res) + curr

                if carry:
                    curr = '1' + curr
                ans = curr


            return ans

        sums = get_sums(num1, num2)
        return add(sums)
