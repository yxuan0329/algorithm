# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:59:18 2020
homework3, algorithm 2020 fall
@author: Yun Xuan, Liang
Student no: S0661124
"""
import sys

inf = float("inf")
f = open("t2_out.txt", "a")

class Node():
    """
        node be used to record:
            distance: the edge distance
            roadwidth: the road width of edge
            accvalue: the accessibility of each transportation
    """
    def __init__(self, distance, roadwidth, accvalue):
        self.distance = distance
        self.roadwidth = roadwidth
        self.accvalue = accvalue
        
        self.parent = None
        
    def show(self):
        print(self.distance)
        
    def __str__(self):
        s = "(" + str(self.distance) +", "+ str(self.roadwidth) +")"
        return s
        
# create array to store nodes info        
def createMap(n): 
    edge = [[None]*n for i in range(n)] # create a matrix(2-D array)
    for i in range(0, n):
        for j in range(0, n):
            edge[i][j] = None
    return edge

def carwidth(transport):
    width = {
        0: 6,
        1: 4,
        2: 2,
        3: 1.5,
        4: 0.5
    }

    return width.get(transport, None)

def errormsg(errorid):
    msg = {
        1: "File error! There should be no self loop.",
        2: "File error! distance and road width should be positive real number.",
        3: "File error! Vertex should be valid number.",
        4: "Input error! Please enter a valid vertex.",
        5: "Input error! Please enter a valid transportation id.",
        6: "Input error! Source and destination should be different."
    }
    
    return msg.get(errorid, None)

# check if the file is valid
def foolproof(src, dest, distance, roadwidth, n):
    if src == dest and distance > 0:
        print(errormsg(1))
        sys.exit()
    elif distance <= 0 or roadwidth <= 0:
        print(errormsg(2))
        sys.exit()
    elif src >= n or dest >= n:
        print(errormsg(3))
        sys.exit()

# read file
def getFile():
    file = open("test3.txt", "r")
    
    while True: 
        n = int(file.readline())
        edge = createMap(n)

        line = file.readlines()
        if not line:
            break
        for i in range(0,len(line)):
            data = list(line[i].split())
            src, dest = int(data[0]), int(data[1])
            distance, roadwidth= float(data[2]), float(data[3])
            if len(data)==5:
                accvalue = data[4]
            else: # no default transportation accessibility
                accvalue = '11111'
            
            foolproof(src, dest, distance, roadwidth, n)

            newNode = Node(distance, roadwidth, accvalue)
            edge[src][dest] =  newNode
            
        # print(edge)
        return n, edge

# set each accessibility of transportation, i=input transportation
def accessibility(n, edge, i, carwidth):
    for src in range(0, n):
        for dest in range(0, n):
            if (edge[src][dest]!= None):
                a = edge[src][dest].accvalue
                if a[i] == '0' or edge[src][dest].roadwidth < carwidth :
                    # print(a[i])    
                    edge[src][dest].distance = inf # disable passing

"""                    
    for src in range(0, n):
        for dest in range(0, n):
            if (edge[src][dest]!= None):
                print(edge[src][dest].distance)

"""
        
def dijkstra(n, edge, start, end):
    parent = []
    for i in range(0, n):
        parent.append(-1)
    visited = [] # check if the vertex has visited
    for i in range(0, n):
        visited.append(False)
    
    dist = [inf]*n # distance to each node
    for i in range(0, n):
        # print(edge[start][i])
        if (edge[start][i]!= None and edge[start][i].distance < inf):
                dist[i] = edge[start][i].distance
                parent[i] = start
    dist[start] = 0 # itself
    visited[start] = True
    
        
    for i in range(0,n):
        min = inf
        u = -1
        for j in range(0, n): # nearest vertex
            if dist[j] < min and visited[j]==False:
                min = dist[j]
                u = j
        visited[u] = True

        for v in range(0,n):
            if (edge[u][v]!= None):
                if edge[u][v].distance < inf:
                    if dist[v] > dist[u] + edge[u][v].distance:
                        dist[v] = dist[u] + edge[u][v].distance
                        parent[v] = u
                        # print(dist) # every iterate of finding shortest path
                        # print(u,v, dist[v], edge[u][v].roadwidth, edge[u][v].accvalue)
    return dist, parent

def findlength(start, end, dist):
    return dist[end]

def findpath(end, parent, edge):
    p = parent[end]
    if p == -1:
        return
    else:
        findpath(p, parent, edge)
    print(p,'->', end, '[ distance=',edge[p][end].distance, ', roadwidth=',edge[p][end].roadwidth, ', accessibility=',edge[p][end].accvalue,']')
    f.write(str(p)+'->'+str(end)+'  [ distance='+str(edge[p][end].distance)+', roadwidth='+str(edge[p][end].roadwidth)+', accessibility='+str(edge[p][end].accvalue)+']\n' )

def getInput(n):
    start = int(input("Please enter source vertex:"))
    while start >= n or start < 0:
        print(errormsg(4))
        start = int(input("Please enter source vertex:"))
    end = int(input("Please enter destination vertex:"))
    while end >= n or end < 0:
        print(errormsg(4))
        end = int(input("Please enter destination vertex:"))
    while end ==start:
        print(errormsg(6))
        end = int(input("Please enter destination vertex:"))
        
    print("======================\nHere's the car width of each transportation:")
    print("5. Bus: 6m")
    print("4. Car: 4m")
    print("3. Motor: 2m")
    print("2. Bike: 1.5m")
    print("1. Walk: 0.5m\n======================")
    transport= 5 - int(input("Please enter the transportation (1-5):"))
    while transport > 4 or transport < 0:
        print(errormsg(5))
        transport= int(input("Please enter the transportation (1-5):"))
    return start, end, transport

# main function
if __name__ == '__main__':
    n, edge = getFile()
    print("There are", n, "vertex in the graph.")
    start, end, transport = getInput(n)

    carwidth = carwidth(transport)
    accessibility(n, edge, transport, carwidth)

    dist, parent = dijkstra(n, edge, start, end) # start node's path to each node

    length = findlength(start, end, dist) # path length
    print("======================")
    print('the shortest path from', start, 'to', end, 'is', length)
    f.write('the shortest path from ' + str(start) + ' to ' + str(end)+' is ' + str(length) + '\n')
    findpath(end, parent, edge)
    f.close()
      
        
        