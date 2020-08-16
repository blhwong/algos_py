from algo_exp.apartment_hunting.main import apartmentHunting


def test_1():
    result = apartmentHunting([
        { 'gym': False, 'school': True, 'store': False },
        { 'gym': True, 'school': False, 'store': False },
        { 'gym': True, 'school': True, 'store': False },
        { 'gym': False, 'school': True, 'store': False },
        { 'gym': False, 'school': True, 'store': True },
    ], ['gym', 'school', 'store'])
    assert result == 3
