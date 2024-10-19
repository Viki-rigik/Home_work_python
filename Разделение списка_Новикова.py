L1 = list(map(int, input('Enter your data by spaces: ').split()))
print(f'Your list: {L1}')

if len(L1) == 0:
    result = [[], []]
else:
    half = (len(L1) + 1) // 2
    part1 = L1[:half]
    part2 = L1[half:]
    result = [part1, part2]
print('Result:', result)
