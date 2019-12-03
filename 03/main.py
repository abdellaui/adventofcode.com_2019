def first_task():
    with open('input.txt') as f:
        return min_dist(string_parser(f.read()))


def second_task():
    with open('input.txt') as f:
        return min_dist_between_intersections(string_parser(f.read()))


def string_parser(commastring):
    return [lines.split(",") for lines in commastring.splitlines()]


def get_trajectory(wire):
    trajectory = dict()
    current_coord = [0, 0]
    steps_left = 0
    for command in wire:
        direction = command[:1]
        steps = int(command[1:])
        for i in range(steps):
            if direction == "U":
                current_coord[0] += 1
            elif direction == "R":
                current_coord[1] += 1
            elif direction == "D":
                current_coord[0] -= 1
            elif direction == "L":
                current_coord[1] -= 1
            key = str(current_coord)
            steps_left += 1
            trajectory[key] = steps_left
    return trajectory


def calculate_intersections(wires):
    trajA = get_trajectory(wires[0])
    trajB = get_trajectory(wires[1])

    intersections = dict()

    for k, v in trajA.items():
        if k in trajB.keys():
            intersections[k] = v + trajB[k]

    return intersections



def min_dist(wires):
    intersections = calculate_intersections(wires)
    keys_to_array = [eval(k) for k in intersections.keys()] # keys are stored as string in form of arrays
    return min(abs(e[0]) + abs(e[1]) for e in keys_to_array)


def min_dist_between_intersections(wires):
    intersections = calculate_intersections(wires)
    return min(intersections.values())


if __name__ == '__main__':
    assert min_dist(string_parser("R8,U5,L5,D3\n" +
                                  "U7,R6,D4,L4")) == 6
    assert min_dist(string_parser("R75,D30,R83,U83,L12,D49,R71,U7,L72\n" +
                                  "U62,R66,U55,R34,D71,R55,D58,R83")) == 159
    assert min_dist(string_parser("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n" +
                                  "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")) == 135

    print("first_task: ", first_task())

    assert min_dist_between_intersections(string_parser("R75,D30,R83,U83,L12,D49,R71,U7,L72\n" +
                                                        "U62,R66,U55,R34,D71,R55,D58,R83")) == 610
    assert min_dist_between_intersections(string_parser("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n" +
                                                        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")) == 410

    print("second_task: ", second_task())
