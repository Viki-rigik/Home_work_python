new_list = list(map(int, input('Enter your data by spaces: ').split()))
print(f'Your list: {new_list}')
Transferring = 0
new_list1 = [x for x in new_list if x !=Transferring]
new_list1.extend([Transferring]*new_list.count(Transferring))
print('New list', new_list1)

