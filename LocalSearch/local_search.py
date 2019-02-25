#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
local_search.py

Created on February 19, 2019

@author: Group 8
'''

import random
import math

from nqueens import Board
from nqueens import getSuccessorStates
from nqueens import numAttackingQueens


# Execute the instructions given in this assignment.
def main():
    board_sizes = [4, 8, 16]
    decay_rates = [0.9, 0.75, 0.5]
    thresholds = [1e-05, 1e-06, 1e-07]
    
    # iterate over board sizes and run simulation with each rate and threshold
    for size in board_sizes:
        print_board_size(size)
        
        for rate, threshold in zip(decay_rates, thresholds):            
            # run simulation with current board size, decay rate and threshold
            print_rate_thresh(rate, threshold)
            avg_h = run_sim_annealing(size, rate, threshold)
            
            print(f"Average h-cost of final solutions: {avg_h}")
    
# Function that executes multiple simulated annealing runs and returns the
# average final heuristic cost of the runs.
def run_sim_annealing(size, rate, threshold):
    NUM_RUNS = 10
    T_INIT = 100
    sum_h = 0
    
    for run in range(0, NUM_RUNS):
        # create a new board, randomize it and calculate its h cost
        current = Board(size)
        current.rand()
        current.h = numAttackingQueens(current)
        
        # output the run count and the initial board
        print(f"Run {run}\nInitial board:")
        current.printBoard()
        print(f"h-value: {current.h}")
        
        # initialize temperature
        T = T_INIT
        
        # Loop until temperature T reaches or falls beneath the threshold.
        # Once this occurs the final board, represented by current, has
        # been found.
        while T > threshold:
            # calculate temperature T using linear schedule: T * rate
            T = f(T, rate)
            
            # we've found the solution if current board's h cost is 0
            if current.h == 0:
                break;
            
            # set next_b to one of current's successors, chosen at random
            next_b = get_random_successor(current)
            next_b.h = numAttackingQueens(next_b)
            
            # calculate the h cost difference between current and next_b
            delta_E = current.h - next_b.h
            
            # if h cost difference greater than 0 or probability of move passes
            # then set current to next_b and continue loop
            if delta_E > 0:
                current = next_b
            elif random.random() < math.exp(delta_E / T):
                current = next_b
        
        # output final board's h cost and the final board
        print(f"Final board h value: {current.h}")
        current.printBoard()
        
        # add this run's final board h cost to the running sum
        sum_h += current.h

    # return the total average h cost: sum of h costs over number of runs
    return sum_h / NUM_RUNS


# Linear scheduling function, returns temperature T multiplied by decay rate.
def f(T, decay_rate):
    return T * decay_rate


# Returns one of a passed in board's successors, chosen at random.
def get_random_successor(board):
    successors = getSuccessorStates(board)
    return successors[random.randint(0, len(successors) - 1)]


# Print the board size surrounded by asterisk separators.
def print_board_size(size):
    sep = "**********************************"
    print(f"{sep}\nBoard size: {size}\n{sep}")

    
# Print the decay rate and threshold surrounded by number sign separators.
def print_rate_thresh(rate, threshold):
    sep = "######################################"
    print(f"{sep}\nDecay rate {rate} T Threshold: {threshold}\n{sep}")


# execute main() if this script is being run
if __name__ == "__main__":
    main()

