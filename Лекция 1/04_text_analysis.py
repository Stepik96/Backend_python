# Задача 4 (слайд 22): учитываем все символы, включая пробелы.
text = input("Введите текст: ").lower()
symbol_counts = {}
for symbol in text:
    symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
print("Количество каждого символа:")
for symbol, count in symbol_counts.items():
    print(f"{symbol!r}: {count}")
# Сортируем по количеству; при равенстве сохраняется порядок появления.
frequent_symbols = sorted(symbol_counts, key=symbol_counts.get, reverse=True)
print("Три самых частых символа:")
for symbol in frequent_symbols[:3]:
    print(f"{symbol!r}: {symbol_counts[symbol]}")
