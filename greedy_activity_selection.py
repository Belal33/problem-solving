# activity Sessions


# Sort the activities based on finish time


def activity_selection(start, finish):
    i = 1
    i_end = 0
    seq = [0]
    while i < len(start):
        if start[i] >= finish[i_end]:
            seq.append(i)
            i_end = i
        i += 1
    return seq


start = [9, 10, 11, 12, 13, 15]
finish = [11, 11, 12, 14, 15, 16]
print(activity_selection(start, finish))
