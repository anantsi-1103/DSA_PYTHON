def twoSumPointer(num, target):

    lp = 0
    rp = len(num) -1

    while(lp < rp):

        cs = num[lp] + num[rp]
        if cs == target:
            return [lp , rp]
        
        elif cs < target:
            lp += 1

        else:
            rp -= 1

    return [-1,-1]


num = [1,2,3,4,5,6]

target = 8

print(twoSumPointer(num , target))