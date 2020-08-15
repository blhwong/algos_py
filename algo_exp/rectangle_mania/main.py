"""
.   .   .   .
.   .   .   .
"""

UP = 'UP'
RIGHT = 'RIGHT'
DOWN = 'DOWN'
LEFT = 'LEFT'

next_direction_map = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
}

def get_direction(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    if x1 == x2:
        if y2 > y1:
            return UP
        if y2 < y1:
            return DOWN
    elif y1 == y2:
        if x2 > x1:
            return RIGHT
        if x2 < x1:
            return LEFT

    return ''

def get_coords_table(coords):
    coords_table = {}

    for coord1 in coords:
        x, y = coord1
        curr = { UP: [], RIGHT: [], DOWN: [], LEFT: []}
        for coord2 in coords:
            direction = get_direction(coord1, coord2)
            if direction in curr:
                curr[direction].append(coord2)

        coords_table[(x, y)] = curr

    return coords_table


def count_rectangles(start, curr, coords_table, direction):
    x, y = curr
    if direction == LEFT:
        return 1 if start in coords_table[(x, y)][LEFT] else 0

    next_direction = next_direction_map[direction]
    rectangles = 0

    for coord in coords_table[(x, y)][direction]:
        rectangles += count_rectangles(start, coord, coords_table, next_direction)

    return rectangles


def rectangleMania(coords):
    coords_table = get_coords_table(coords)
    ans = 0

    for coord in coords:
        ans += count_rectangles(coord, coord, coords_table, UP)

    return ans
