class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'[{self.start}, {self.end}]'

    def __eq__(self, interval):
        return self.start == interval.start and self.end == interval.end

    def print_interval(self):
        print('[' + str(self.start) + ', ' + str(self.end) + ']', end='')
