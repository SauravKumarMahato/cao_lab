a = [1,3,0,3,5,6,3] 
stack = []

# n = int(input("No of page reference string= "))

no_of_frames = int(input("No of frames = "))



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
        if (is_full(stack)):
            # stack.pop(count)
            stack[count] = item 
            count = count + 1 
            continue
        # stack = stack[:-1]
        stack.append(item)
    else:
        # case of hit
        continue

for item in stack:
    print(item)

    
        
        


