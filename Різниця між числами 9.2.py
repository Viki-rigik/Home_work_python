def difference(values):
    if not values:
        return 0
    max_value = max(values)
    min_value = min(values)
    your_result = max_value - min_value
    return round(your_result, 2)

print(difference([1, 2, 3]))
print(difference([5, -5]))
print(difference([10.2, -2.2, 0, 1.1, 0.5]))
print(difference([]))
