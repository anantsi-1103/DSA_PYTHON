# Hashmap

# student = {
#     "Ajay" : 90,
#     "Rakesh": 49,
#     "Rohan":95
# }

# print(student)

# print(student.get("Ajay"))

# Hash Set
# num = {10,20,30,40,50}

# num.add(10)

# print(40 in num)

# array -> Frequency count 

# arr = [1,1,1,2,2,2,2,2,3,3,3,3,4,4,4]

# freq = {}

# for n inpp arr:
#     freq[n] = freq.get(n,0) + 1


# print(freq)

# character Frequency

# s = "ale"

# charFreq = {}

# for ch in s:
#     charFreq[ch] = charFreq.get(ch,0) + 1


# print(charFreq)


# first non repeating character

# s = "aabbcde"

# freq = {}

# for ch in s:
#     freq[ch] = freq.get(ch,0) + 1


# for ch in s:
#     if freq[ch] == 1:
#         print(ch)
#         break


# Duplicate detection

# arr = [1,2,3,4,5,2]

# seen = set() #1,2,3,4,5,2

# duplicate = False

# for num in arr:
#     if num in seen:
#         duplicate = True
#         print(num)
#         break

#     seen.add(num)


# count distinct elements

# arr = [1,2,2,3,3,4,5,5,4]

# distinct = len(set(arr))

# print("Distinct Element : ", distinct)


# Two Sum 

# def twoSum(num, target):
#     hashmap = {}

#     for i,n in enumerate(num):
#         diff = target - n

#         if diff in hashmap:
#             return [hashmap[diff],i]

#         hashmap[n] = i

#     return []

# num = [2,11,7,15]
# target = 90

# print(twoSum(num,target))

# Longest Consecutive Number


# arr = [100,4,200,1,3,2]
# 1,2,3,4

# s = set(arr)
# print(s)
# longest = 0

# for n in s:
#     if n-1 not in s:
#         curr = n
#         length = 1

#         while curr+1 in s:
#             curr+= 1
#             length +=1

#         longest = max(longest,length)

# print(longest)


# Anagram

# def isAnagram(s1,s2):

#     if len(s1) != len(s2):
#         return False

#     freq = {}

    # count characters in s1
    # for ch in s1:

    #     if ch in freq:
    #         freq[ch] +=1
    #     else:
    #         freq[ch] =1


    # Decrease count using s2
#     for ch in s2:

#         if ch not in freq:
#             return False

#         freq[ch] -= 1

#         if freq[ch] < 0:
#             return False

#     return True


# print(isAnagram('silent','listen'))
# print(isAnagram('naman','listen'))


# from collections import Counter

# def isAnagram(s1, s2):

#     return Counter(s1) == Counter(s2)


# print(isAnagram("listen", "silent"))


# def isAnagram(s1, s2):

#     if len(s1) != len(s2):
#         return False

#     return sorted(s1) == sorted(s2)


# print(isAnagram("listen", "silent"))

