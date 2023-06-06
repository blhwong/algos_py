from typing import List


class Solution:

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        alphabets_index = { letter: i for i, letter in enumerate(alphabets) }

        s = set()

        for word in words:
            morse = ""
            for char in word:
                morse += morse_list[alphabets_index[char]]
            s.add(morse)

        return len(s)
