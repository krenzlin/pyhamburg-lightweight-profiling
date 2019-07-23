import time


def slow(i):
    time.sleep(0.001)
    return i


def medium(i):
    time.sleep(0.0001)
    return i


def fast(i):
    return i
    

def do_stuff():
    N = 10000
    for i in range(N):
        slow(i)
        medium(i)
        fast(i)
