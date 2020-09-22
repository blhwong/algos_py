from leet.text_justification.main import Solution


s = Solution()


def test_1():
    result = s.fullJustify([
        'This',
        'is',
        'an',
        'example',
        'of',
        'text',
        'justification.',
    ], 16)
    expected = [
        'This    is    an',
        'example  of text',
        'justification.  '
    ]
    assert result == expected

def test_2():
    result = s.fullJustify([
        'What',
        'must',
        'be',
        'acknowledgment',
        'shall',
        'be',
    ], 16)
    expected = [
        'What   must   be',
        'acknowledgment  ',
        'shall be        '
    ]
    assert result == expected


def test_3():
    result = s.fullJustify([
        'Science',
        'is',
        'what',
        'we',
        'understand',
        'well',
        'enough',
        'to',
        'explain',
        'to',
        'a',
        'computer.',
        'Art',
        'is',
        'everything',
        'else',
        'we',
        'do',
    ], 20)
    expected = [
        'Science  is  what we',
        'understand      well',
        'enough to explain to',
        'a  computer.  Art is',
        'everything  else  we',
        'do                  '
    ]
    assert result == expected


def test_4():
    result = s.fullJustify([
        'The',
        'important',
        'thing',
        'is',
        'not',
        'to',
        'stop',
        'questioning.',
        'Curiosity',
        'has',
        'its',
        'own',
        'reason',
        'for',
        'existing.',
    ], 17)
    expected = [
        'The     important',
        'thing  is  not to',
        'stop questioning.',
        'Curiosity has its',
        'own   reason  for',
        'existing.        ',
    ]
    assert result == expected


def test_5():
    result = s.fullJustify([
        'ask',
        'not',
        'what',
        'your',
        'country',
        'can',
        'do',
        'for',
        'you',
        'ask',
        'what',
        'you',
        'can',
        'do',
        'for',
        'your',
        'country',
    ], 16)
    expected = [
        'ask   not   what',
        'your country can',
        'do  for  you ask',
        'what  you can do',
        'for your country',
    ]
    assert result == expected
