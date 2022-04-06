from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

result = []

# Заполним result_list значениями,
# которые не повторяются в списке src
start = perf_counter()
for val in src:
    if src.count(val) == 1:
        result.append(val)
print('result = ', result, ' Время выполнения: ', perf_counter() - start)

# тот же алгоритм, но с более короткой записью
result.clear()
start = perf_counter()
result = [val for val in src if src.count(val) == 1]
print('result = ', result, ' Время выполнения: ', perf_counter() - start)

# Через проверку уникальности
# ВРОДЕ КАК САМЫЙ ЛУЧШИЙ!!!
result.clear()
start = perf_counter()
for val in src:
    if val not in result:
        result.append(val)
print('result = ', result, ' Время выполнения: ', perf_counter() - start)

# Вариант с множеством, но если не важен исходный порядок
# Не удивительно что долгий, так как все сначало пишется во множество,
# а потом конвертиться в список
result.clear()
start = perf_counter()
result = [val for val in set(src) if src.count(val) == 1]
print('result = ', result, ' Время выполнения: ', perf_counter() - start)

# Небольшая модификация предыдущего варианта
result.clear()
start = perf_counter()
s = set()
result = list([(s.add(val) or val) for val in src if val not in s])
print('result = ', result, ' Время выполнения: ', perf_counter() - start)
