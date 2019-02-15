import solution as s

def test_no_dupe_words():
    examples = {
        'aa bb cc dd ee' : True,
        'aa bb cc dd aa' : False,
        'aa bb cc dd aaa' : True
    }
    for elem in examples:
        assert s.no_dupe_words(elem) == examples[elem]

def test_no_anagrams():
    examples = {
        'abcde fghij' : True,
        'abcde xyz ecdab' : False,
        'a ab abc abd abf abj' : True,
        'iiii oiii ooii oooi oooo' : True,
        'oiii ioii iioi iiio' : False
    }
    for elem in examples:
        assert s.no_anagram_words(elem) == examples[elem]