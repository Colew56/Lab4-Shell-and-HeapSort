from time import perf_counter

def heap(arr, i, n):
    while True:
        #left child of an element will be 2i + 1
        #right child of an element will be 2i + 2
        largest = i#assumes current node is the largest
        left = 2 * i + 1
        right = 2 * i + 2

        #compare left child to root
        if left < n and arr[left] > arr[largest]:
            largest = left#update largest pointer

        #compare right child to left child
        if right < n and arr[right] > arr[largest]:
            largest = right#update largest pointer 

        #if max-heap conditions are already satisfied, exit the loop
        if largest == i:
            break  

        #swap parent with largest child, 
        arr[i], arr[largest] = arr[largest], arr[i]
        #move down the tree
        i = largest 
        
def heapSort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):#select last nonleaf node, step back by 1
        #build the heap from the last non-leaf node
        heap(arr,i,n)
    
    #initialize i 
    i = n-1
    
    while i >0:
        #begins sorting max heap
        arr[i],arr[0] = arr[0],arr[i]
        #restore heap property to new root
        heap(arr,0,i)
        
        i-=1#i-1, keeps sorting [0:n-1]


def merge_columns_sorted(inputfile1, inputfile2, inputfile3, outputfile):
    
    #function to make sure input is an integer
    def read_file(filename):
        with open(filename, 'r') as f:
            
            #error checking, ensures input is an integer
            return [int(line.strip()) for line in f if line.strip().isdigit()]

    # Read and sort each file separately
    col1 = read_file(inputfile1)
    col2 = read_file(inputfile2)
    col3 = read_file(inputfile3)
    
    #time each function 
    start1 = perf_counter()
    heapSort(col1)
    time1 = (perf_counter() - start1)* 10**3

    start2 = perf_counter()
    heapSort(col2)
    time2 = (perf_counter() - start2) * 10**3

    start3 = perf_counter()
    heapSort(col3)
    time3 = (perf_counter() - start3) * 10**3
    
    #determines number of rows to print
    max_len = max(len(col1), len(col2), len(col3))

    with open(outputfile, 'w') as f:
        
        #writes to output file
        f.write(f"HeapSort Time (Random): {time1} seconds\n")
        f.write(f"HeapSort Time (Ascending): {time2} seconds\n")
        f.write(f"HeapSort Time (Descending): {time3} seconds\n\n")

        
        #header 
        f.write("Ran\tAsc\tDes\n")
        
        #writes the columns
        for i in range(max_len):
            val1 = str(col1[i]) if i < len(col1) else ''
            val2 = str(col2[i]) if i < len(col2) else ''
            val3 = str(col3[i]) if i < len(col3) else ''
            f.write(f"{val1}\t{val2}\t{val3}\n")
#extract files
merge_columns_sorted("25_ran.txt", "25_asc.txt", "25_rev.txt", "25_outputcolumns.txt")
merge_columns_sorted("50_ran.txt", "50_asc.txt", "50_rev.txt", "50_outputcolumns.txt")
merge_columns_sorted("200_ran.txt", "200_asc.txt", "200_rev.txt", "200_outputcolumns.txt")
merge_columns_sorted("500_ran.txt", "500_asc.txt", "500_rev.txt", "500_outputcolumns.txt")
        