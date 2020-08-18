from algo_exp.airport_connections.main import airportConnections

airports = [
    'BGI',
    'CDG',
    'DEL',
    'DOH',
    'DSM',
    'EWR',
    'EYW',
    'HND',
    'ICN',
    'JFK',
    'LGA',
    'LHR',
    'ORD',
    'SAN',
    'SFO',
    'SIN',
    'TLV',
    'BUD',
]

def test_1():
    routes = [
        ['DSM', 'ORD'],
        ['ORD', 'BGI'],
        ['BGI', 'LGA'],
        ['SIN', 'CDG'],
        ['CDG', 'SIN'],
        ['CDG', 'BUD'],
        ['DEL', 'DOH'],
        ['DEL', 'CDG'],
        ['TLV', 'DEL'],
        ['EWR', 'HND'],
        ['HND', 'ICN'],
        ['HND', 'JFK'],
        ['ICN', 'JFK'],
        ['JFK', 'LGA'],
        ['EYW', 'LHR'],
        ['LHR', 'SFO'],
        ['SFO', 'SAN'],
        ['SFO', 'DSM'],
        ['SAN', 'EYW'],
    ]
    starting_airport = 'LGA'
    assert airportConnections(airports, routes, starting_airport) == 3

def test_2():
    routes = [['LGA', 'DSM'], ['LGA', 'ORD'], ['LGA', 'EYW']]
    starting_airport = 'LGA'
    assert airportConnections(airports, routes, starting_airport) == 14

def test_3():
    routes = [['LGA', 'DSM'], ['DSM', 'ORD'], ['LGA', 'EYW'], ['EYW', 'JFK'], ['EYW', 'EWR'], ['JFK', 'ICN']]
    starting_airport = 'LGA'
    assert airportConnections(airports, routes, starting_airport) == 11
