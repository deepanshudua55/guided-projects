# Algorithms Day 1

## Links

- [Great video example of whiteboarding](https://www.youtube.com/watch?v=XKu_SEDAykw)

- [Big-O Notation](https://runestone.academy/runestone/static/pythonds/AlgorithmAnalysis/BigONotation.html)

- [Big-O Cheatsheet](http://bigocheatsheet.com/)

- [Polya's problem solving technique](https://math.berkeley.edu/~gmelvin/polya.pdf)

## What is an algorithm?

- A set of steps to solve a problem.
- A recipe.

## Why did we start with sorting?

- In sorting we practice:
  - swapping elements in an array
  - Partitioning an array
  - Writing recursive functions
  - Randomization
- Sorting algorithms combine all these core concepts together to make more complex solutions.

## How to solve algorithmic problems

1. Understand the problem. Ask clarifying questions.
2. Devise a plan. Write it out in sentences and pseudocode.
3. Carry out your plan. Write out the code.
4. Evaluate. Do the Big-O analysis. Try to optimize. Clean up your code where you can.

## Big O Review

1. Compute the Big-O of every individual line.
   - If something is in a loop, multiply its Big-O by the loop for the total.
2. If two things happen sequentially, add the Big-Os.
3. Drop leading multiplicative constants from each Big-O. O(2n) -> O(n)
4. From all the Big-Os that are added, drop all but the biggest dominating one.
