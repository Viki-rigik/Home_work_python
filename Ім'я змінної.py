import string
import keyword

your_string = input('Enter_your_data: ')
if your_string in keyword.kwlist:
    print(False)
elif your_string[0].isdigit():
    print(False)
elif any(char.isupper() for char in your_string):
    print(False)
elif any(char in string.punctuation.replace('_', '') for char in your_string):
    print(False)
elif your_string.count('_') > 1:
    print(False)
else:
    print(True)


