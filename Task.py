# Дано положительное число. Найти сумму его цифр. Если передаётся не число, то вернуть "Чё, самый умный?"
# Начинаем с тестирования.
# if number = 42
#   return 6
# if number = {text}
#   return 'Чё, самый умный?'
number = (input('Input an integer positive number: '))
def sum_of_digits(number):
    if type(number) != int:
        return print('Чё, самый умный?')
    else:
        sum = 0
        while number != 0:
            sum += number % 10
            number //= 10

        return print(sum)
sum_of_digits(number)

