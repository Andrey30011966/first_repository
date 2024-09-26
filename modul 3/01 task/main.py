calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    st = (len(string), str(string).upper(), str(string).lower())
    return st

def is_contains(string, list_to_search):
    count_calls()
    lst = []
    for i in list_to_search:
        lst.append(i.upper())
    return string.upper() in lst



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
