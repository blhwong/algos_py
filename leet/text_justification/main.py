import math
from typing import List

class Solution:

    def justify(self, max_width, line, last_line):
        word_count, words = line
        if last_line:
            return ' '.join(words).ljust(max_width)
        if len(words) == 1:
            return words[0].ljust(max_width)

        justified = ''
        spaces_left = max_width - word_count
        space_count = len(words) - 1
        width = math.ceil((spaces_left) / space_count)

        for word in words:
            spaces = ' ' * width
            justified += (word + spaces)
            spaces_left -= width
            space_count -= 1
            width = math.ceil(spaces_left / space_count) if space_count else 0

        return justified


    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = []
        word_count = 0
        for word in words:
            if word_count + len(line) + len(word) > maxWidth:
                lines.append((word_count, line))
                line = [word]
                word_count = len(word)
            else:
                line.append(word)
                word_count += len(word)

        lines.append((word_count, line))
        ans = [self.justify(maxWidth, line, idx == len(lines) - 1) for idx, line in enumerate(lines)]
        return ans
