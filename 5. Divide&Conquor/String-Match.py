def stringMatching(text, pattern):
    n = len(text)
    m = len(pattern)

    # 23 - 4 + 1 = 20
    for i in range(n - m + 1 ):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j+=1

        if j == m:
            print(f"Pattern found at index {i}")


text = "AAAAAABABAAAAA"
pattern = "BABA"


stringMatching(text,pattern)