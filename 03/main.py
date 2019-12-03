def first_task():
    with open('input.txt') as f:
        return calc_min_dist(string_parser(f.read()))

def second_task():
    with open('input.txt') as f:
        return calc_dist(string_parser(f.read()))

def string_parser(commastring):
    return [lines.split(",") for lines in commastring.splitlines()]

def generate_histroy_map(wires):
    history_map = dict()
    for wire_index, commands in enumerate(wires):
        current_coord = [0, 0]
        for command in commands:
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

                # if key not exists, default value is wire_index
                # if value of key is NOT eq wire_index => 2 diff wires intersects
                history_map[key] = wire_index if history_map.get(key, wire_index) == wire_index else 'X'
    return history_map

def calc_min_dist(wires):
    history_map = generate_histroy_map(wires)

    min_distance = float("inf")
    for (k, v) in history_map.items():
        if v == 'X' and k != "[0, 0]":  # intersects and aren't origin
            coord = eval(k)  # from string-array to array
            distance = abs(coord[0]) + abs(coord[1])
            if distance < min_distance:
                min_distance = distance
                min_coord = coord
    return min_distance



def calc_min_dist_between_intersections(wires):
    history_map = generate_histroy_map(wires)
    min_steps = float("inf")
    for (k, v) in history_map.items():
        if v == 'X' and k != "[0, 0]":  # intersects and aren't origin
            intersection_point = eval(k)  # from string-array to array
            sum_step_for_intersection = 0
            for commands in wires:
                remember_steps_map = dict()
                current_coord = [0, 0]
                steps_amount = 0
                for command in commands:
                    key = str(current_coord)
                    steps_amount = remember_steps_map.get(key, steps_amount)

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

                        steps_amount += 1
                        remember_steps_map[key] = steps_amount

                        if current_coord == intersection_point:
                            sum_step_for_intersection += steps_amount
                            steps_amount = 0
                if min_steps > sum_step_for_intersection:
                    min_steps = sum_step_for_intersection
    return min_steps

if __name__ == '__main__':
    assert calc_min_dist(string_parser("R8,U5,L5,D3\n" +
                                 "U7,R6,D4,L4")) == 6
    assert calc_min_dist(string_parser("R75,D30,R83,U83,L12,D49,R71,U7,L72\n" +
                                 "U62,R66,U55,R34,D71,R55,D58,R83")) == 159
    assert calc_min_dist(string_parser("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n" +
                                 "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")) == 135

    print("first_task: ", first_task())

    print(calc_min_dist_between_intersections(string_parser("R75,D30,R83,U83,L12,D49,R71,U7,L72\n" +
                                 "U62,R66,U55,R34,D71,R55,D58,R83")))
    assert calc_min_dist_between_intersections(string_parser("R75,D30,R83,U83,L12,D49,R71,U7,L72\n" +
                                 "U62,R66,U55,R34,D71,R55,D58,R83")) == 610
    assert calc_min_dist_between_intersections(string_parser("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n" +
                                 "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")) == 410

    print("second_task: ", second_task())

