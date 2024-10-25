import string

your_string = input('Enter_your_data:')
string_without_spaces = " "
for sign in your_string:
    if sign not in string.punctuation:
        string_without_spaces += sign
entered_words = string_without_spaces.split()
hashtag = '#' + ''.join(entered_word.capitalize() for entered_word in entered_words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print('Hashtag: ', hashtag)