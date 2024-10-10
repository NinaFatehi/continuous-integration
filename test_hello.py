from hello import more_hello, more_goodbye, add


def test_more_hello():
    assert "hi" == more_hello()


def test_more_goodbye():
    assert "bye" == more_goodbye()

def test_add():
    assert int(2)==add(1,1)
