g = 0

def outer():
    n = 0
    def inner(commands):
        nonlocal n
        global g
        for scope, val in commands:
            val = int(val)
            if scope == "global":
                g += val
            elif scope == "nonlocal":
                n += val
            # local scope does nothing
        return n
    return inner

cmd_count = int(input())
commands = [input().split() for _ in range(cmd_count)]

n_final = outer()(commands)
print(f"{g} {n_final}")