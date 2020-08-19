
def power(a, pow=2):
    return a ** pow


def count_values(counter, *args):
    return [counter(v) for v in args]

#def count_values(counter, *args):
#    return {v: counter(v) for v in args}


def main():
    res = count_values(power, 1, 2, 3, 5)
    print(res)

main()