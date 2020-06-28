from unittest import TestCase, main
from algo_exp.caesar_cipher_encryptor.main import caesarCipherEncryptor


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(caesarCipherEncryptor('xyz', 2), 'zab')


if __name__ == '__main__':
    main()
