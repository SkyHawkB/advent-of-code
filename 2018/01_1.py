with open('01_1_input.txt') as f:
    TOTAL = 0
    INPUTS = f.read().split('\n')

    for i in INPUTS:
        if i != '':
            TOTAL += int(i)

    print(TOTAL)
