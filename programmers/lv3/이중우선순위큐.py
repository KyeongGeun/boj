from heapq import heappush, heappop

def solution(operations):
    
    mmax = []
    mmin = []
    
    maxDict = dict()
    minDict = dict()
    
    for s in operations:
        a, b = s.split()
        b = int(b)
        
        if a == 'I':
            heappush(mmax, -b)
            heappush(mmin, b)
        
        elif b == -1:
            while mmin and mmin[0] in minDict:
                minDict[mmin[0]] -= 1
                if minDict[mmin[0]] == 0:
                    minDict.pop(mmin[0])
                heappop(mmin)
            if mmin:
                maxDict.setdefault(-mmin[0], 0)
                maxDict[-heappop(mmin)] += 1
                
        elif b == 1:
            while mmax and mmax[0] in maxDict:
                maxDict[mmax[0]] -= 1
                if maxDict[mmax[0]] == 0:
                    maxDict.pop(mmax[0])
                heappop(mmax)
            if mmax:
                minDict.setdefault(-mmax[0], 0)
                minDict[-heappop(mmax)] += 1

                
    while mmin and mmin[0] in minDict:
        minDict[mmin[0]] -= 1
        if minDict[mmin[0]] == 0:
            minDict.pop(mmin[0])
        heappop(mmin)
    
    while mmax and mmax[0] in maxDict:
        maxDict[mmax[0]] -= 1
        if maxDict[mmax[0]] == 0:
            maxDict.pop(mmax[0])
        heappop(mmax)
    
    answer = [0, 0]
    
    if mmax:
        answer[0] = -mmax[0]
    if mmin:
        answer[1] = mmin[0]

    return answer