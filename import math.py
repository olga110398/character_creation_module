"""Документация модуля. Описывает работу классов и функций. 
Размещается в верхней части файла (начиная с первой строки).
"""
def tricky_func(self):
    """Описывает работу функции tricky_func."""
    ...


class Test:
    """Класс Test используется для демонстрации docstring."""

    def first(self):
        """Описывает метод first и демонстрирует перенос строки 
        документации.
        """
        ...


print(__doc__)
print(tricky_func.__doc__)
print(Test.__doc__)
print(Test.first.__doc__)