# National Novel Generation Month 2014

## About

This novel, The Conversations of Florence and Makena, is about two elderly friends who were deeply involved in WWII and the Cold War, and are now trying to make a new life as they learn English.

The program uses Markov chains to create realistic lines. The corpus text uses historical speeches from various time periods and geographic areas.

## Usage

First, you need a file called `corpus.txt` that contains a bunch of text that will be used to create Markov chains. For The Conversations of Florence and Makena, it was full of historical speeches.

Then, run:

```
python generate.py
```

And the `novel` file will hold a new literary masterpiece.