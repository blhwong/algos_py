class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        i = 0

        while i < len(self.intervals) and self.intervals[i][1] <= start:
            i += 1

        if i == len(self.intervals):
            self.intervals.append([start, end])
            return True

        if end > self.intervals[i][0]:
            return False

        while i < len(self.intervals):
            saved_start, saved_end = self.intervals[i]
            self.intervals[i] = [start, end]
            start, end = saved_start, saved_end
            i += 1

        self.intervals.append([start, end])
        return True
