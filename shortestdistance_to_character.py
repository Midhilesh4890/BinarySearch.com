def shortestToChar(s,c):
    N = len(s)
    left,right,output =  [0]*N,[0]*N,[0]*N
    tmp = 10**4 + 1
    for i in range(N):
        if s[i]==c:
            tmp = 0
        left[i] = tmp
        tmp+=1
    
    for i in range(N-1,-1,-1):
        if s[i]==c:
            tmp = 0
        right[i] = tmp
        tmp+=1
        
    for i in range(N):
        output[i] = min(right[i],left[i])
    return output

s = 'loveleetcode'
c = 'e'

print(shortestToChar(s,c))