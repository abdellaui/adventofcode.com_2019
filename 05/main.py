def first_task():
    with open('input.txt') as f:
        b = string_to_instruction_buffer(f.readline())
        process(b)
        return "Done"


def string_to_instruction_buffer(commastring):
    return [int(i) for i in commastring.split(",")]


def process(buffer):

    i_pointer = 0
    while i_pointer + 3 < len(buffer):

        op_str = str(buffer[i_pointer]).zfill(5)
        current_op = int(op_str[3:5])

        first_mode = int(op_str[2:3])
        second_mode = int(op_str[1:2])
        third_mode = int(op_str[0:1]) or True

        first_param_p = buffer[i_pointer + 1]
        second_param_p = buffer[i_pointer + 2]
        third_param_p = buffer[i_pointer + 3]

        first_param = first_param_p if first_mode else buffer[first_param_p]
        second_param = second_param_p if second_mode else buffer[second_param_p]
        third_param = third_param_p if third_mode else buffer[third_param_p]

        if current_op == 1:

            buffer[third_param_p] = first_param + second_param
            pointer_velocity = 4

        elif current_op == 2:

            buffer[third_param_p] = first_param * second_param
            pointer_velocity = 4

        elif current_op == 3:

            buffer[first_param_p] = int(input("Input (int):"))
            pointer_velocity = 2

        elif current_op == 4:
            print(buffer[first_param_p])
            pointer_velocity = 2

        elif current_op == 5:  # jump if true
            if first_param:
                i_pointer = second_param
                pointer_velocity = 0
            else:
                pointer_velocity = 3

        elif current_op == 6:  # jump if false
            if not first_param:
                i_pointer = second_param
                pointer_velocity = 0
            else:
                pointer_velocity = 3

        elif current_op == 7:  # less than
            buffer[third_param_p] = int(first_param < second_param)
            pointer_velocity = 4


        elif current_op == 8:  # eq than
            buffer[third_param_p] = int(first_param == second_param)
            pointer_velocity = 4

        elif current_op == 99:
            return ",".join([str(i) for i in buffer])
            # pointer_velocity = 1

        else:
            print("something went wrong!")
            pointer_velocity = 4

        i_pointer += pointer_velocity


if __name__ == '__main__':
    print("first_task: ", first_task())
