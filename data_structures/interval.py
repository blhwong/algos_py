class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print('[' + str(self.start) + ', ' + str(self.end) + ']', end='')

    @staticmethod
    def compare(intervals1, intervals2):
        if len(intervals1) != len(intervals2):
            return False
        for idx, val in enumerate(intervals1):
            start1, end1 = intervals1[idx].start, intervals1[idx].end
            start2, end2 = intervals2[idx].start, intervals2[idx].end
            if start1 != start2 or end1 != end2:
                return False

        return True
