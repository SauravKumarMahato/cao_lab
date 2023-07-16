a = [6, 1, 1, 2, 0, 3, 4, 6, 0, 2, 1, 2, 1, 2, 0, 3, 2, 1, 4, 0] 
# a = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
stack = []
# n = int(input("No of page reference string= "))

no_of_frames = int(input("No of frames = "))
optimal_index = []
hit = 0 
miss = 0 
index = 0 

# USING  FIFO FOR PAGE REPLACEMENT 

def is_full(stack):
    if len(stack) == no_of_frames:
        return True
    else:
        return False 

def find_index_to_replace(item, stack, a):
    temp_index = a.index(item)
    b = a[temp_index:]

    for i in range(len(optimal_index)):
        optimal_index.pop()

    for data in stack:
        no = b.count(data)
        optimal_index.append(no)
    
    return optimal_index.index(min(optimal_index))


    
for item in a:
    if(item not in stack):
        # case of miss
        miss = miss + 1
        if (is_full(stack)):
            # stack.pop(index)
            index = find_index_to_replace(item, stack, a)
            stack[index] = item
            continue
        # stack = stack[:-1]
        stack.append(item)
    else:
        # case of hit
        hit = hit + 1 
        continue

for item in stack:
    print(item)

print("Hit Ratio = ",hit/len(a), ", No of page faults(Miss) = ", miss, ", Hits = ", hit)


    
        
        


