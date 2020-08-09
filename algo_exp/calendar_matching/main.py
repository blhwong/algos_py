def get_intersection(interval1, interval2, duration):
    merged_intervals = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(interval1) and j < len(interval2):
        a = interval1[i]
        b = interval2[j]

        a_starts_with_b = b[start] <= a[start] < b[end]
        b_starts_with_a = a[start] <= b[start] < a[end]

        a_and_b_overlap = a_starts_with_b or b_starts_with_a

        if a_and_b_overlap:
            slot = [max(a[start], b[start]), min(a[end], b[end])]
            if slot[1] - slot[0] >= duration:
                merged_intervals.append(slot)

        if a[end] < b[end]:
            i += 1
        else:
            j += 1

    return merged_intervals

def get_availability(interval, bounds, duration):
    if not interval:
        return [bounds]
    earliest, latest = bounds
    start, end = 0, 1
    availability = []
    i = 1

    if earliest + duration <= interval[0][start]:
        availability.append([earliest, interval[0][start]])

    while i < len(interval):
        if interval[i - 1][end] + duration <= interval[i][start]:
            availability.append([interval[i - 1][end], interval[i][start]])
        i += 1

    if interval[i - 1][end] + duration <= latest:
        availability.append([interval[i - 1][end], latest])


    return availability

def time_to_minutes(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

def minutes_to_time(minutes):
    hour_string = str(minutes // 60)
    min_string = str(minutes % 60).zfill(2)
    return f'{hour_string}:{min_string}'

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    min1 = [[time_to_minutes(start), time_to_minutes(end)] for start, end in calendar1]
    min2 = [[time_to_minutes(start), time_to_minutes(end)] for start, end in calendar2]
    d1 = [time_to_minutes(i) for i in dailyBounds1]
    d2 = [time_to_minutes(i) for i in dailyBounds2]
    a1 = get_availability(min1, d1, meetingDuration)
    a2 = get_availability(min2, d2, meetingDuration)
    intersection = get_intersection(a1, a2, meetingDuration)
    return [[minutes_to_time(start), minutes_to_time(end)] for start, end in intersection]
