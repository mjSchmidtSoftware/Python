"""
@author: Michael James Schmidt

this program is used to compare Simple Sorting algorithms
Bubble Sort
Selection Sort
Insertion Sort

the program runs each algorithm on array of size n
For n in [100,200,300,...,10000]

each algorithm is given following
- fully sorted array of length n
- reverse sorted array of length n
- and random array of length n
"""
import numpy as np
import matplotlib.pyplot as plt
import timeit
import random
from matplotlib.legend_handler import HandlerLine2D
# implement Sorting algorithms
# //////////////////////////////////////////////////////////////////////////////
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
# //////////////////////////////////////////////////////////////////////////////
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

# //////////////////////////////////////////////////////////////////////////////
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
# /////////////////////////////////////////////////////////////////////////////
# This is the code that sets the testing sorting size 
# input size array
A = np.arange(101)*100
inputSize = np.delete(A, 0)
# magic number for now
# /////////
n = 15  # 100 = 10,000 array elements
# //////////////////////////////////////////////////////////////////////////////

# This is the code that runs and does the test for each of the types of sorting algorithm. 

# /////////////////////sorting analysis on BUBBLE_SORT//////////////////////////
# arrays to store plotting coordinate info
# bubbleSort coordinate info
A_t_sort_bubbleSort = np.empty(n) # array to store sorted times (y coordinates)    
A_t_rev_bubbleSort = np.empty(n)  # array to store reversed times (y coordinates)
A_t_ran_bubbleSort = np.empty(n)  # array to store random times (y coordinates)
A_n_bubbleSort = np.empty(n)      # number of elements same for all 
# Plot1
# on each iteration create an array where (100 * i) = size of array
# when n = 1 - 100 numbers when n = 2  - 200 numbers.....when n = 100 - 10,000
for i in range(n): 
    print("_____BubbleSort____________________________")
    print("iteration: ", i)
    # create arrays for sorting 
    A_sorted = np.arange(inputSize[i]) # create sorted array
    A_reverse = A_sorted[::-1]         # create reverse sorted array 
    A_ran = np.arange(inputSize[i])    # create a array for random array
    random.shuffle(A_ran)              # shuffle the array into random array 
    print("number of elements: ", A_sorted.size)
    # timeit and calls 
    t_sort = timeit.Timer(lambda: bubbleSort(A_sorted))  
    t_rev = timeit.Timer(lambda: bubbleSort(A_reverse))
    t_ren = timeit.Timer(lambda: bubbleSort(A_ran))
    # store time info 
    A_t_sort_bubbleSort[i] = t_sort.timeit(number=1) # y_coordinate for sorted 
    A_t_rev_bubbleSort[i] = t_rev.timeit(number=1) # y_coordinate for reversed   
    A_t_ran_bubbleSort[i] = t_ren.timeit(number=1) # y_coordinate for random
    A_n_bubbleSort[i] = inputSize[i] # n is the x coordinate 
    # print times     
    print("Sorted Time: ", t_sort.timeit(number =1))
    print("reversed Time: ", t_rev.timeit(number = 1))
    print("random time: ", t_ren.timeit(number = 1))
    print("___________________________________________")   
