from logs import setLogging
from sys import argv
from comb import combinations

if __name__ == '__main__':
    """
    Программа для составления списка вещей, которые помещаются в рюкзак.
    
    Пример запуска из командной строки: 'python .\main.py зажигалка=0.1,книга=0.2 1.0'
    """

    setLogging(__name__, 'info', f'Запуск программы.')
    try:
        items = {
            "ключи": 0.3,
            "кошелек": 0.2,
            "телефон": 0.5,
            # "книга": "один", # Для примера обработки исключений.
            "зажигалка": 0.1
        }
        max_weight: float = 1.0

        if len(argv) > 1:
            items_argv = argv[1]
            max_weight_argv = argv[2]
            items_dict = dict(pair.split('=') for pair in items_argv.split(','))
            items = items_dict
            max_weight = float(max_weight_argv)

        setLogging(__name__, 'info', f'Переданы следуюшие предметы "{items = }", а так же установлено значение "{max_weight = }"')

        result = combinations(items, max_weight)
        print('Результат: ', result)
    except Exception as e:
        setLogging(__name__, 'error', 'Возникло исключение!')
    finally:
        setLogging(__name__, 'info', f'Завершение программы.\n{"="*100}')

