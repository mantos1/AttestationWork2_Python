from logs import setLogging

def combinations(items, max_weight):
    setLogging(__name__, 'info', f'Запущен метод "{combinations.__name__}"')

    backpacks = []
    sorted_result = []
    for i in range(2 ** len(items)):
        backpack = {}
        weight = 0
        for j, item in enumerate(items):
            if i & (1 << j):
                if weight + float(items[item]) <= max_weight:
                    backpack[item] = float(items[item])
                    weight += float(items[item])
                else:
                    break
        backpacks.append(backpack)

    full_result = [backpack for backpack in backpacks if backpack]
    result = []
    for item in full_result:
        if item not in result:
            result.append(item)

    setLogging(__name__, 'info', f'Завершение метода "{combinations.__name__}"')
    return result


if __name__ == '__main__':
    setLogging(__name__, 'Запуск модуля.')
