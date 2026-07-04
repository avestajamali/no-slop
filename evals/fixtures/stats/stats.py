def mean(xs):
    t = 0
    n = 0
    for x in xs:
        t = t + x
        n = n + 1
    if n == 0:
        return None
    return t / n


def median(xs):
    n = len(xs)
    if n == 0:
        return None
    return xs[n // 2]
