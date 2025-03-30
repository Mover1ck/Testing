import unittest
import math
def my_factorial(num):  # вычисление факториала
    if num < 0 or not (isinstance(num, int)):
        raise ValueError('Аргементом функции должно являться целое число больше нуля')
    a = 1
    if num > 1:
        for i in range(1, num + 1):
            a = a * i
    return a


def get_fib(n):  # вычисление числа Фибоначчи
    if n <= 0 or not (isinstance(n, int)):
        raise ValueError('Аргументом должно быть натуральное число')
    a = []
    a.append(1)
    a.append(1)
    if n > 2:
        for i in range(2, n):
            a.append(a[i - 1] + a[i - 2])
    return a[n - 1]


def my_pow(num, st):  # возведение в степень
    if num < 0 or not isinstance(st, (int, float)) or not isinstance(num, (int, float)):
        raise ValueError('Аргументы должны быть действительными числами')
    return num ** st


def my_is_simple(num):  # проверка числа на простоту
    if not isinstance(num, int) or num <= 0:
        raise ValueError('Аргументом функции должно являться натуральное число')
    res = True
    if num > 0:
        for i in range(2, math.ceil(num / 2) + 1):
            if num % i == 0 and num != 2:
                res = False
    return res


def is_pal(st):  # проверка на палиндром
    if not isinstance(st, str):
        raise TypeError('Аргументом функции должна быть строка')
    result = True
    for i in range(0, len(st)):
        if st[i] != st[len(st) - i - 1]:
            result = False
    return result

class TestFunctions(unittest.TestCase):  # Тестирующий класс
    def test_factorial(self):
        with self.assertRaises(ValueError):
            my_factorial(2.5)
        self.assertEqual(my_factorial(0),1, 'Должно получиться 1')
        with self.assertRaises(ValueError):
            my_factorial(-1)
        self.assertEqual(my_factorial(6), 720, 'Должно получиться 720')
    def test_get_fib(self):
        with self.assertRaises(ValueError):
            get_fib(-1)
        with self.assertRaises(ValueError):
            get_fib(0)
        self.assertEqual(get_fib(2),1, 'Должно получиться 1')
    def test_my_pow(self):
        self.assertEqual(my_pow(0,2), 0, 'Должно получиться 0')
        with self.assertRaises(ValueError):
            my_pow(-5,2)
        self.assertEqual(my_pow(2,2), 4, 'Должно получиться 4')
    def test_my_is_simple(self):
        self.assertEqual(my_is_simple(5), True, 'Должно получиться "True"')
        with self.assertRaises(ValueError):
            my_is_simple(-1)
        with self.assertRaises(ValueError):
            my_is_simple(0)
    def test_is_pal(self):
        self.assertEqual(is_pal('202'))

if __name__ == '__main__':
    unittest.main()