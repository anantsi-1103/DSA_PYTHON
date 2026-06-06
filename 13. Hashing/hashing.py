# student = {
#     "Ajay" : 90,
#     "Aman" : 78,
#     "Rohan" : 56
# }

# print(student["Aman"])


# n = {20,30,40,50}

# print(20 in n)

# count characters

# s = "naman"

# freq = {}
# # n = 2, a = 2,  m = 1,

# for ch in s:

#     freq[ch] = freq.get(ch,0) + 1

# print(freq)


# first non repeating character

# s = "aabbcde"

# freq = {}

# for ch in s:
#     freq[ch] = freq.get(ch,0) + 1

# for ch in s:
#     if freq[ch] == 1:
#         print(ch, end=" ")
        

# 
# s = "aabbcde"


# s = "swiss"

# Two Sum

num = [2,7,11,15]
target = 18


def two_sum(num, target):

    hashmap = {}


    for i , n in enumerate(num):

        diff = target - n

        if diff in hashmap:
            return [hashmap[diff], i]
        

        hashmap[n] = i

print(two_sum(num,target))


