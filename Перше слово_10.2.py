def first_word(text):
    """ Пошук першого слова """
    text = text.replace(".", " ").replace(",", " ")
    your_text = text.split()
    return your_text[0] \
        if your_text \
        else ""

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')