# The Challenge

We want you to create a command-line application that will calculate the
ranking table for a soccer league.


## Table of contents
- [The Challenge](#the-challenge)
  * [Expected input and output](#expected-input-and-output)
  * [The rules](#the-rules)
  * [Guidelines](#guidelines)
    + [After you finish](#after-you-finish)
  * [What to send back to our team](#what-to-send-back-to-our-team)
    + [Platform support](#platform-support)
    + [What to expect afterwards](#what-to-expect-afterwards)

## Expected input and output

You can find the [sample-input.txt](sample-input.txt) and [expected-output.txt](expected-output.txt) files at the top of this repository

The input and output will be text. Your solution should parse the provided `sample-input.txt` file via stdin (pipe or redirect)or by parsing a file passed by name on the command line. Your solution should output the correct result via stdout to the console.

The input contains results of games, one per line. See `sample-input.txt` for details. The output should be ordered from most to least points, following the format specified in `expected-output.txt`.

You can expect that the input will be well-formed. There is no need to add
special handling for malformed input files.

## The rules

In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0 points. If two or more teams have the same number of points, they should have the same rank and be printed in alphabetical order (as in the tie for 3rd place in the sample data). Ranks are assigned according to [standard competition (1224) ranking](https://en.wikipedia.org/wiki/Ranking#Standard_competition_ranking_(%221224%22_ranking)).

We expect the resulting output of the provided `sample-input.txt` file to *exactly match the contents* of `expected-output.txt`.

## Guidelines

For the programming languages allowed we would prefer that you use Python. If Python is not a programming language that you use often, please choose a language that is both comfortable for you and suited to the task. However _we would be very impress_ if you are able to submit the challenge in a pythonic fashion (don't worry we would be rating your submission keeping this in mind!).

Your solution should be able to be run (and if applicable, built) from the command line. Please include appropriate scripts and instructions for running your application and your tests.

If you use other libraries installed by a common package manager (pip, poetry, npm, gradle, etc.), it is not necessary to commit the installed packages.

We write automated tests and *we would like you to do so as well*.

We appreciate well factored, object-oriented or functional designs.

We request that you spend no more than a few hours on this portion of the interview ( <= 3 hours is what we expect).

### After you finish

- Please document any steps necessary to run your solution and your tests.
- Please take 10 minutes to review your submission and list a few areas that would benefit from more time and attention.

## What to send back to our team

Please send an email back to your point of contact with:

- the code you used to calculate the rankings
- your test suite code
- simple instructions on how to install and use your code
- the amount of time you spent on the project
- the list of improvements you would make

> You can send us the submission in the form of a tarball, zip file, or a Github link to your repository.

### Platform support

This will be run in a unix-ish environment (OS X or Linux).
Please use platform-agnostic constructs where possible (line-endings and file-path-separators are two problematic areas).

### What to expect afterwards

Once you have sent us your project, we will review the code with our team members and rate it appropiately.
If everything looks fine, we would like to have a code review interview with you where we will be going over what you sent us, as well as requesting a few changes in the code to see if the output can be altered. An example of what you can be expecting can be seen in this documentation: [goal-differential-instructions.md](goal-differential-instructions.md)

# Instructions

## Dependencies

- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

## Getting Started

```bash
# Creates virtual environment/downloads dev dependencies
# Installs the code as a package
# Sets up pre-commit hooks
make init

# Run the package (args have defaults)
radai --input-file=./sample-input.txt

# Run all tests
make test

# Clean-up virtual environment
make deinit
```
