your_list = list(map(int, input('Enter your data: ').split()))
if not your_list:
    print(0)
else:
    print(f'Your list: {your_list}')

    sum_even_index = sum(your_list[::2])
    result = sum_even_index * your_list[-1]
    print('Your_result:', result)