#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:11:04 2019

@author: qiaoshulin
"""

class Node:
    def __init__(self, location, value, parent):
        self.location = location
        self.value = value
        self.parent = parent
        

def ReadGrid(filename):
    f = open(filename, 'r')
    grid = []
    content = f.readlines()
    
    for line in content:
        grid.append(line.split())
        
    return grid

def ModifyGrid(grid, location, value):
    rowIndex = location[0]
    colIndex = location[1]
    grid[rowIndex][colIndex] = value
    
def GetValue(grid, location):
    rowIndex = location[0]
    colIndex = location[1]
    return grid[rowIndex][colIndex]

def RecordPath(grid, start, goal, path):
    for pt in path:
        ModifyGrid(grid, pt, "*")
    
    ModifyGrid(grid, start, "S")
    ModifyGrid(grid, goal, "G")

def WriteGrid(grid, filename="output.txt"): 
    f = open(filename, "w")
    gridString = ""
    
    for row in grid:
        row = ' '.join(row)
        gridString += row
        gridString += "\n"
        
    f.write(gridString)
    
def GetChildren(grid, parent):
    children = []
    rowIndex = parent.location[0]
    colIndex = parent.location[1]
    if (rowIndex - 1 >= 0):
        val = grid[rowIndex - 1][colIndex]
        if (val == '0'):
            node = Node([rowIndex - 1, colIndex], val, parent)
            children.append(node)
    if (rowIndex + 1 < len(grid[0])):
        val = grid[rowIndex + 1][colIndex]
        if (val == '0'):
            node = Node([rowIndex + 1, colIndex], val, parent)
            children.append(node)
    if (colIndex - 1 >= 0):
        val = grid[rowIndex][colIndex - 1]
        if (val == '0'):
            node = Node([rowIndex, colIndex - 1], val, parent)
            children.append(node)
    if (colIndex + 1 < len(grid)):
        val = grid[rowIndex][colIndex + 1]
        if (val == '0'):
            node = Node([rowIndex, colIndex + 1], val, parent)
            children.append(node)
        
    return children

def ContainNode(ls, node):
    for n in ls:
        if node.location == n.location:
            return True
    return False

def ExpandNode(grid, node, visitedNodes):
    children = GetChildren(grid, node)
    for index, child in enumerate(children):
        if ContainNode(visitedNodes, child):
            del children[index]
            break
    return children

#def BFS(grid, startPos, goalPos):
#    ls = []
#    visitedNodes = []
#    startNode = Node(startPos, GetValue(grid, startPos), None)
#    ls.append(startNode)
#    while ls:
#        node = ls[0]
#        del ls[0]
#        visitedNodes.append(node)
#        if node.location == goalPos:
#            endNode = node
#            break
#        else:
#            ls += ExpandNode(grid, node, visitedNodes)
#        endNode = None
#        
#    path = []
#    if endNode:
#        path.append(endNode.location)
#        parent = endNode.parent
#        while parent:
#            path = [parent.location] + path
#            parent = parent.parent
#    return path
#
#def DFS(grid, startPos, goalPos):
#    ls = []
#    visitedNodes = []
#    startNode = Node(startPos, GetValue(grid, startPos), None)
#    ls.append(startNode)
#    while ls:
#        node = ls[-1]
#        del ls[-1]
#        visitedNodes.append(node)
#        if node.location == goalPos:
#            endNode = node
#            break
#        else:
#            ls += ExpandNode(grid, node, visitedNodes)
#        endNode = None
#        
#    path = []
#    if endNode:
#        path.append(endNode.location)
#        parent = endNode.parent
#        while parent:
#            path = [parent.location] + path
#            parent = parent.parent
#    return path

def Search (grid, startPos, goalPos, searchingMethod):
    ls = []
    visitedNodes = []
    startNode = Node(startPos, GetValue(grid, startPos), None)
    ls.append(startNode)
    while ls:
        # Searching Branch
        if searchingMethod == "BFS":
            node = ls[0]
            del ls[0]
        else:
            node = ls[-1]
            del ls[-1]
            
        if not ContainNode(visitedNodes, node):
            visitedNodes.append(node)

        if node.location == goalPos:
            endNode = node
            break
        else:
            ls += ExpandNode(grid, node, visitedNodes)
        endNode = None
        
    print("Number of Expanded Nodes during the search:", len(visitedNodes))
    
    path = []
    if endNode:
        path.append(endNode.location)
        parent = endNode.parent
        while parent:
            path = [parent.location] + path
            parent = parent.parent
    return path

if __name__== "__main__":
    grid = ReadGrid("./grid.txt")
    #print grid
    for row in grid:
        print(' '.join(str(x) for x in row))
    startRow = int(input("Row number of the starting postition (0-indexed): "))
    startCol = int(input("Column number of the starting postition (0-indexed): "))
    goalRow = int(input("Row number of the goal postition (0-indexed): "))
    goalCol = int(input("Col number of the goal postition (0-indexed): "))
    startPos = [startRow, startCol]
    goalPos = [goalRow, goalCol]
    searchM = input("Which searching method would you like (BFS/DFS): ")
    path = Search(grid, startPos, goalPos, searchM)
    if not path:
        print("path is not found.")
    else:
        RecordPath(grid, startPos, goalPos, path)
        for row in grid:
            print(' '.join(str(x) for x in row))
        print("Path: ", path)
        WriteGrid(grid, "./output.txt")
    
