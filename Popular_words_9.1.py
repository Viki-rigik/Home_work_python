def popular_words(text, words):
    text = text.lower().split()
    text_result = {}

    for every_word in words:
        text_result[every_word] = text.count(every_word)
    return text_result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')