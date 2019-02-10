# Have fun and learn!

This is what this repository is all about.
After watching [this](https://www.youtube.com/watch?v=MYucYon2-lk), [this](https://www.youtube.com/watch?v=p84DMv8TQuo), [this](https://www.youtube.com/watch?v=jmsk1QZQEvQ), [this](https://www.youtube.com/watch?v=5pwv3cuo3Qk), [this](https://www.youtube.com/watch?v=lNITrPhl2_A) and [also this](https://www.youtube.com/watch?v=H18vxq-VsCk) I decided to experiment with property based tests and contracts. This repository is all about experimenting with that. In order to do that I am using a simple 2D vector library that I wrote in the past.

To make things even more fun I am going to experiment with several implementations of the 2D vector lib.

## How to run

This repository uses [pipenv](https://pipenv.readthedocs.io). Just run `pipenv install` on the root of this repository and everything will be setup. Then `pipenv shell` and `pytest` on the `src` folder. You can also run it the old school style (install the packages globaly).

## What I learned

1. Float arithmetic with fixed number of bits is weird.
2. Property based tests finds edge cases that you would (probably) never think of
3. Converting `int` to `float` can cause some unexpected errors (i.e. a number that can fit in an `int` but not a `float`)
4. Interfacing with objects in C makes it very hard to ensure that arithmetic works as expected. When passing numbers around it is very easy to lose precision when dealing with "big" numbers like 2^31. YMMV depending on archteture I guess. I am pretty much limiting the range of numbers that can be passed to C in order to avoid losing some bits around.
5. Achieving 100% test coverage with property based tests can be pretty brutal. Lots of edge cases to cover, some of which may be out of the intended use cases.

