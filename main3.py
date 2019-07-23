from sampler import Sampler
from pprint import pprint

import lib


if __name__ == "__main__":
    with Sampler(filename='profiler.out', save_on_exit=True) as sampler:
        lib.do_stuff()
        raise Exception
        