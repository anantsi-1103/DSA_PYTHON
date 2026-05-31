# ======================================
# HASHING IN PYTHON - ALL OPERATIONS
# ======================================

# -----------------------------
# 1. HASH MAP (Dictionary)
# -----------------------------

student = {
    "Anant": 90,
    "Rahul": 85,
    "Rohan": 95
}

print(student)

# Insert
student["Amit"] = 80

# Update
student["Rahul"] = 88

# Delete
del student["Rohan"]

# Search
print("Rahul Marks =", student.get("Rahul"))

print()


# -----------------------------
# 2. HASH SET
# -----------------------------

nums = {10, 20, 30, 40}

# Insert
nums.add(50)

# Delete
nums.remove(20)

# Search
print(30 in nums)

print(nums)

print()


# -----------------------------
# 3. FREQUENCY COUNT ARRAY
# -----------------------------

arr = [1,2,2,3,3,3,4,4,4,4]

freq = {}

for num in arr:
    freq[num] = freq.get(num,0) + 1

print("Frequency Count:")
print(freq)

print()


# -----------------------------
# 4. CHARACTER FREQUENCY
# -----------------------------

s = "banana"

char_freq = {}

for ch in s:
    char_freq[ch] = char_freq.get(ch,0) + 1

print(char_freq)

print()


# -----------------------------
# 5. FIRST NON REPEATING CHAR
# -----------------------------

s = "aabbcde"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0) + 1

for ch in s:
    if freq[ch] == 1:
        print("First Non-Repeating:", ch)
        break

print()


# -----------------------------
# 6. DUPLICATE DETECTION
# -----------------------------

arr = [1,2,3,4,5,2]

seen = set()

duplicate = False

for num in arr:

    if num in seen:
        duplicate = True
        print("Duplicate Found:", num)
        break

    seen.add(num)

print()


# -----------------------------
# 7. COUNT DISTINCT ELEMENTS
# -----------------------------

arr = [1,2,2,3,4,4,5]

distinct = len(set(arr))

print("Distinct Elements =", distinct)

print()


# -----------------------------
# 8. TWO SUM
# -----------------------------

def two_sum(nums,target):

    hashmap = {}

    for i,num in enumerate(nums):

        diff = target - num

        if diff in hashmap:
            return [hashmap[diff],i]

        hashmap[num] = i

    return []

print("Two Sum:",two_sum([2,7,11,15],9))

print()


# -----------------------------
# 9. LONGEST CONSECUTIVE SEQUENCE
# -----------------------------

nums = [100,4,200,1,3,2]

s = set(nums)

longest = 0

for num in s:

    if num-1 not in s:

        current = num

        length = 1

        while current+1 in s:

            current += 1

            length += 1

        longest = max(longest,length)

print("Longest Consecutive Length =", longest)

print()


# -----------------------------
# 10. GROUP ANAGRAMS
# -----------------------------

from collections import defaultdict

words = ["eat","tea","tan","ate","nat","bat"]

groups = defaultdict(list)

for word in words:

    key = "".join(sorted(word))

    groups[key].append(word)

print(list(groups.values()))

print()


# -----------------------------
# 11. SUBARRAY SUM = K
# -----------------------------

def subarray_sum(nums,k):

    prefix_sum = 0

    hashmap = {0:1}

    count = 0

    for num in nums:

        prefix_sum += num

        if prefix_sum-k in hashmap:
            count += hashmap[prefix_sum-k]

        hashmap[prefix_sum] = hashmap.get(prefix_sum,0)+1

    return count

print(subarray_sum([1,1,1],2))

print()


# -----------------------------
# 12. CUSTOM HASH TABLE
# (CHAINING)
# -----------------------------

SIZE = 10

table = [[] for _ in range(SIZE)]

def insert(key):

    index = key % SIZE

    table[index].append(key)

def search(key):

    index = key % SIZE

    return key in table[index]

insert(25)
insert(35)
insert(45)

print(table)

print("Search 35 =", search(35))