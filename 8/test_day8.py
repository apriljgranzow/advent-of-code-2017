import solution as s

ex_text = '''
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''

def test_get_inputs():
    results = {
        0 : ('b', 'inc', '5', 'a', '> 1'),
        1 : ('a', 'inc', '1', 'b', '< 5'),
        2 : ('c', 'dec', '-10', 'a', '>= 1'),
        3 : ('c', 'inc', '1', 'c', '== 10')
    }
    inputs = s.get_inputs(ex_text)
    for i in range(len(inputs)):
        assert results[i] == inputs[i]