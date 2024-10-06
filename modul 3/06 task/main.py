def calculate_structure_sum(number):
    summ = 0
    if isinstance(number, (int, float)):
        summ += number
    if isinstance(number, str):
        summ += len(number)
    if isinstance(number, dict):
        for key, value in number.items():
            summ += calculate_structure_sum(key)
            summ += calculate_structure_sum(value)
    if isinstance(number, (list, tuple, set)):
        for i in number:
            summ += calculate_structure_sum(i)

    return summ


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
