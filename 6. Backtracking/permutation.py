def permutation(s, current=" "):

    # base 
    if (len(s)) == 0:
        print(current)
        return 
    

    for i in range(len(s)):
        ch = s[i]
        # b

        remaining = s[:i] + s[i+1:] # skip the already added element

                    # bc , "" + a
                    # c  , "a" + b
                    # "" , "ab" + c

        permutation(remaining, current+ch)









s = "abc"

permutation(s)