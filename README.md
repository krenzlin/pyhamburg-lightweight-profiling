

# **premature optimization** is the root of all evil

Donald E. Knuth


    Programmers waste enormous amounts of time
    thinking about, or worrying about,
    the speed of noncritical parts of their programs.



# Is there a problem?

`$ time python main1.py`


# If yes, profile!

## timeit

`$ python -m timeit -s "import lib" "lib.do_stuff()"`

or if you know about the internals

`$ python -m timeit -s "import lib" "lib.fast()"`

`$ python -m timeit -s "import lib" "lib.medium()"`

`$ python -m timeit -s "import lib" "lib.slow()"`


## cProfile

`$ python -m cProfile -s cumulative main1.py`

[keys to sort by](https://docs.python.org/3.7/library/profile.html#pstats.Stats.sort_stats)

**but** overhead

`$ time python main1.py`

vs.

`$ time python -m cProfile -s cumulative main1.py`


# deterministic vs. statistical profiling**

## sample profiling

`python main2.py`

 `N = 10_000`

# Links

* original article - https://www.nylas.com/blog/performance/
* https://p403n1x87.github.io/python/profiling/2019/05/05/python-profiling.html
* FlameGraph - https://github.com/brendangregg/FlameGraph
