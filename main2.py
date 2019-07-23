from sampler import Sampler
from pprint import pprint

import lib


if __name__ == "__main__":
    sampler = Sampler()
    sampler.start()

    lib.do_stuff()
    
    sampler.stop()
    pprint(sampler.stack_counts)

    sampler.save('profiler.out')
