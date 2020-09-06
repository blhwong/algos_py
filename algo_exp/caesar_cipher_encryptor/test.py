from algo_exp.caesar_cipher_encryptor.main import caesar_cipher_encryptor


def test_1():
    assert caesar_cipher_encryptor('xyz', 2) == 'zab'
