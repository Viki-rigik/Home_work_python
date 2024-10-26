import string

your_data = input('Enter two letters separated by a hyphen (a-z): ')
first, end = your_data.split('-')
first_index = string.ascii_letters.index(first)
end_index = string.ascii_letters.index(end)
result = string.ascii_letters[first_index:end_index]

print('Result:', result)
