def factorial(n: int):
    a = 1
    for i in range(1, n+1):
        a *=i
    return a


def zeros(n):
    list_of = list(str(factorial(n)))
    count = 0
    for i in list_of[::-1]:
        if i == '0':
            count += 1
        else:
            break
    print(count)
    return count


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
