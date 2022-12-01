from functools import reduce

def add_points(a, b):
    return (a[0] + b[0], a[1] + b[1])

deltas = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

def trace(moves):
    path = {}
    loc = (0, 0)
    steps = 0
    for move in moves:
        direction, dist = move[:1], int(move[1:])
        delta = deltas[direction]
        for i in range(1, dist+1):
            loc = add_points(loc, delta)
            steps += 1
            if loc not in path:
                path[loc] = steps
    return path

with open('input/03') as f:
    paths = [trace(line.strip().split(',')) for line in f]
    intersecting_points = reduce(set.intersection, (set(path) for path in paths))
    # dists = (abs(p[0]) + abs(p[1]) for p in intersecting_points)
    dists = (sum(path[p] for path in paths) for p in intersecting_points)
    print(min(dists))
