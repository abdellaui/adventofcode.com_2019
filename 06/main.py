relation_map = dict()
reverse_map = dict()
depth_map = dict()
remember_map = dict()


def string_to_buffer(commastring):
    return [i.split(")") for i in commastring.splitlines()]


def first_task():
    global depth_map

    return sum(depth_map.values())


def second_task():
    global depth_map, remember_map

    _ = detect_intersection_point("SAN")
    intersection = detect_intersection_point("YOU")

    return depth_map["SAN"] + depth_map["YOU"] - 2*depth_map[intersection] - 2


def detect_intersection_point(key="YOU"):
    global reverse_map, remember_map

    for i in reverse_map.get(key, []):
        if remember_map.get(i, False):
            return i
        remember_map[i] = True
        return detect_intersection_point(i)




def resolve_depth(key, depth = 0):
    global relation_map, depth_map
    depth_map[key] = depth
    for k in relation_map.get(key, []):
        resolve_depth(k, depth+1)

def process(buffer):
    global relation_map, reverse_map
    for key, value in buffer:


        current_list = relation_map.get(key, list())
        current_list.append(value)
        relation_map[key] = current_list

        reverse_list = reverse_map.get(value, list())
        reverse_list.append(key)
        reverse_map[value] = reverse_list






if __name__ == '__main__':

    with open('input') as f:
        process(string_to_buffer(f.read()))
        resolve_depth("COM")

        print("first_task: ", first_task())

        print("second_task: ", second_task())
