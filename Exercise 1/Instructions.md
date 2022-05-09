1.	Write the search.py program that executes the search, as taught in the lecture *. The program will contain one function: search (n: int) that solves a n-size problem. The function prints the initial (random) state and returns the target state. The function will check whether a given state is a target state after it is pulled out of the data structure.
2.	Modify the data structure to save the number of states stored in the structure. As a result, the frontier will include 5 items and not 4:
 ]#stack, max. depth, init. state, try next level?, total items pushed]
3.	Write software that will emit the maximum depth and number of tests (items) on average from 100 runs. The output can be for search (2):
Average depth 1.83
Average number 6.39
4.	Run search (2), search (3) and search (4), 
what is your conclusion?

stack.py – implementation the data structure: stack.

frontier.py – Implementing an ID data structure: an "elaborate" stack - a stack that stores states up to depth of search d. when it is depleted it re-claims the initial state and increases d by 1.


state.py – Implementing an nXn N-Puzzle mode.
