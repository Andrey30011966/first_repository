def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(3)
print_params(4, 7)
print_params(b = 25)
print_params(c = [1,2,3])


values_list_2 = [54.32, 'Строка' ]
values_list = [4, 'string', (1, 2)]
values_dict = {'a': 25, 'b': 'Andrey', 'c': 'Moscow'}

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2)
