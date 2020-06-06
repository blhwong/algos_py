from unittest import TestCase, main
from leet.valid_palindrome.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(False, s.isPalindrome('babad'))

    def test_2(self):
        self.assertEqual(False, s.isPalindrome('cbbd'))

    def test_3(self):
        self.assertEqual(True, s.isPalindrome(''))

    def test_4(self):
        self.assertEqual(True, s.isPalindrome('a'))

    def test_4(self):
        self.assertEqual(True, s.isPalindrome('bb'))

    def test_5(self):
        self.assertEqual(False, s.isPalindrome('zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir'))

    def test_6(self):
        self.assertEqual(False, s.isPalindrome('babadada'))

    def test_7(self):
        self.assertEqual(False, s.isPalindrome('abb'))

    def test_8(self):
        self.assertEqual(True, s.isPalindrome('A man, a plan, a canal: Panama'))

    def test_9(self):
        self.assertEqual(False, s.isPalindrome('race a car'))

    def test_10(self):
        self.assertEqual(True, s.isPalindrome('racecar'))

    def test_11(self):
        self.assertEqual(True, s.isPalindrome(' '))

    def test_12(self):
        self.assertEqual(False, s.isPalindrome('0P'))

if __name__ == '__main__':
    main()
