a = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3] 
# a = [6, 1, 1, 2, 0, 3, 4, 6, 0, 2, 1, 2, 1, 2, 0, 3, 2, 1, 2, 0] 
stack = []

# n = int(input("No of page reference string= "))

no_of_frames = int(input("No of frames = "))

hit = 0 
miss = 0 

# USING  FIFO FOR PAGE REPLACEMENT 

def is_full(stack):
    if len(stack) == no_of_frames:
        return True
    else:
        return False 
    
count = 0 
for item in a:
    if(item not in stack):
        # case of miss
        miss = miss + 1
        if (is_full(stack)):
            # stack.pop(count)
            stack[count] = item 
            count = count + 1 
            continue
        # stack = stack[:-1]
        stack.append(item)
    else:
        # case of hit
        hit = hit + 1 
        continue

for item in stack:
    print(item)

print("Hit Ratio = ",hit/len(a), ", No of page faults(Miss) = ", miss)


    
        
        


