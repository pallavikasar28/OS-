# Python3 implementation of Least Recently Used (LRU) page replacement Algorithm in Operating Systems. 
from collections import deque
from operator import itemgetter
import pandas as pd

def LRU(pages, n, capacity):
    #To store the current frame
    #"N/A" represent empty frame
    frame = ["N/A"]*capacity 
    time_used = [0]*capacity

    #To store the time
    time = 0

    #To store the output
    output = pd.DataFrame(index=range(0,capacity))

    # Start from initial page  
    page_faults = 0
    
    for i in range(n):
        # Check if the set can hold more pages  
        if (frame.count("N/A") > 0):
            # Insert it into set if not present  
            # already which represents page fault  
            if (pages[i] not in frame): 
                frame[frame.index("N/A")] = pages[i]
                # increment page fault  
                page_faults += 1

                #Put in the dataframe
                output[time] = frame

        # If the set is full then need to perform LRU Algorithm  
        # i.e. replace page that has not been used in the most amount of time 
        else: 
              
            # Check if current page is not  
            # already present in the set  
            if (pages[i] not in frame): 
                
                index = max(enumerate(time_used), key=itemgetter(1))[0]
                
                # Replace the indexes page
                frame[index] = pages[i]
                time_used[index] = 0
                # Increment page faults  
                page_faults += 1

                #Put in the dataframe
                output[time] = frame
            else:
                time_used[frame.index(pages[i])] = 0
                temp = ["N/A"]*capacity
                temp[frame.index(pages[i])] = "hit"
                output[time] = temp
        time_used = [t+170 for t in time_used]
        time += 1

    print_graph(output, pages,capacity, page_faults)
    
# This is the function used to print out the simulated graph in a nice way
def print_graph(output, pages,capacity, page_faults):
    print("This is the simulated graph using Optimal page replacement algorithm:")
    
    for page in pages:
        print(str(page), end = '\t')
    print('\n')
    for c in range(0,capacity):
        for col in output:
            if(output[col][c] != "N/A"):
                print(output[col][c], end='\t')
            else:
                print(" ", end='\t')
        print('\n')

    print("\nNumber of page fault: " + str(page_faults))

# Driver code  
if __name__ == '__main__':
    
    print('\n')
    print("Input the reference string reference string.\n")
    print("Please input the reference string separated by comma: (e.g. 7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1)")

    pages_input = input()
    pages = pages_input.split(',')
    pages = [int(i) for i in pages] 

    capacity = int(input("Please input the number of frame:\n"))
    
    n = len(pages)

    LRU(pages, n, capacity)
