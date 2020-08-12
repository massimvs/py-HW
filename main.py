def secondary():
    print("Secondary")

def add(a, b):
    # return a + b
    print
    print("Add", a, b)
    res = a + b


def main():
    secondary()
    print('Hello main')

main()


def rain_today():
    res = ... # some web request to whether API
    if res.status == "OK"
        return res.data.will_rain
    # print
    return None

