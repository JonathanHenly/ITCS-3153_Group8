#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:21:43 2019

@author: qiaoshulin
"""

import math
from queue import PriorityQueue

class Node:
    # takes grid object
    def __init__(self, gridObj, location, parentNode, isGreedy):
        self.location = location
        self.value = gridObj.getValue(location)
        self.parent = parentNode
        self.isGreedy = isGreedy
        
        self.heuristicCost = self.distance()
        if parentNode:
            self.pathCost = self.parent.pathCost + 1
        else:
            self.pathCost = 0
        self.aStarCost = self.heuristicCost + self.pathCost
        
    #double h = heuristic cost of the node using mahattan distance
    def distance (self):
        p1 = self.location
        p2 = gridObj.goal
        distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
    
        return distance

    def __lt__(self, other):
        if self.isGreedy:
            return self.heuristicCost < other.heuristicCost
        else:
            return self.aStarCost < other.aStarCost

class Grid:
    def __init__(self, filename):
        self.grid = self.readGrid(filename)
        self.totalRow = len(self.grid)
        self.totalCol = len(self.grid[0])
        
    def setStart(self, startPt):
        self.start = startPt
        
    def setGoal(self, goalPt):
        self.goal = goalPt
        
    def readGrid(self, filename):
        f = open(filename, 'r')
        grid = []
        content = f.readlines()
        
        for line in content:
            grid.append(line.split())
            
        return grid
    
    def modifyGrid(self, location, newValue):
        self.grid[location[0]][location[1]] = newValue
        
    def getValue(self, location):
        return self.grid[location[0]][location[1]]
    
    def recordPath(self, path):
        for pt in path:
            self.modifyGrid(pt, "*")
        
        self.modifyGrid(self.start, "S")
        self.modifyGrid(self.goal, "G")

    def writeGrid(self, filename="output.txt"): 
        f = open(filename, "w")
        gridString = ""
        
        for row in self.grid:
            row = ' '.join(row)
            gridString += row
            gridString += "\n"
            
        f.write(gridString)
    
def GetChildren(gridObj, parent, isGreedy):
    children = []
    rowIndex = parent.location[0]
    colIndex = parent.location[1]
    
    # Check Right
    if (colIndex + 1 < gridObj.totalCol):
        val = gridObj.getValue([rowIndex, colIndex + 1])
        if (val == '0'):
            node = Node(gridObj, [rowIndex, colIndex + 1], parent, isGreedy)
            children.append(node)
            
    # Check Down
    if (rowIndex + 1 < gridObj.totalRow):
        val = gridObj.getValue([rowIndex + 1, colIndex])
        if (val == '0'):
            node = Node(gridObj, [rowIndex + 1, colIndex], parent, isGreedy)
            children.append(node)
            
    # Check Left
    if (colIndex - 1 >= 0):
        val = gridObj.getValue([rowIndex, colIndex - 1])
        if (val == '0'):
            node = Node(gridObj, [rowIndex, colIndex - 1], parent, isGreedy)
            children.append(node)
            
    # Check Up
    if (rowIndex - 1 >= 0):
        val = gridObj.getValue([rowIndex - 1, colIndex])
        if (val == '0'):
            node = Node(gridObj, [rowIndex - 1, colIndex], parent, isGreedy)
            children.append(node)
    
    # Return list of children
    return children

def ContainNode(ls, node):
    for n in ls:
        if node.location == n.location:
            return True
    return False

def ExpandNode(gridObj, node, visitedNodes, isGreedy):
    children = GetChildren(gridObj, node, isGreedy)
    for index, child in enumerate(children):
        if ContainNode(visitedNodes, child):
            del children[index]
            break
    return children

def Search (gridObj, isGreedy):
    openList = PriorityQueue()
    visitedNodes = []
    
    startNode = Node(gridObj, gridObj.start, None, isGreedy)
    openList.put(startNode)
    
    endNode = None
    
    while not openList.empty():
        currentNode = openList.get()
        
        if currentNode.location == gridObj.goal:
            endNode = currentNode
            break
        
        visitedNodes.append(currentNode)

        chld = ExpandNode(gridObj, currentNode, visitedNodes, isGreedy)
        for node in chld:
            openList.put(node)

    
    print("Number of nodes Expanded:", len(visitedNodes))
    
    path = []
    
    if endNode:
        path.append(endNode.location)
        parent = endNode.parent
        while parent:
            path = [parent.location] + path
            parent = parent.parent
            
    return path

if __name__== "__main__":
    gridObj = Grid("./grid.txt")
    
    #print grid
    for row in gridObj.grid:
        print(' '.join(str(x) for x in row))
        
    #user input
    startRow = int(input("Row number of the starting postition (0-indexed): "))
    startCol = int(input("Column number of the starting postition (0-indexed): "))
    goalRow = int(input("Row number of the goal postition (0-indexed): "))
    goalCol = int(input("Col number of the goal postition (0-indexed): "))
    
    gridObj.start = [startRow, startCol]
    gridObj.goal = [goalRow, goalCol]
    searchM = input("Which searching method would you like (greedy/astar): ")
    
    isGreedy = (searchM == "greedy")
    
    path = Search(gridObj, isGreedy)
    
    if not path:
        print("We're not able to find a result.")
    else:
        gridObj.recordPath(path)
        for row in gridObj.grid:
            print(' '.join(str(x) for x in row))
        print("Path: ", path)
        gridObj.writeGrid()
    
