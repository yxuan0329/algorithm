# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:10:07 2020
homework1, Algorithm 2020 fall
@author: 梁芸瑄
Student no.: S0661124
"""


# read file and split type to double
file = open("test1.txt", "r")
data = file.readlines()
print(data) #['3.23 5.34 3.45 1.1 5.2 9.0 -23 5.8 10 23 4.0 8']

data = list(data[0].split())
print(data) #['3.23', '5.34', '3.45', '1.1', '5.2', '9.0', '-23', '5.8', '10', '23', '4.0', '8']

for i in range(0, len(data)):
    data[i] = float(data[i])
# print(data)

#Quick Sort
def quickSort(data, left, right):
    if left >= right :     
        return

    i = left
    j = right
    key = data[left]  #pivot

    while i != j :      
        while data[i] <= key and i < j :
            i += 1            
        while data[j] > key and i < j :
            j -= 1
        if i < j: 
            data[i], data[j] = data[j], data[i]  #swap

    data[left] = data[i] 
    data[i] = key

    quickSort(data, left, i-1)
    quickSort(data, i+1, right)

#Insertion Sort
def insertionSort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i-1
        while j >=0 and key < data[j] : 
            data[j+1] = data[j] 
            j -= 1
        data[j+1] = key 

# main menu and output for program
select = int(input("Please select the sorting way you want: \n1.QuickSort  \n2.InsertionSort  \n3.Quit\n"))
while select!=1 and select !=2 and select != 3:
    print("Input error.")
    select = int(input("Please select the sorting way you want: \n1.QuickSort  \n2.InsertionSort  \n3.Quit\n"))
print("Before sorting:\n"+ str(data) + "\n" )
if select == 1 :
    quickSort(data, 0, len(data)-1)
    print("Sorting with Quick-Sort:")
    print(data)
elif select == 2 :
    insertionSort(data)
    print("Sorting with Insertion-Sort:\n")
    print(data)
elif select == 3 :
    print("Exit.")

print("\nArray numbers: "+ str(len(data)) )
print("Max number: " + str(max(data)) )
print("Min number: " + str(min(data)) )
