# Have fun and learn!

This is what this repository is all about.
After watching [this](https://www.youtube.com/watch?v=MYucYon2-lk), [this](https://www.youtube.com/watch?v=p84DMv8TQuo), [this](https://www.youtube.com/watch?v=jmsk1QZQEvQ), [this](https://www.youtube.com/watch?v=5pwv3cuo3Qk), [this](https://www.youtube.com/watch?v=lNITrPhl2_A) and [also this](https://www.youtube.com/watch?v=H18vxq-VsCk) I decided to experiment with property based tests and contracts. This repository is all about experimenting with that. In order to do that I am using a simple 2D vector library that I wrote in the past.

To make things even more fun I am going to experiment with several implementations of the 2D vector lib.

## How to run

This repository uses [pipenv](https://pipenv.readthedocs.io). Just run `pipenv install` on the root of this repository and everything will be setup. Then `pipenv shell` and `pytest` on the `src` folder. You can also run it the old school style (install the packages globaly).

## What I learned

1. Float arithmetic with fixed number of bits is weird.
2. Property based tests finds edge cases that you would (probably) never think of
