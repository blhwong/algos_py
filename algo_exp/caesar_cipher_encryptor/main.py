def caesarCipherEncryptor(string, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    array = list(alphabet)
    lookup = {key: idx for idx, key in enumerate(array)}
    ans = ''
    for char in string:
        idx = lookup[char]
        ans += array[(idx + key) % 26]
    return ans
