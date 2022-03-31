def find_minimum(inptList):
    mini = inptList[0]
    for i in range(1, len(inptList)):
        if inptList[i] < mini:
            mini = inptList[i]
        else:
            pass
    return mini

def find_minimum_indx(lst):
    mini = lst[0]
    pos = 0
    for i in range(1, len(lst)):
        if lst[i] < mini:
            mini = lst[i]
            pos = i
        else:
            pass
    return mini,pos

if __name__ == '__main__':
    lst = [23, -123, 56, -567, 90, 100]

    minimum, position = find_minimum_indx(lst)
    print("Lista: ", lst)
    print("Minimum: ", minimum)
    print("Position: ", position)
