def common_elements():
    list_with_3 = [x for x in range(100) if x % 3 == 0]
    list_with_5 = [x for x in range(100) if x % 5 == 0]

    set_with_3 = set(list_with_3)
    set_with_5 = set(list_with_5)
    intersection_set = set_with_3.intersection(set_with_5)
    return intersection_set

result = common_elements()

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')


