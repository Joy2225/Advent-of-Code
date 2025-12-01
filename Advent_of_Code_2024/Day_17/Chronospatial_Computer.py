def simulate(a):
    b=0
    c=0
    output = []
    while a!=0:
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ c
        b = b ^ 6
        a = a >> 3
        output.append(b%8)
    return output

print(simulate(51064159))
program = [2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0]

# Not my code. Credits:- mental-chaos(reddit)
def get_best_quine_input(program, cursor, sofar):
    for candidate in range(8):
        if simulate(sofar * 8 + candidate) == program[cursor:]:
            print(candidate)
            if cursor == 0:
                return sofar * 8 + candidate
            ret = get_best_quine_input(program, cursor - 1, sofar * 8 + candidate)
            if ret is not None:
                return ret
    return None

print(get_best_quine_input(program, len(program) - 1, 0))