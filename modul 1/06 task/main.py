my_dict = {'Mark': 2000, 'Anton': 1983}

print(my_dict)
print(my_dict['Mark'])
my_dict['Alisa'] = 1999
print(my_dict['Alisa'])
my_dict.update({'Sergey': 2003, 'Masha': 2007})
mark_del = my_dict.pop('Mark')
print(mark_del)
print(my_dict)
