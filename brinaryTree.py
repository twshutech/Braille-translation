def findingMarlin(h, nemo, end, start):
    marlin = None
    divide = lambda s,e : (e - s)//2 
    if (end == nemo): 
        return -1
    
    while(nemo >= 1):
        end -= 1
        mid = start + divide(start, end)

        if(mid == nemo or end == nemo): 
            marlin= end+1
            return marlin
        elif (nemo < mid):
            end = mid
            findingMarlin(h, nemo, end, start)
        else: 
            start = mid
            findingMarlin(h, nemo, end, start)

def findingMarlinViaNemo(h, q):
    length = lambda x : (2 ** x ) -1

    maxValue = length(h)
    marlinArr = []
    for node in q:
        marlinArr.append(findingMarlin(h,node,maxValue,1))
    return marlinArr

def solution(h, q):
    return findingMarlinViaNemo(h, q)

solution(3, [7,3,5,1])