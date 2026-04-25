def findSubset(s, current = "", index = 0):
    # base case 

    if(index == len(s)):
        if current == "" :  #skip empty subset if needed
            print("null")
        else:
            print(current)
        return


    # include 
    # ""+s[0] 
    # a 
    findSubset(s, current+s[index], index+1)
    # exclude
    findSubset(s, current, index+1)

s = "abc"
findSubset(s)