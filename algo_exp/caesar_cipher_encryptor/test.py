from algo_exp.caesar_cipher_encryptor.main import caesarCipherEncryptor


def test_1():
    assert caesarCipherEncryptor('xyz', 2) == 'zab'
