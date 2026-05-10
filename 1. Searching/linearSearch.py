a = [2,4,3,5,7,6,8,9,10]



def linearSearch(a,key):
    for i in range(len(a)):
        if(a[i] == key):
            return i
    return -1


print(linearSearch(a,60))