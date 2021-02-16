# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:18:58 2020
homework1, Algorithm 2020 fall
"""
class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rank = 0
        
        self.left = False
        self.order = 0
    
    def show(self):
        print(self.x, self.y, self.rank)
        
# read file and split type to float
def getInput():
    inputList = []
    file = open("test2.txt", "r")
    while True:
        line = file.readlines()
        if not line:
            break
        for i in range(0, len(line)):
            data = list(line[i].split())
            #print(data[0], data[1])
            x = float(data[0])
            y = float(data[1])
            newNode = Node(x,y)
            inputList.append(newNode)
    return inputList

# build heap
def construct(data, op): 
    n = len(data)
    for i in range(n//2 -1, -1, -1):
        heapify(data, n, i, op)
            
def heapify(data, n, root, op): 
    largest = root
    l = 2*root + 1 
    r = 2*root + 2    

    def x_smaller_than(a ,b): # if a<b return true
        if a.x < b.x:
            return True
        if a.x == b.x and a.y > b.y:
                return True
        return False

    def get_compare_func(op):
        if op == 1: return x_smaller_than
        elif op == 2: return (lambda a, b: a.y < b.y) # smaller_than of y
        elif op == 3: return (lambda a, b: a.rank < b.rank) # smaller_than of rank 

    smaller_than = get_compare_func(op)

    if l < n and smaller_than(data[root], data[l]):
        largest = l 
    if r < n and smaller_than(data[largest], data[r]): 
        largest = r
                
    if largest != root: 
        data[root], data[largest] = data[largest], data[root]  # swap 
        heapify(data, n, largest, op)
        
def heapSort(data, op):
    n = len(data)
    construct(data, op)
  
    for i in range(n-1, 0, -1): 
        data[i], data[0] = data[0], data[i]   # swap 
        heapify(data, i, 0, op)
        
# split the input data  
def split_list(data):
    half_size = len(data)//2
    return data[:half_size], data[half_size:]

# count the amount of rank
def count_rank(data):
    count = 0
    same_y_count = 0  # the numbers that have same y-coor
    if(data[0].left == True): same_y_count = 1

    # print("some itr")
    for i in range (1, len(data)):
        if(data[i].y != data[i-1].y):
            count += same_y_count
            same_y_count = 0
        if(data[i].left == True):
            same_y_count += 1
        else:
            data[i].rank += count
        # print("idx:", i, "point:", data[i].x, data[i].y, "rank:", data[i].rank, "count:", count)
    return data
     
def ranking(data):
    if len(data) == 1:
        data[0].rank = 0
        return data
    
    heapSort(data, 1)
    
    left_data, right_data = split_list(data) # divide + recursive
    left_data = ranking(left_data)
    right_data = ranking(right_data)
    
    data = []
    # data = left_data + right_data
    for i in range(0, len(left_data)):
        left_data[i].left = True
        data.append(left_data[i])
    
    for i in range(0, len(right_data)):
        right_data[i].left = False
        data.append(right_data[i])
    
    heapSort(data, 2)
    
    data = count_rank(data) # merge part
    return data

def avgRank(data):
    sum = 0
    for i in range(0,len(data)):
        sum += data[i].rank
    avg = sum / len(data)
    return avg

# main function, output data
inputList = getInput()
inputList = ranking(inputList)
heapSort(inputList, 3)
print("Vertex coordinate sort by rank: \n(x, y, rank)")
for element in inputList:
    element.show()
print("1. vertex numbers:" ,len(inputList))
print("2. max rank:" ,inputList[len(inputList)-1].rank)
print("3. min rank:" , inputList[0].rank)
print("4. average rank:" ,round(avgRank(inputList), 2))
    