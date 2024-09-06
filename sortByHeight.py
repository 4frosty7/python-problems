'''
trees are in a fixed index

rearrange people by height
non-descending order

pick out the heights of the people
sort the heights
append the 
make new array and copy values in the order of the reordered indices
'''

def solution(a):
    peopleHeight = []
    result = []
    for i in a:
        if i>-1:
            peopleHeight.append(i)
    peopleHeight.sort()
    
    for i in a:
        if i==-1:
            result.append(i)
            continue
        result.append(peopleHeight.pop(0))
    return result

a = [-1, 150, 190, 170, -1, -1, 160, 180]
print (solution (a))
