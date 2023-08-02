import numpy as np
import matplotlib.pyplot as plt
import timeit
import random
from matplotlib.legend_handler import HandlerLine2D
#//////////////////////////////////////////////////////////////////////////////
#Insertionsort

def insertionsort(a):
   if (len(a) == 1) or (len(a)== 0):
       return a
   for i in range(1,len(a),1): # i is the dividing line
     temp = a[i]               # remove marked item
     inner = i                 # starts shifts at i
     while inner>0 and a[inner-1] >= temp: # loop untill one is smaller
                a[inner] = a[inner-1]   #shift item to right
                inner -= 1              #go left one index
                a[inner] = temp         #insert marked item
   return a

def insertionsort2(a, half):
   if (len(a) == 1) or (len(a)== 0):
       return a

   for i in range(1,len(a),1): # i is the dividing line

     while i < half:

        temp = a[i]               # remove marked item
        inner = i                 # starts shifts at i
        while inner>0 and a[inner-1] >= temp: # loop untill one is smaller
                    a[inner] = a[inner-1]   #shift item to right
                    inner -= 1              #go left one index
                    a[inner] = temp         #insert marked item
     return a

#//////////////////////////////////////////////////////////////////////////////
#MergeSort
def mergesort(a): # A = Array to be sorted /p = 0 / l = length of A
    p = 0
    l = len(a)
    if (len(a) == 1) or (len(a)== 0):
        return a

    mid = int((p + l) / 2)      #mid
    L = mergesort(a[0:mid])     #mergeSort the left
    R = mergesort(a[mid:l])     #mergeSort the right
    M = merge(L,R)              #MERGE

    return M

def merge(B,C):
    D = np.empty(len(B) + len(C))
    i = j = k = 0
    while k < (len(B) + len(C)):
        # check left Array is out of bounds
        if (i == len(B)):
             D[k] = C[j]
             j = j + 1
        # check right Array is out of bounds
        elif(j == len(C)):
            D[k] = B[i]
            i = i + 1

        elif B[i] < C[j]:
            D[k] = B[i]
            i = i + 1
        else:
            D[k] = C[j]
            j = j + 1

        k = k + 1
    return D
#//////////////////////////////////////////////////////////////////////////////
# input size array
A = np.arange(101)*100
inputSize = np.delete(A, 0)
# magic number for now
# /////////
n = 20  # 100 = 10,000 array elements
# ////////
# //////////////////////////////////////////////////////////////////////////////
# ////////////////////////Simple Sorting analysis///////////////////////////////
# arrays for storing times and number of array elements
A_t_mergesort = np.empty(n)
A_t_insertionSort = np.empty(n)
A_n = np.empty(n)
# main iteration loop
for i in range(n):

    #A_ran = np.arange(inputSize[i])
    #random.shuffle(A_ran)  # randomize the array
    #A_ran2 = np.copy(A_ran)

    A_ran = np.arange(inputSize[i])
    random.shuffle(A_ran)  # randomize the array

    A_ran2 = np.arange(inputSize[i])
    random.shuffle(A_ran2)  # randomize the array
    sortHalf = (A_ran.size/2)

    A_ran3 = insertionsort2(A_ran2, sortHalf)

    print(A_ran3)


    # A_ran1 = np.copy(A_ran)
    #random.shuffle(A_ran)  # randomize the array
    #A_ran2 = np.copy(A_ran)
    #A_sorted = np.arange(inputSize[i])

    print("_____Simple Sorting analysis____________________________")

    print(A_ran)


    # NOTE: it is important that the data is consistent meaning that (A_ran, A_ran2, A_ran3) are identical
    t_mergesort = timeit.Timer(lambda: mergesort(A_ran))

    print(A_ran2)
    t_insertion = timeit.Timer(lambda: insertionsort(A_ran2))


    # store the times and array size
    A_t_mergesort[i] = t_mergesort.timeit(number=1)
    A_t_insertionSort[i] = t_insertion.timeit(number=1)
    A_n[i] = inputSize[i]

    print("iteration: ", i)
    print("number of elements: ", A_ran.size)
    print("t_mergesort: ", t_mergesort.timeit(number=1))
    print("insertion Sort time: ", t_insertion.timeit(number=1))
    print("___________________________________________")

# plot
plt.figure(1)
plt.title("(mergesort - randomize array, insertion Sort - sorted array)")
plt.ylabel("execution time")
plt.xlabel("size of array (n)")
# x-axis of plots is n, the input size
# y-axis execution time
line1, = plt.plot(A_n, A_t_mergesort, 'r--', label="mergesort")
line2, = plt.plot(A_n , A_t_insertionSort, 'bs', label="insertionSort")
#line3, = plt.plot(A_n, A_t_insertionSort, 'g^', label="Insertion Sort")
# legend
plt.legend(handler_map={line1: HandlerLine2D(numpoints=1)}, loc=2)
plt.show(1)
