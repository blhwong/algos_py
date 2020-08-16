from algo_exp.calendar_matching.main import calendarMatching


def test_1():
    calendar1 = [
        ['9:00', '10:30'],
        ['12:00', '13:00'],
        ['16:00', '18:00'],
    ]
    daily_bounds_1 = ['9:00', '20:00']
    calendar2 = [
        ['10:00', '11:30'],
        ['12:30', '14:30'],
        ['14:30', '15:00'],
        ['16:00', '17:00'],
    ]
    daily_bounds_2 = ['10:00', '18:30']
    meeting_duration = 30
    result = calendarMatching(
        calendar1,
        daily_bounds_1,
        calendar2,
        daily_bounds_2,
        meeting_duration,
    )
    expected = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
    assert result == expected

def test_2():
    calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
    calendar2 = [
        ["10:00", "11:30"],
        ["12:30", "14:30"],
        ["14:30", "15:00"],
        ["16:00", "17:00"]
    ]
    daily_bounds_1 = ['9:00', '20:00']
    daily_bounds_2 = ['10:00', '18:30']
    meeting_duration = 45
    result = calendarMatching(
        calendar1,
        daily_bounds_1,
        calendar2,
        daily_bounds_2,
        meeting_duration
    )
    expected = [["15:00", "16:00"]]
    assert result == expected

def test_3():
    calendar1 = [
        ["10:00", "10:30"],
        ["10:45", "11:15"],
        ["11:30", "13:00"],
        ["14:15", "16:00"],
        ["16:00", "18:00"]
    ]
    calendar2 = [
        ["10:00", "11:00"],
        ["12:30", "13:30"],
        ["14:30", "15:00"],
        ["16:00", "17:00"]
    ]
    daily_bounds_1 = ["9:30", "20:00"]
    daily_bounds_2 = ["9:00", "18:30"]
    meeting_duration = 15
    result = calendarMatching(
        calendar1,
        daily_bounds_1,
        calendar2,
        daily_bounds_2,
        meeting_duration
    )
    expected = [["9:30", "10:00"], ["11:15", "11:30"],
                ["13:30", "14:15"], ["18:00", "18:30"]]
    assert result == expected
