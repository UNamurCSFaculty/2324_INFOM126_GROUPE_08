def inc(x):
    return x + 1

def test_answer_OK():
    assert inc(3) == 5

def test_answer_KO():
    assert inc(3) == 4