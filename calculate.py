import circle  # Импортируем модуль circle, который содержит функции для работы с кругами
import square  # Импортируем модуль square, который содержит функции для работы с квадратами

figs = ['circle', 'square'] # Список доступных фигур
funcs = ['perimeter', 'area'] # Список доступных функций для расчёта
sizes = {} # Словарь для хранения размеров фигур

def calc(fig, func, size):
    """
    Функция для вычисления заданной функции (периметр или площадь) для указанной фигуры.
    
    Аргументы:
    fig -- название фигуры (например, 'circle' или 'square')
    func -- название функции (например, 'perimeter' или 'area')
    size -- размеры фигуры, передаваемые в функцию
    
    Возвращает:
    Результат вычисления и выводит его на экран.
    """
    assert fig in figs  # Проверяем, что фигура допустима
    assert func in funcs  # Проверяем, что функция допустима

    # Вычисляем результат, вызывая соответствующую функцию из модуля фигуры
    result = eval(f'{fig}.{func}(*{size}')  # Используем eval для динамического вызова функции
    print(f'{func} of {fig} is {result}')  # Выводим результат на экран

if __name__ == "__main__":
    func = ''  # Инициализация переменной для функции
    fig = ''  # Инициализация переменной для фигуры
    size = list()  # Инициализация списка для размеров

    # Цикл для ввода фигуры, пока не будет введено допустимое значение
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    
    # Цикл для ввода функции, пока не будет введено допустимое значение
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    
    # Цикл для ввода размеров фигуры, пока не будет введено нужное количество значений
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    
    # Вызываем функцию для вычисления и вывода результата
    calc(fig, func, size)
