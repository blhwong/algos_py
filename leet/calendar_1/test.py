from leet.calendar_1.main import MyCalendar


def test_1():
    c = MyCalendar()
    assert c.book(10, 20) is True
    assert c.book(15, 25) is False
    assert c.book(20, 30) is True
    assert c.book(5, 10) is True
    assert c.book(0, 6) is False


def test_2():
    c = MyCalendar()
    assert c.book(47, 50) is True
    assert c.book(33, 41) is True
    assert c.book(39, 45) is False
    assert c.book(33, 42) is False
    assert c.book(25, 32) is True
    assert c.book(26, 35) is False
    assert c.book(19, 25) is True
    assert c.book(3, 8) is True
    assert c.book(8, 13) is True
    assert c.book(18, 27) is False
