import random


def find_password(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if num % (i + j) == 0:
                result += (str(i) + str(j))

    return result


list_number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num = random.choice(list_number)
print(f'{num} - число из первой вставки')
print(f'Пароль: {find_password(num)}')
