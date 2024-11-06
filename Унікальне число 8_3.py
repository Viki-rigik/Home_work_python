from collections import Counter

def find_unique_value(some_list):
    counts = Counter(some_list)
    unique_value = [item for item, count in counts.items() if count == 1]
    return unique_value[0] if unique_value else None


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")