# draw plot 1
plt.figure(1) # figure one is selectionSort Graph
plt.title("bubble sort analysis")
plt.ylabel("execution time in sec")
plt.xlabel("size of array (n)")
# x-axis of plots is n, the input size
# y-axis execution time
line1, = plt.plot(A_n_bubbleSort, A_t_sort_bubbleSort,'r--', label="sorted array")
line2, = plt.plot(A_n_bubbleSort , A_t_rev_bubbleSort, 'bs', label="reversed array") 
line3, = plt.plot(A_n_bubbleSort, A_t_ran_bubbleSort, 'g^',label="random array")
# legend
plt.legend(handler_map={line1: HandlerLine2D(numpoints=1)}, loc=2)
print("Display Graph")
plt.show()
# //END_bubbleSort/////////////////////////////////////////////////////////////
"""
# /////////////////////sorting analysis on SELECTION_SORT///////////////////////
# arrays to store plotting coordinate info
# bubbleSort coordinate info
A_t_sort_select = np.empty(n) 
A_t_rev_select = np.empty(n)
A_t_ran_select = np.empty(n)
A_n_select = np.empty(n)
for i in range(n):
    print("_____SELECTION_SORT____________________________")
    print(i)
    A_sorted = np.arange(inputSize[i])
    A_reverse = A_sorted[::-1]
    A_ran = np.arange(inputSize[i])    # create a array for random
    random.shuffle(A_ran)               # shuffle the array
    # RUN selectionsort
    t_sort = timeit.Timer(lambda: selectionSort(A_sorted))
    t_rev = timeit.Timer(lambda: selectionSort(A_reverse))
    t_ren = timeit.Timer(lambda: selectionSort(A_ran))
    # storing time and size variables in arrays
    A_t_sort_select[i] = t_sort.timeit(number=1)
    A_t_rev_select[i] = t_rev.timeit(number=1)
    A_t_ran_select[i] = t_ren.timeit(number=1) # y_coordinate for random
    A_n_select[i] = inputSize[i] # n is the x coordinate 
    print("Sorted Time: ", t_sort.timeit(number =1))
    print("reversed Time: ", t_rev.timeit(number = 1))
    print("random time: ", t_ren.timeit(number = 1))      
    # plot points
    # plt.plot(i,t_sort.timeit(number=1), 'bs', i, t_rev.timeit(number=1), 'g^')
    print("_________________________________")
# draw Plot 1
plt.figure(1) # figure one is selectionSort Graph
plt.title("selection Sort analysis")
plt.ylabel("execution Time")
plt.xlabel("size of array (n)")
line1, = plt.plot(A_n_select, A_t_sort_select,'r--', label="sorted array")
line2 = plt.plot(A_n_select , A_t_rev_select, 'bs', label="reversed array")
line3 = plt.plot(A_n_select, A_t_ran_select, 'g^', label="random array")
#legend
plt.legend(handler_map={line1: HandlerLine2D(numpoints=1)}, loc=2)
plt.show()
# //END_SELECTION_SORT//////////////////////////////////////////////////////////

# ////////////////////////sorting analysis on INSERTIONSORT/////////////////////
# insertion sort
# create empty array to store time data 
A_t_sort_insert = np.empty(n) 
A_t_rev_insert = np.empty(n)
A_t_ran_insert = np.empty(n)
A_n_insert = np.empty(n)
# Run It
for i in range (n):
    print("_____INSERTION_SORT______________")
    print(i)  
    A_sorted = np.arange(inputSize[i])
    A_reverse = A_sorted[::-1]
    ran = np.arange(inputSize[i])
    random.shuffle(ran)  
    # RUN Insertion Sort
    t_sort = timeit.Timer(lambda: insertionSort(A_sorted))
    t_rev = timeit.Timer(lambda: insertionSort(A_reverse))
    r_ran = timeit.Timer(lambda: insertionSort(ran))
    # storing time and size variables in arrays
    A_t_sort_insert[i] = t_sort.timeit(number = 1)
    A_t_rev_insert[i] = t_rev.timeit(number = 1)
    A_t_ran_insert[i] = r_ran.timeit(number = 1 )
    A_n_insert[i] = inputSize[i]  
    print(t_sort.timeit(number = 1))
    print(t_rev.timeit(number = 1)) 
    print(r_ran.timeit(number = 1))
    print("_________________________________")   
# draw Plot
plt.figure(1) # figure one is selectionSort Graph
plt.title("insertion sort analysis")
plt.ylabel("execution time")
plt.xlabel("size of array (n)")
line1, = plt.plot(A_n_insert, A_t_sort_insert, 'bs', label = "sorted array")
line2, = plt.plot(A_n_insert, A_t_rev_insert, 'g^' , label = "reversed array")
line3, = plt.plot(A_n_insert, A_t_ran_insert, 'r--' , label = "random array")
# legend
plt.legend(handler_map={line2: HandlerLine2D(numpoints=1)}, loc=2)
plt.show()
# //END_INSERTION_SORT//////////////////////////////////////////////////////////

# If you where to run all Three use this code to output the results of all three
# ////////////////////////Simple Sorting analysis///////////////////////////////
# arrays for storing times and number of array elements
A_t_bubbleSort = np.empty(n)    
A_t_selectionSort = np.empty(n)  
A_t_insertionSort = np.empty(n)  
A_n = np.empty(n)
# main iteration loop
for i in range(n):
    A_ran = np.arange(inputSize[i])
    random.shuffle(A_ran)  # randomize the array
    A_ran2 = np.copy(A_ran)
    A_ran3 = np.copy(A_ran2)
    # NOTE: it is important that the data is consistent meaning that (A_ran, A_ran2, A_ran3) are identical
    t_bubble = timeit.Timer(lambda: bubbleSort(A_ran))
    t_select = timeit.Timer(lambda: selectionSort(A_ran2))
    t_insertion = timeit.Timer(lambda: insertionSort(A_ran3))
    # store the times and array size
    A_t_bubbleSort[i] = t_bubble.timeit(number=1) 
    A_t_selectionSort[i] = t_select.timeit(number=1)   
    A_t_insertionSort[i] = t_insertion.timeit(number=1) 
    A_n[i] = inputSize[i]
    print("_____Simple Sorting analysis____________________________")
    print("iteration: ", i)
    print("number of elements: ", A_ran.size)
    print("bubble Sort time: ", t_bubble.timeit(number=1))
    print("selection Sort time: ", t_select.timeit(number=1))
    print("insertion Sort time: ", t_insertion.timeit(number=1))
    print("___________________________________________")
# plot
plt.figure(1)
plt.title("Simple Sorting Analysis (sorting of randomize array)")
plt.ylabel("execution time")
plt.xlabel("size of array (n)")
# x-axis of plots is n, the input size
# y-axis execution time
line1, = plt.plot(A_n, A_t_bubbleSort, 'r--', label="Bubble Sort")
line2, = plt.plot(A_n , A_t_selectionSort, 'bs', label="Selection Sort")
line3, = plt.plot(A_n, A_t_insertionSort, 'g^', label="Insertion Sort")
# legend
plt.legend(handler_map={line1: HandlerLine2D(numpoints=1)}, loc=2)
plt.show()

"""
print("Program Complete")