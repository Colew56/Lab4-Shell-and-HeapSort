import time
def shell_sort_algorithm(nums, gaps):
    
    n=len(nums)
    gap_sequence = [gap for gap in gaps if gap <n][::-1]#calculate which gap sequences to use based on array length
                                                        #reverse the order so largest gap is used first
    for gap in gap_sequence:#iterate through gap sequences
        
        for i in range(gap,n):
            
            temp = nums[i]#temp varibale set to element at i
            j=i#initialize j variable to index gap element
            
            while j>= gap and nums[j-gap] > temp:#compare gap elements
                nums[j] = nums[j-gap]#switch larger element with smaller element
                j -= gap#set j to smaller index 
            
            nums[j] = temp#set gap index to smaller temp variable
    
    return nums#return sorted array
        

knuth_sequence = [1, 4, 13, 40, 121, 364, 1093, 3280, 9841, 29524]
other_sequence =[1, 5, 17, 53, 149, 373, 1123, 3371, 10111, 30341]
other_sequence2 = [1, 10, 30, 60, 120, 360, 1080, 3240, 9720, 29160]
other_sequence3 = [1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, 8929]
sequences = [knuth_sequence,other_sequence,other_sequence2,other_sequence3]

#function to perform shell sort on 20000 int file
def extractfiles_20000int(filename, outputfile):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        #error checking, makes sure input is integer
        original_nums = [int(line.strip()) for line in lines if line.strip().isdigit()]

    results = []
    times = []

    #times the shell sort, based on the gap sequence
    for seq in [knuth_sequence, other_sequence, other_sequence2, other_sequence3]:
        nums_copy = original_nums.copy()
        start = time.perf_counter()
        sorted_nums = shell_sort_algorithm(nums_copy, seq)
        elapsed = time.perf_counter() - start
        results.append(sorted_nums)
        times.append(elapsed)

    #calculate number of rows in the output file
    max_len = max(len(col) for col in results)

    #write sorted columns and times to ouput file 
    with open(outputfile, 'w') as out:
        out.write("Shell Sort Comparison (Time in seconds):\n")
        out.write(f"Knuth: {times[0]:.6f}\tSeq2: {times[1]:.6f}\tSeq3: {times[2]:.6f}\tSeq4: {times[3]:.6f}\n\n")
        out.write("Knuth\tSeq2\tSeq3\tSeq4\n")
        for i in range(max_len):
            vals = []
            for col in results:
                val = str(col[i]) if i < len(col) else ''
                vals.append(val)
            out.write('\t'.join(vals) + '\n')

#run shell sort on 20000 integers
extractfiles_20000int('ShellInputs.txt', 'ShellComparisonOutput.txt')

def extractfiles(inputfile1, inputfile2, inputfile3, outputfile):
    
    #function to readlines 
    def read_file(filename):
        with open(filename, 'r') as f:
            
            #error checking, determines if the input is an integer
            return [int(line.strip()) for line in f if line.strip().isdigit()]

    #read lines from input file
    ran = read_file(inputfile1)
    asc = read_file(inputfile2)
    des = read_file(inputfile3)

    #list to store the columns
    sorted_columns = []
    sort_times = []

    #sort data based on order and gap seuqnece
    for data, label in zip([ran, asc, des], ['Ran', 'Asc', 'Des']):
        for seq in sequences:
            data_copy = data.copy()
            
            start = time.perf_counter()
            sorted_data = shell_sort_algorithm(data_copy, seq)
            #calculate time
            elapsed = (time.perf_counter() - start) * 1000
            
            sorted_columns.append((sorted_data, f"{label}"))
            #append time to list
            sort_times.append(elapsed)

    #calculates number of rows
    max_len = max(len(col[0]) for col in sorted_columns)

    with open(outputfile, 'w') as out:
        
        out.write("Shell Sort Times (in milliseconds):\n")
        headers = ['K', 'S2', 'S3', 'S4']
        for i, label in enumerate(['Ran', 'Asc', 'Des']):
            out.write(f"{label}:\t" + '\t'.join(f"{headers[j]}: {sort_times[i * 4 + j]:.3f}" for j in range(4)) + "\n")
        out.write("\n")

        #columns headers
        column_labels = [f"{h}_{l}" for l in ['Ran', 'Asc', 'Des'] for h in headers]
        out.write('\t'.join(column_labels) + "\n")

        #print the sorted values underneith headers
        for i in range(max_len):
            row = []
            for col, _ in sorted_columns:
                val = str(col[i]) if i < len(col) else ''
                row.append(val)
            out.write('\t'.join(row) + "\n")

#function to perform shell sort on asc, rand, dec input files with lenghts 25,50,200,500
extractfiles("25_ran.txt", "25_asc.txt", "25_rev.txt", "25_outputcolumns.txt")
extractfiles("50_ran.txt", "50_asc.txt", "50_rev.txt", "50_outputcolumns.txt")
extractfiles("200_ran.txt", "200_asc.txt", "200_rev.txt", "200_outputcolumns.txt")
extractfiles("500_ran.txt", "500_asc.txt", "500_rev.txt", "500_outputcolumns.txt")

