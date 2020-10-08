from misc.data_compressor.main import DataCompressor




def test_1():
    data = [
        [0.00, 11.79],
        [2.62, 11.6],
        [5.03, 11.33],
        [7.05, 11.76],
        [9.48, 16.84],
        [12.48, 23.85],
        [15.15, 27.85],
        [17.98, 27.8],
        [20.29, 27.52],
        [22.47, 27.88],
        [24.65, 27.41],
    ]
    dc = DataCompressor(0.1)
    res = dc.compress(data)
    print(res)
    assert res == [
        [0.00, 11.79],
        [7.05, 11.76],
        [15.15, 27.85],
        [24.65, 27.41],
    ]
