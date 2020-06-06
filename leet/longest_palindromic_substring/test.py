from unittest import TestCase, main
from leet.longest_palindromic_substring.main import Solution

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(s.longestPalindrome('babad') in ['bab', 'aba'])

    def test_2(self):
        self.assertEqual('bb', s.longestPalindrome('cbbd'))

    def test_3(self):
        self.assertEqual('', s.longestPalindrome(''))

    def test_4(self):
        self.assertEqual('a', s.longestPalindrome('a'))

    def test_4(self):
        self.assertEqual('bb', s.longestPalindrome('bb'))

    def test_5(self):
        self.assertEqual('gykrkyg', s.longestPalindrome('zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir'))

    def test_6(self):
        self.assertEqual('adada', s.longestPalindrome('babadada'))

    def test_7(self):
        self.assertEqual('bb', s.longestPalindrome('abb'))


if __name__ == '__main__':
    main()
