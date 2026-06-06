def maxMeeting(start, end):

    meeting = []

    for i in range(len(start)):
        meeting.append((end[i], start[i]))

    # sort 
    meeting.sort()


    count = 1
    last_end = meeting[0][0]

    for i in range(1, len(meeting)):

        currStart = meeting[i][1]

        # 
        if currStart > last_end:
            count += 1
            last_end = meeting[i][0]


    return count




start = [900, 940, 950, 1100, 1500, 1800]
end = [910, 1200, 1120, 1130, 1900, 2000]

print(maxMeeting(start, end))