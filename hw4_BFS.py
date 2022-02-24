# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:39:28 2020
homework4, algorithm 2020 fall
@author: Yun Xuan, Liang
Student no: S0661124
"""
class Node():
    """
        node be used for record:
            current positon 
            history of walked 
    """
    def __init__(self, position, history):
        self.position = position
        self.history = history
    
    def show(self):
        print(self.position, self.history)

    
def checking(point, matrix):
    def bound_checking(point, matrix):
        x = point[0]
        y = point[1]
        max_x = len(matrix)
        max_y = len(matrix[0])

        if(x < 0 or y < 0 or x >= max_x or y >= max_y):
            # print("bound_checking: out of bound.")
            return False
        return True

    def barrier_checking(point, matrix):
        r = point[0]
        c = point[1]
        return not matrix[r][c]
    return bound_checking(point, matrix) and barrier_checking(point, matrix)

def is_target(node, end):
    return node.position == end
    

def get_branches(node, martix):
    branches = []
    history = node.history

    x = node.position[0]
    y = node.position[1]

    position_set = []
    position_set.append((x + 1, y))
    position_set.append((x - 1, y))
    position_set.append((x, y + 1))
    position_set.append((x, y - 1))

    for position in position_set:
        if(checking(position, matrix)):
            new_history = history.copy()
            new_history.append(position)
            branches.append( Node(position, new_history)) 
    
    return branches


def BFS(start, end, matrix):
    queue = [] 
    explored = set() # record all the used position

    if(checking(start, matrix)):
        queue.append(Node(start, [start]))

    explored.add(start)
    
    while(len(queue) != 0):
        node = queue.pop(0)
        if(is_target(node, end)):
            return node
        branches = get_branches(node, matrix)

        for branch in branches:
            position = branch.position
            if not(position in explored):
                queue.append(branch)
                explored.add(position)
    return None # if no answer

# I/O
def matrix_init():
    name = "test4.txt"

    buffer = []
    for line in open(name, "r"):
        buffer.append(line)
    
    n, m = buffer.pop(0).split()
    m = int(m)
    n = int(n)

    matrix = []
    for item in buffer:
        string = item.strip('\n')
        row = []
        for c in string:
            row.append(int(c))
        matrix.append(row)

    # file error checking
    CRED = '\033[91m'
    CEND = '\033[0m'
    if(len(matrix) != m):
        exit(CRED + "data error in source file" + CEND)
    for row in matrix:
        if(len(row) != n):
            exit(CRED + "data error in source file" + CEND)

    return matrix
        

def input_vertex():
    print("Input the info for starting point(x1, y1), and ending point(x2, y2).")
    print("please input as the form: x1 y1 x2 y2 ")

    x1, y1, x2, y2 = input().split()
    start = (int(y1), int(x1))
    end = (int(y2), int(x2))

    return start, end

# display and marked the path
def colored_matrix_display(matrix, answer_node):
    m = len(matrix)
    n = len(matrix[0])

    history = answer_node.history
    trace = [[0 for x in range(n)] for y in range(m)]

    for point in history:
        r = point[0]
        c = point[1]
        trace[r][c] = 1

    CRED = '\033[91m'
    CEND = '\033[0m'
    for r in range(m):
        for c in range(n):
            if(trace[r][c] == 1):
                string = CRED + str(matrix[r][c]) + CEND
            else:
                string = matrix[r][c]
            print(string, end = '')
        print()


def show_path(answer_node):    
    def direction(start, end):
        y = end[0] - start[0]
        x = end[1] - start[1]
        if(x == 1 and y == 0): return "right"
        if(x == -1 and y == 0): return "left"
        if(x == 0 and y == 1): return "down"
        if(x == 0 and y == -1): return "up"
        return ""

    history = answer_node.history
    point_num = len(history)

    print("path: ", end = '')
    for index in range(point_num):
        y = history[index][0]
        x = history[index][1]
        print((x, y), end = ' ')
        if(index < point_num - 1):
            print(direction(history[index], history[index + 1]), end = ' ')
    print()

    print("step: " + str(point_num - 1))

if __name__  == '__main__':
    matrix = matrix_init()
    start, end = input_vertex()

    answer_node = BFS(start, end, matrix)
    print("==========================")
    if(answer_node):
        colored_matrix_display(matrix, answer_node)
        show_path(answer_node)
    else:
        print("No answer")
