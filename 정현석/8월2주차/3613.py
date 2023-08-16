import sys

variable = sys.stdin.readline().rstrip()


def contain_weird(v: str):
    if v[0].isupper():
        return True

    if v[0] == "_":
        return True

    if v[-1] == "_":
        return True

    prev = v[0]
    for c in v[1:]:
        if prev == "_" and c == "_":
            return True
        prev = c

    return False


def contain_capital(v: str):
    for c in v:
        if c.isupper():
            return True

    return False


def contain_underscore(v: str):
    for c in v:
        if c == "_":
            return True

    return False


weird = contain_weird(variable)
capital = contain_capital(variable)
underscore = contain_underscore(variable)

if weird or (capital and underscore):
    print("Error!")
elif capital:
    variable = list(variable)
    for i, c in enumerate(variable):
        if c.isupper():
            variable[i] = "_" + c.lower()
    print(*variable, sep="")
elif underscore:
    variable = variable.split("_")
    for i, w in enumerate(variable):
        if i:
            variable[i] = w.capitalize()
    print(*variable, sep="")
else:
    print(variable)
