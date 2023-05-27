from leet.sum_of_beauty_of_all_substrings.main import Solution


s = Solution()


def test_1():
    assert s.beautySum("aabcb") == 5


def test_2():
    assert s.beautySum("aabcbaa") == 17


def test_3():
    assert s.beautySum("woqrqcvfdgkrafoqdktsfpeygawfpdlvaylgpxhufpvucmmztjoqmxhegdpeczbtvwrmnwrvlptscwwqbjstanyqbgoagxopvgtlyzsemgktcgciualltsquepotmtszbmejbwbtzlavpxnujdsdyrypfcfcfwdidglybzvzuznytwndidzumoekzuukxtpouudsfcohapfcjjmqwjgcvalzarugmzucheydwsncxgyojnfvgroihfckmbtqewxhuqihplprgyeaqhocivaupdfokwpliziwcmuxnebxeszxbsrmffwwdz") == 293232
