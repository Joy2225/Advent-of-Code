import re
from z3 import *

def parse_input(input_text):
    machines = []
    machine_data = input_text.strip().split("\n\n")
    for data in machine_data:
        lines = data.splitlines()
        button_a = re.findall(r"X\+([0-9]+), Y\+([0-9]+)", lines[0])
        button_b = re.findall(r"X\+([0-9]+), Y\+([0-9]+)", lines[1])
        prize = re.findall(r"X=([0-9]+), Y=([0-9]+)", lines[2])
        machines.append((button_a[0], button_b[0], prize[0]))
    return machines

def solve_claw_machine(button_a, button_b, prize, max_presses):
    print(button_a, button_b, prize, max_presses)
    a_x, a_y = map(int, button_a)
    b_x, b_y = map(int, button_b)
    p_x, p_y = map(int ,prize)
    p_x+=10000000000000
    p_y+=10000000000000
    
    solver = Solver()

    x_a = Int('x_a')
    x_b = Int('x_b')

    solver.add(a_x * x_a + b_x * x_b == p_x)
    solver.add(a_y * x_a + b_y * x_b == p_y)

    solver.add(x_a >= 0)
    solver.add(x_b >= 0)

    if solver.check() == sat:
        model = solver.model()
        x_a_value = model[x_a].as_long()
        x_b_value = model[x_b].as_long()

        cost = 3 * x_a_value + 1 * x_b_value
        return cost, x_a_value, x_b_value
    return None  

def main():
    input_text = open("D13.txt").read()

    machines = parse_input(input_text)
    max_presses = 100
    total_tokens = 0
    prizes_won = 0

    for idx, (button_a, button_b, prize) in enumerate(machines):
        result = solve_claw_machine(button_a, button_b, prize, max_presses)
        if result:
            cost, x_a, x_b = result
            total_tokens += cost
            prizes_won += 1
            print(f"Machine {idx + 1}: Win with {x_a} presses of A and {x_b} presses of B, costing {cost} tokens.")
        else:
            print(f"Machine {idx + 1}: No solution.")

    print(f"\nTotal prizes won: {prizes_won}")
    print(f"Total tokens spent: {total_tokens}")

if __name__ == "__main__":
    main()
