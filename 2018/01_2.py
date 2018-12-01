import itertools

with open('01_2_input.txt') as f:
    total = 0
    prev = [total]

    for i in itertools.cycle([int(x) for x in f.read().split('\n')[:-1]]):
        total += i
        
        print(total)

        if total in prev:
            print(total)
            break

        prev.append(total)
        
