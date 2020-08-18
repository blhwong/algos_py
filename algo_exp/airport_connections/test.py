from algo_exp.airport_connections.main import airportConnections

def test_1():
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
