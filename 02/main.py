def first_task():
    with open('input.txt') as f:
        buffer = string_to_instruction_buffer(f.readline())
        # 1202 program alarm
        buffer[1] = 12
        buffer[2] = 2
        return process(buffer)


def second_task(noun, verb):
    with open('input.txt') as f:
        buffer = string_to_instruction_buffer(f.readline())
        # 1202 program alarm
        buffer[1] = noun
        buffer[2] = verb
        return process(buffer)


def operate(buffer, pointer, lambda_func):
    left_hand_p = buffer[pointer + 1]
    right_hand_p = buffer[pointer + 2]
    output_p = buffer[pointer + 3]
    buffer[output_p] = lambda_func(buffer[left_hand_p], buffer[right_hand_p])


def string_to_instruction_buffer(commastring):
    return [int(i) for i in commastring.split(",")]


def process(instruction_buffer):
    i_pointer = 0
    while i_pointer < len(instruction_buffer):
        current_op = instruction_buffer[i_pointer]

        if current_op == 1:
            operate(instruction_buffer, i_pointer, lambda a, b: a + b)

        elif current_op == 2:
            operate(instruction_buffer, i_pointer, lambda a, b: a * b)

        elif current_op == 99:
            return ",".join([str(i) for i in instruction_buffer])

        else:
            print("something went wrong!")

        i_pointer += 4


if __name__ == '__main__':
    assert process(string_to_instruction_buffer("1,0,0,0,99")) == "2,0,0,0,99"  # (1 + 1 = 2)
    assert process(string_to_instruction_buffer("2,3,0,3,99")) == "2,3,0,6,99"  # (3 * 2 = 6)
    assert process(string_to_instruction_buffer("2,4,4,5,99,0")) == "2,4,4,5,99,9801"  # (99 * 99 = 9801)
    assert process(string_to_instruction_buffer("1,1,1,4,99,5,6,0,99")) == "30,1,1,4,2,5,6,0,99"

    print("first_task: ", first_task())

    """
    # ctrl+c is your friend
    while True:
        noun = int(input("Enter noun: "))
        verb = int(input("Enter verb: "))
        print("second_task: ", second_task(noun, verb))
    """
    for noun in range(0, 100, 1):
        for verb in range(0, 100, 1):
            result = second_task(noun, verb).split(",")[0]
            if result == "19690720":
                print("second_task: ", result, noun, verb)
                break
