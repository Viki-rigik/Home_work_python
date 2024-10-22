import random

your_list = [random.randint(-1000, 1000) for _ in range(random.randint(3, 10))]
print('Your_list', your_list)
new_list = [your_list[0], your_list[2], your_list[-2]]
print('Your_new_list:', new_list)