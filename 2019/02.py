def init_prog():
    with open('input/02') as f:
        return [int(x) for x in f.read().strip().split(',')]

def run_prog(prog, i1, i2):
    prog[1] = i1
    prog[2] = i2
    ip = 0
    while prog[ip] != 99:
        op = prog[ip]
        ia1, ia2, oa = prog[ip+1:ip+4]
        x = prog[ia1]
        y = prog[ia2]
        if op == 1:
            v = x + y
        else:
            v = x * y
        prog[oa] = v
        ip += 4
    return prog[0]

# print(run_prog(init_prog(), 12, 2))

for i in range(100):
    for j in range(100):
        prog = init_prog()
        res = run_prog(prog, i, j)
        if res == 19690720:
            print(100 * i + j)
