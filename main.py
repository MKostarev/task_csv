import pandas as pd

file_path = 'Scheta.csv'

# настройка отображения
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# чтение файла csv в DataFrame
data = pd.read_csv(file_path, encoding='utf-8', delimiter='\t')

# вводим номер объекта
desired_value = input("Номер объекта: ")


# выводим количество объектов по счёту
data['Количество значений'] = data['Комментарий'].str.split(',').apply(len)

# убираем пробелы и символы '\xa0', заменяем запятые на точки в столбце "Всего"
data['Всего'] = data['Всего'].str.replace(r'\s| ', '', regex=True).str.replace(',', '.', regex=False).astype(float)

# создаем столбец "Среднее значение"
data['Среднее значение'] = data['Всего'] / data['Количество значений']

# округляем значения в столбце "Среднее значение" до 2 знаков после запятой
data['Среднее значение'] = data['Среднее значение'].round(2)

# функция для проверки, содержит ли строка нужное значение в списке
def contains_desired_value(comment, desired_value):
    values_list = [value.strip() for value in comment.split(',')]  # разбиваем строку на список значений
    return desired_value in values_list

filtered_data = data[data['Комментарий'].apply(lambda x: contains_desired_value(x, desired_value))]

print(filtered_data)

total_sum = data['Среднее значение'].sum()

# форматирование числа с разделением тысяч пробелами и двумя знаками после запятой
total_sum = '{:,.2f}'.format(total_sum).replace(',', ' ')

print("Сумма расходов по объекту ", desired_value, 'равна: ', total_sum, 'руб.')
