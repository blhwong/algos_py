class DataCompressor:

    def __init__(self, margin_of_error):
        self.margin_of_error = margin_of_error

    @staticmethod
    def get_m(y1, y2, x1, x2):
        return (y2 - y1) / (x2 - x1)

    @staticmethod
    def get_b(y, m, x):
        return y - m*x

    @staticmethod
    def get_y(m, x, b):
        return m*x + b

    def is_within_margin(self, y, y_prime):
        margin = y * self.margin_of_error
        under = y - margin
        over = y + margin
        return under <= y_prime <= over

    def compress(self, data):
        compressed = [0]
        next_point = 1
        i = 2
        while i < len(data):
            idx = compressed[-1]
            coord = data[idx]
            x1, y1 = coord
            x2, y2 = data[i]
            m = self.get_m(y1, y2, x1, x2)
            within_margin = True
            b = self.get_b(y1, m, x1)
            for j in reversed(range(idx, i)):
                x, y = data[j]
                y_prime = self.get_y(m, x, b)
                if not self.is_within_margin(y, y_prime):
                    within_margin = False
                    compressed.append(next_point)
                    next_point = i + 1
                    i += 2
                    break
            if within_margin:
                next_point = i
                i += 1

        compressed.append(next_point)

        return [data[i] for i in compressed]


if __name__ == '__main__':
    dc = DataCompressor(0.1)
    print(dc.compress([
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
    ]))
