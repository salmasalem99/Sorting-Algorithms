'''Merge Sort'''
def merge(array,s,m,e,length):
    temparray =[0]*length
    index1=s
    index2=m+1
    i=s
    z=0
    while i <= e:
        z=i
        if index1==(m+1):
            while z <= e:
                temparray[z]=array[index2]
                index2+=1
                z+=1
        elif index2==(e+1):
            while z<=e:
                temparray[z]=array[index1]
                index1+=1
                z+=1
        if z==(e+1):
            break

        elif array[index1] <= array[index2]:
            temparray[i]=array[index1]
            index1+=1
        elif array[index2] < array[index1]:
            temparray[i]=array[index2]
            index2+=1
        i+=1

    i=s
    while i<=e:
        array[i]=temparray[i]
        i+=1
        
def mergesort(array, start, end,length):
    if start < end:
        middle = int((start+end)/2)
        mergesort(array,start,middle,length)
        mergesort(array,middle+1,end,length)
        merge(array,start,middle,end,length)


'''Selection Sort'''
def selectionsort(array2):
    i=0
    j=0
    flag=0
    index=0
    minimum=0
    while i<len(array2):
        flag=0
        minimum=array2[i]
        j=i+1
        while j<len(array2):
            if array2[j]<=minimum:
                minimum=array2[j]
                index=j
                flag=1
            j+=1
        if flag==1:
            minimum=array2[index]
            array2[index]=array2[i]
            array2[i]=minimum
        i+=1

'''Heap Sort'''
def max_heapify(array,i,n):
    ch1=2*i+1
    ch2=ch1+1
    m=i
    if ch1<=n:
        if array[ch1]>array[m]:
            m=ch1
    if ch2<=n:
        if array[ch2]>array[m]:
            m=ch2
    if m!=i:
        temp=array[m]
        array[m]=array[i]
        array[i]=temp
        max_heapify(array,m,n)

def Build_MH(array,n):
    i=int((n-1)/2)
    while i>=0:
        max_heapify(array,i,n)
        i-=1

def HS(array,n):
    Build_MH(array,n)
    temp=0
    i=n
    while i>0:
        temp=array[i]
        array[i]=array[0]
        array[0]=temp
        max_heapify(array,0,i-1)
        i-=1
        

'''Main Function'''
import time
def read_file(path):
    with open(path ,encoding = 'utf-8') as f2:
        lines = f2.readlines()
        array= [int(line) for line in lines]
    return array

array1 = read_file("file1.txt")
array2 = read_file("file2.txt")


HS1=array1.copy()
HS2=array2.copy()
MS1=array1.copy()
MS2=array2.copy()
SS1=array1.copy()
SS2=array2.copy()

print('Heap sort')
l1=len(array1)-1
l2=len(array2)-1
start = time.time()*1000.0
HS(HS1,l1)
time.sleep(1)
elapsed_time = float(time.time()*1000.0 - start -1000)
print('Time taken by Heap sort algorithm',elapsed_time)
HS(HS2,l2)
print(HS1)
print(HS2)


print('Selection sort')
start = time.time()*1000.0
selectionsort(SS1)
time.sleep(1)
elapsed_time = float(time.time()*1000.0 - start -1000)
print('Time taken by Selection sort algorithm',elapsed_time)
selectionsort(SS2)
print(SS1)
print(SS2)

print('Merge sort')
start = time.time()*1000.0
mergesort(MS1,0,len(MS1)-1,len(MS1))
time.sleep(1)
elapsed_time = float(time.time()*1000.0 - start -1000)
print('Time taken by Merge sort algorithm',elapsed_time)
mergesort(MS2,0,len(MS2)-1,len(MS2))
print(MS1)
print(MS2)
i=0
flag=0
if  len(MS1) != len(MS2) :
    print('Files are not identical')
else:
    while i< len(MS1) :
        if MS1[i] != MS2[i]:
            flag=1
        if(flag):
            print('Files are not identical')
            break
        i+=1

if flag==0:
    print('Files are identical')





'''import matplotlib.pyplot as plt
import numpy as np
n = [1000 , 5000, 10000, 50000, 100000,200000,300000]
heaptime=[]
mergetime=[]
selectiontime=[]
for i in n:
    arr = np.random.randint(1,100000,i)
    ss=arr.copy()
    hs=arr.copy()
    ms=arr.copy()
    
    start = time.time()
    selectionsort(ss)
    elapsed_time = float(time.time()- start)
    selectiontime.append(elapsed_time)
    
    start = time.time()
    HS(hs,len(hs)-1)
    elapsed_time = float(time.time()- start)
    heaptime.append(elapsed_time)

    start = time.time()
    mergesort(ms,0,len(ms)-1,len(ms))
    elapsed_time = float(time.time()- start)
    mergetime.append(elapsed_time)
    print(i, " is done")

plt.figure()
plt.title('Time Performance of Sorting Algorithms')
plt.plot(n, heaptime,label='Heap Sort')
plt.plot(n,mergetime,label='Merge Sort')
plt.plot(n,selectiontime,label='Selection Sort')
plt.legend()
plt.ylabel('Time(s)')
plt.xlabel('n')

plt.show()'''
