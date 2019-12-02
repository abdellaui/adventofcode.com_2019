"""
Fuel required to launch a given module is based on its mass. 
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
"""

def first_step():
    with open('input') as f:
        return sum([(int(module[:-1])//3)-2 for module in f ])

def second_step():
    with open('input') as f:
        return sum([helper_recrusiv_calculation(int(module[:-1])) for module in f ])

def helper_recrusiv_calculation(rest_mass):
    fuel = (rest_mass//3)-2
    if fuel<=2:
        return max(0, fuel)

    return helper_recrusiv_calculation(fuel) + fuel

if __name__ == '__main__':
    print("first_step: ", first_step())
    print("second_step: ", second_step())