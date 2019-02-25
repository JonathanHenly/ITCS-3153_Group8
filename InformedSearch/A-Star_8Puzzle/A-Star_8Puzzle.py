#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Friday February 1 2019

@author: Group 8
"""

from queue import PriorityQueue
from enum import Enum

class Puzzle:
    """ A 3x3 8-puzzle grid where 0 represents the blank tile. """
    
    def __init__(self, puzzle):
        self.puzzle = puzzle
    
    def set_value(self, coords: tuple, value):
        """ Set the val of the specified (row, col) coordinates. """
        self.puzzle[coords[0]][coords[1]] = value
        
    def swap(self, loc_one : tuple, loc_two : tuple):
        """ Swap the values at loc_one and loc_two """
        one = self.puzzle[loc_one[0]][loc_one[1]]
        two = self.puzzle[loc_two[0]][loc_two[1]]
        
        self.puzzle[loc_one[0]][loc_one[1]] = two
        self.puzzle[loc_two[0]][loc_two[1]] = one
        
    def value_at(self, coords):
        """ Return the val at the specified (row, col) coordinates. """
        return self.puzzle[coords[0]][coords[1]]
    
    def loc_of_value(self, value):
        """ Return the (row, col) coordinates of a specified val. """
        for row in range(0, 3):
            for col in range(0, 3):
                rc = (row, col)
                if self.value_at(rc) == value:
                    return rc
        return None
    
    def print(self):            
        """ Print a string representation of this puzzle. """
        print(self.to_string())
    
    def clone(self):
        """ Make a deep copy of this puzzle. """
        return Puzzle([x[:] for x in self.puzzle])

    def __str__(self):
        """ Return a string representation of this puzzle. """
        return '\n'.join(' '.join(map(str, row)) for row in self.puzzle)
    
    def __eq__(self, other):
        """ Check for equality between Puzzle objects. """
        return self.puzzle == other.puzzle
    
    @classmethod
    def read_puzzle(cls, filename):
        """ Read a puzzle from a specified file. """
        
        puzzle = []
        with open(filename, 'r') as infile:
            for line in infile.readlines():
                puzzle.append(list(map(int, line.strip().split(' '))))
        return cls(puzzle)

    @staticmethod
    def write_puzzle(filename, puzzle):
        """ Write a puzzle to a specified file. """

        with open(filename, 'w') as outfile:
            outfile.write(str(puzzle))


class Node:
    """ Holds the value and parent as well as the g, h and f costs. """
    
    def __init__(self, value, parent, g_cost, h_cost):
        self.val = value
        self.parent = parent
        self.g = g_cost
        self.h = h_cost
        self.f = self.g + self.h
        
    def __eq__(self, other):
        """ Overridden equals comparator, returns self.val == other.val """
        return self.val == other.val
    
    def __lt__(self, other):
        """ Overridden less than comparator, returns self.f < other.f """
        return self.f < other.f
    
    def __gt__(self, other):
        """ Overridden less than comparator, returns self.f > other.f """
        return self.f > other.f
    
class Dir(Enum):
    UP = (1, 0)
    DOWN = (-1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class AStar:
    
    def __init__(self):
        self.open = PriorityQueue()
        self.steps = 0
        self.expanded = 0
        
    def search(self, initial : Puzzle, goal : Puzzle):
        """ Find the A* path with specified initial and goal 8-Puzzles. """
        goal_node = Node(goal, None, 0, 0)
        # calculate initial's city block heuristic
        root_h = AStar.calc_h(initial, goal)
        # create root node with initial 8 Puzzle and heuristic
        root = Node(initial, None, 0, root_h)
        
        # add root node to open priority queue
        self.open.put(root)
        
        while not self.open.empty():
            # get next node with lowest f cost
            node = self.open.get()
                
            # check if goal has been reached
            if node.h == goal_node.h:
                return node
            
            prev_loc = None
            if node.parent is not None:
                prev_loc = node.parent.val.loc_of_value(0)
                
            # expand this node
            children = AStar.get_children(node, goal_node, prev_loc)
            self.expanded += 1
            
            # add this node's children to priority queue
            for c in children:
                self.open.put(c)
        
        # return None if the A* path could not be found
        return None
        
    @staticmethod
    def get_children(node : Node, goal : Node, prev_loc : tuple):
        """ Returns the specified node's UP, DOWN, LEFT and RIGHT
            children.
        """
        # get node's blank tile coordinates
        t_loc = node.val.loc_of_value(0)
        children = []
        
        # iterate over UP, DOWN, LEFT, RIGHT coordinate tuples
        for dir in Dir:
            # calculate movement coordinates
            swap_loc = AStar.valid_swap_loc(dir.value, t_loc)
            
            # if movement coords are in bounds then create and append child
            if swap_loc is not None:
                # if movement coords are same as parent blank coords, continue
                if swap_loc == prev_loc:
                    continue
                
                # swap child's blank tile with UP, DOWN, LEFT or RIGHT tile
                child_val = node.val.clone()
                child_val.swap(t_loc, swap_loc)
                # calculate child's city block heuristic
                child_h = AStar.calc_h(child_val, goal.val)
                # append new child, with node as parent, to children
                children.append(Node(child_val, node, node.g + 1, child_h))
                
        return children
            
    
    @staticmethod
    def valid_swap_loc(dir : tuple, loc : tuple):
        """ Returns a coordinate tuple of a valid movement location
            or None if the location is out of bounds.
        """
        valid_loc = tuple(x + y for x, y in zip(dir, loc))
        for i in valid_loc:
            if i < 0 or i > 2:
                return None
        return valid_loc
        
    @staticmethod
    def calc_h(state : Puzzle, goal : Puzzle):
        """ Calculate the specified 8 Puzzle's city block heuristic
            based on the specified goal.
        """
        sum = 0
        for val in range(1, 9):
            s_loc = state.loc_of_value(val)
            g_loc = goal.loc_of_value(val)
            sum += abs(s_loc[0] - g_loc[0]) + abs(s_loc[1] - g_loc[1])

        return sum

def print_node_list(node : Node):
    if node is None:
        return
    else:
        print_node_list(node.parent)
    
    print(str(node.val), '\n')
    #print('node.h:', node.h, '\n')
        
def print_horiz(init : Puzzle, goal : Puzzle):
    """ Prints the initial and goal states side by side. """
    i_rows = str(init).split('\n')
    g_rows = str(goal).split('\n')
    for rows in zip(i_rows, g_rows):
        print('   '.join(rows))
        
def calc_city_block(init, goal):
    """ Calculate the city block heuristic based off initial and goal
    states.
    """
    sum = 0
    for val in range(1, 9):
        s_loc = init.loc_of_value(val)
        g_loc = goal.loc_of_value(val)
        sum += abs(s_loc[0] - g_loc[0]) + abs(s_loc[1] - g_loc[1])
    
    return sum

def append_file(filename, content):
    """ Write a puzzle to a specified file. """

    with open(filename, 'a') as outfile:
        outfile.write(content)

def main():
    """ Main entry point of the program. """
    #initial = Puzzle.read_puzzle('../zin/two.txt')
    #goal = Puzzle.read_puzzle('../zin/two_goal.txt')
    
    initial_file = str(input("Initial 8-Puzzle file path: "))
    goal_file = str(input("Goal 8-Puzzle file path: "))
    out_file = str(input("Output file path: "))
    
    initial = Puzzle.read_puzzle(initial_file)
    goal = Puzzle.read_puzzle(goal_file)
    
    print("Init:   Goal:")
    print_horiz(initial, goal)
    
    a = AStar()
    node = a.search(initial, goal)
    
    if node is not None:
        print("1.) Solution found: Yes")
        
        print("2.) Number of states expanded:", a.expanded)
        
        print("3.) Final path:")
        print_node_list(node)
        
        print("4.) Heuristic function used: City block heuristic")
        
        cur = node
        str_list = []
        while cur is not None:
            str_list.append(str(cur.val))    
            cur = cur.parent
            
        
        while len(str_list) > 0:
            append_file(out_file, f"{str_list.pop()}\n\n")
        
    else:
        print("1.) Solution found: No")
    
    
main()