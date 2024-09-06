'''
2 strings
    string length is longer than 1, shorter than 15
common characters
characters are in lowercase

max value is the length of the shorter string

unpack both strings
sort both strings
start from the shorter string

'''
def unpackString (s):
    a = []
    for i in s:
        a.append(i)
    return a

def solution(s1,s2):
    a1 = unpackString(s1)
    a2 = unpackString(s2)
    
    shorter = a1
    longer = a2
    if len(a2)<len(a1):
        shorter = a2
        longer = a1
    returnArray = []
    for i in shorter:
        if i in longer:
            returnArray.append(i)   
            longer.remove(i)
    return (len(returnArray))
print (solution("sfs","qwesffs"))
        
