def groupAnagrams(words):
    tracker = {}
    for word in words:
        key = ''.join(sorted([char for char in word]))
        if key not in tracker:
            tracker[key] = []

        tracker[key].append(word)

    return list(tracker.values())
