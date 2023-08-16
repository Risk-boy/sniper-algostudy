import sys

n = int(sys.stdin.readline().rstrip())

ex = sys.stdin.readline().rstrip()
start = int(ex[0])
ex = ex[1:]

op_len = n // 2


def find_max(i, result):
    index_op = i * 2

    if i == op_len:
        return result

    if i == op_len - 1:
        return eval("result " + ex[index_op] + ex[index_op + 1])

    return max(
        find_max(i + 1, eval("result" + ex[index_op : index_op + 2])),
        find_max(
            i + 2,
            eval("result" + ex[index_op] + "(" + ex[index_op + 1 : index_op + 4] + ")"),
        ),
    )


print(find_max(0, start))
