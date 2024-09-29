class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
        if self.__is_valid_vin(vin):
            self.__vin = vin

    def __is_valid_vin(self, vin):
        if vin > 9999999 or vin < 1000000:
            raise IncorrectVinNumber(
                message='Неверный диапазон для vin номера')
        elif not isinstance(vin, int):
            raise IncorrectVinNumber(message='Некорректный тип vin номера')
        return True

    def __is_valid_numbers(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers(
                message='Некорректный тип данных для номера')
        elif len(number) > 6 or len(number) < 0:
            raise IncorrectCarNumbers(message='Неверная длинна номера')
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
