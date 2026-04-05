"""
MEDIUM PROBLEM NO 4
We basically have to do a little bit of signal processing here.
we have given two different filters up in the question we implement and display the output.
we have been allowed to experiment with a hybrid filter.
"""
#open a file named log.txt to obtain the list
with open('log.txt', 'r') as f:
    arr_test = f.readline().strip().split()
k = int(input("Enter the value of window sizes: "))  #recieve list and rolling window size

def muchiko_filter(arr, k): #implementation of munchikp filter
    n = len(arr)
    if n<=k:
        return arr
    filtered = []
    for i in range(n-k+1):
        window = arr[i:i+k]
        filtered.append(sum(window)/k)  #appends the average to the list
    return filtered

print("Muchiko filter output:", muchiko_filter(arr_test, k))

def suchiko_filter(arr, k):
    n = len(arr)
    if n<=k:
        return arr 
    filtered = []
    for i in range(n-k+1):
        window = arr[i:i+k]
        filtered.append(sorted(window)[k//2])  #appends the sorted median to the lists
    return filtered

print("Suchiko filter output:", suchiko_filter(arr_test, k))

def hybrid_muchiko_suchiko_filter(arr, k):
    n = len(arr)
    if n<=k:
        return arr 
    filtered = []
    for i in range(n-k+1):
        window = arr[i:i+k]
        avg = sum(window)/k
        median = sorted(window)[k//2]
        filtered.append((avg + median) / 2)    #obtains average(munchiko) sorted median(suchiko) and combined average
    return filtered

print("Hybrid filter output:", hybrid_muchiko_suchiko_filter(arr_test, k))