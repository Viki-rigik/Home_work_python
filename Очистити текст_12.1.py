import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cleaned = re.sub(r'<.*?>', '', html)
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned)

    print(f"The cleaned file is saved in '{result_file}'")

delete_html_tags('draft.html')

