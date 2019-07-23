
# Hamburg Python Meetup (2019-07-23) - Lightweight Profiling 

github.com/krenzlin/pyhamburg-lightweight-profiling

bit.ly/2K3Nixs

## **premature optimization** is the root of all evil

Donald E. Knuth (1974): "Computer Programming as an Art"


    Programmers waste enormous amounts of time
    thinking about, or worrying about,
    the speed of noncritical parts of their programs.

__ (1974): "Structured Programming with go to Statements"


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


# Statistical profiling

* trade accuracy for less overhead

## sample profiling

`python main2.py`

# Visualisation

* FlameGraph - https://github.com/brendangregg/FlameGraph

`$ ./flamegraph.pl profiler.out > graph.svg`


# Others

* [py-spy](https://github.com/benfred/py-spy)
  * hook into running python processes
  * threads
  * looks promising
* [austin](https://github.com/P403n1x87/austin)

# Sources

* Morikawa, Evan (2016): "Profiling Python in Production" [link](https://www.nylas.com/blog/performance/)
* Knuth, Donald E. (1974): "Computer programming as an art" [pdf](https://dl.acm.org/citation.cfm?id=361612)
* Knuth, Donald E. (1974): "Structured Programming with go to Statements" [link](http://www.kohala.com/start/papers.others/knuth.dec74.html)
* Tornetta, Gabriele N. (2019): "Deterministic and Statistical Python Profiling" https://p403n1x87.github.io/python/profiling/2019/05/05/python-profiling.html

