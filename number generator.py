import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('Начало лога\n\n')

random_data = np.random.randint(-10000, 10001, size=1000)

# отчистка от цифового мусора
min_meaning = -10000
max_meaning = 10001

def clean_data(input_list, min_bound=-10000, max_bound=10001):

    print("Начинаем отчистку данных...")
    cleaned = []
    for item in input_list:
        # проверка на пустые значения
        if item is None or (isinstance(item, float) and math.isnan(item)):
            continue

        # проверка попадания в целевой диапазон
        if item < min_bound or item > max_bound:
            continue

        # сохраняем
        cleaned.append(item)
    print("Отчистка данных завершена")
    return cleaned[:1000]

# Запуск очистки данных
validated_data = clean_data(random_data)

# объект Series
series = pd.Series(validated_data)

with open('random_numbers.txt', 'w', encoding='utf-8') as file:
    for number in series:
        file.write(f"{number}\n")

print(f"\n{series}")
print("\nПромежуточное сохранение в текстовый файл\n\n")
#print(series)


# рассчет стандартных числовых характеристик
min_value = series.min()
max_value = series.max()
sum_values = series.sum()
std_deviation = series.std()

total_count = len(series)
unique_count = series.nunique()
duplicate_count = total_count - unique_count

print("Стандартные числовые характеристики набора данных:")
print(f"Минимальное значение: {min_value}")
print(f"Количество повторяющихся значений (дубликатов): {duplicate_count}")
print(f"Максимальное значение: {max_value}")
print(f"Сумма всех чисел: {sum_values}")
print(f"Среднеквадратическое отклонение: {std_deviation:.2f}")


def math_round(x):
    sign = 1 if x >= 0 else -1
    abs_x = abs(x) / 100
    rounded = math.floor(abs_x + 0.5)
    return sign * rounded * 100

rounded_series = series.apply(math_round)

# визуализация данных

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)  # (строк, столбцов, номер графика)
plt.plot(series, color='royalblue', linewidth=0.7, label='Исходные числа')
plt.title('Линейный график')
plt.xlabel('Индекс элемента')
plt.ylabel('Значение')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.subplot(1, 2, 2)

unique_bins = np.arange(rounded_series.min() - 50, rounded_series.max() + 150, 100)
plt.hist(rounded_series, color='green', edgecolor='black', alpha=0.8, rwidth=0.8)
plt.title('Гистограмма')
plt.xlabel('Округленные значения')
plt.ylabel('Частота (кол-во чисел)')
plt.grid(True, linestyle='--', alpha=0.6)

plt.gca().patches[0].set_facecolor('#2ecc71')
for patch in plt.gca().patches:
    patch.set_facecolor('#2ecc71')

plt.tight_layout()
plt.show()

# создание датафрейма
df = pd.DataFrame({'Исходные данные': series})

#reset_index(drop=True)
df['По возрастанию'] = series.sort_values(ascending=True).reset_index(drop=True)

df['По убыванию'] = series.sort_values(ascending=False).reset_index(drop=True)

df.to_csv('sorted_numbers.csv', index=False, encoding='utf-8-sig')

print("\n\nФайл 'sorted_numbers.csv' успешно сохранен\n\n")
print(df.head(10))

# вторая визуализаци
plt.figure(figsize=(10, 6))

# график по возрастанию
plt.plot(df['По возрастанию'], color='darkgreen', linewidth=2, label='По возрастанию')

# график по убыванию
plt.plot(df['По убыванию'], color='crimson', linewidth=2, label='По убыванию')

plt.title('Графики отсортированных значений', fontsize=14)
plt.xlabel('Порядковый номер (индекс)', fontsize=12)
plt.ylabel('Значение числа', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)

plt.legend(fontsize=11)

plt.tight_layout()
plt.show()

print("\nРабота завершена")
