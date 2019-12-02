def first_step():
    with open('input') as f:
        return sum([calculation(int(module[:-1])) for module in f])

def second_step():
    with open('input') as f:
        return sum([recrusiv_calculation(int(module[:-1])) for module in f])

def calculation(mass):
    return (mass//3)-2

def recrusiv_calculation(rest_mass):
    fuel = calculation(rest_mass)
    if fuel<=2:
        return max(0, fuel)

    return recrusiv_calculation(fuel) + fuel

if __name__ == '__main__':
    assert calculation(12) == 2
    assert calculation(14) == 2
    assert calculation(1969) == 654
    assert calculation(100756) == 33583

    print("first_step: ", first_step())

    assert recrusiv_calculation(14) == 2
    assert recrusiv_calculation(1969) == 966
    assert recrusiv_calculation(100756) == 50346

    print("second_step: ", second_step())