def correct_sentence(text):
    parts = text.split('.', 1)
    part1 = parts[0].strip().capitalize()
    if len(parts) > 1 and parts[1].strip():
        part2 = parts[1].strip().capitalize()
        return f"{part1}. {part2}."
    else:
        return f"{part1}."


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')