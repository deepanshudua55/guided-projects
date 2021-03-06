# Sorting - Day 1

## Links

- [Cool interactive widget on Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms/intro-to-algorithms/a/a-guessing-game)
- [Big-O Cheatsheet](http://bigocheatsheet.com/)
- [Visualgo](https://visualgo.net/bn/sorting) will allow you to visualize sorting algorithms step-by-step (and other things too)
- [Log base 2 calculator](https://www.miniwebtool.com/log-base-2-calculator/)
- [Python tutor](http://pythontutor.com/visualize.html)

## Big O/Time Complexity

- What is the maximum amount of times that a function runs?
- Big O is the worst case. Big Theta is the average case and Big Omega is the best case.

### Big O Analysis

- First, use your gut feeling. How many iterations does the algorithm have to make?
- How does it scale when n gets large?

1. Compute the Big-O for each line in isolation
2. If something is in a loop, multiply the Big-O by that loop total.
3. If two things happen sequentially, add the Big-Os
4. Drop leading multiplicative constants from each Big-O.
5. From all the Big-Os, drop all but the biggest, dominating one.

## Why sorting?

- Sorting is important. In order to do binary searches our data must be sorted.
  - Sorting allows us to search our data much more efficiently.
- Sorting gives you practice implementing many subroutines that you will use when creating solutions to other algorithm problems.
  - Swapping elements in an array
  - Paritioning an array
  - Writing recursive functions
  - Randomization
- Sorting combines these subroutines together to create larger, more complex solutions.
