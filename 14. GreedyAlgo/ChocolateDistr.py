
def chocolateDist(packets, students):
    packets.sort()

    n = len(packets)


    if students == 0 or n == 0:
        return 0

    if students > n:
        return -1


    min_diff = float('inf')

    for i in range(n - students + 1):

        diff = packets[i+students-1] - packets[i]

        min_diff = min(min_diff , diff)

    return min_diff





# huffman encoding #







Packets = [7, 3, 2, 4, 9, 12, 56]
Students = 3


print(chocolateDist(Packets, Students))