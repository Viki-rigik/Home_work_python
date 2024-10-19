L1 = list(map(int, input('Enter your data by spaces: ').split()))
print(f'Your list: {L1}')
if len(L1) > 1:
    L1 = [L1[-1]] + L1[:-1]

print('Result:', L1)