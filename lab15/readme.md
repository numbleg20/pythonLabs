
# Лабораторна робота №15: Overview of Big Data Technologies<br>
**Мета роботи:** Ознайомлення з основними технологіями обробки великих даних та їх застосування в Python.

**Завдання:**<br>
> Створити функцію clean_data(), яка приймає довгий рядок даних, розділених комами, і використовує map() для повернення списку даних, кожен з яких позбавлений пробілів і переведений в нижній регістр.

> Створити функцію filter_emails(), яка приймає довгий рядок, що містить адреси електронної пошти, і використовує filter() для повернення списку лише дійсних адрес електронної пошти. Адреса є дійсною, якщо вона містить рівно один символ '@'.

> Створити функцію extract_keywords(), яка приймає довгий рядок слів і використовує filter() для повернення списку слів, які довші за вказану довжину.

> Створити функцію process_text(), яка приймає довгий рядок текстових даних і використовує map() для видалення пробілів, спеціальних символів і переведення тексту в нижній регістр, а потім використовує filter() для повернення списку без порожніх або дуже коротких записів.

> Створити функцію normalize_data(), яка приймає довгий рядок числових значень, розділених комами, і нормалізує їх до діапазону від 0 до 1 на основі максимального значення.

> Створити функцію concatenate_strings(), яка приймає кілька рядків, розділених спеціальним символом, і конкатенує їх в один рядок без цього роздільника.

> Створити функцію sum_numeric_strings(), яка приймає рядок, що містить числа, розділені комами, і обчислює їх суму.

> Створити функцію filter_numbers(), яка використовується для фільтрації чисел з рядка, значення яких вище заданого порогу.

> Створити функцію map_to_squares(), яка приймає рядок чисел, конвертує їх у їх квадрати і повертає список цих значень.

> Створити функцію reverse_strings(), яка приймає рядок слів, розділених комами, і реверсує кожне слово.

**Виконання роботи:**
Кожне завдання було реалізовано окремою функцією. Для перевірки правильності роботи функцій використовувалися тестові випадки.

**Використання:**<br>

``` Python
data = " Apple,  Banana , orange "
cleaned_data = clean_data(data)
print(cleaned_data)  # Output: ['apple', 'banana', 'orange']

emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails)  # Output: ['test@example.com', 'example@test.co']

words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words)  # Output: ['apple', 'banana']

texts = "Hello! , Yes? , No. , "
processed_texts = process_text(texts)
print(processed_texts)  # Output: ['hello', 'yes', 'no']

numbers = "10, 20, 30, 40, 50"
normalized_numbers = normalize_data(numbers)
print(normalized_numbers)  # Output: [0.2, 0.4, 0.6, 0.8, 1.0]

data_to_concatenate = "Hello, World!, How, are, you?"
separator = ","
concatenated_data = concatenate_strings(data_to_concatenate, separator)
print(concatenated_data)  # Output: "Hello World! How are you?"

numeric_strings = "10, 20, abc, 30, def, 40"
sum_of_numeric_strings = sum_numeric_strings(numeric_strings)
print(sum_of_numeric_strings)  # Output: 100

numbers_to_filter = "10, 20, abc, 30, def, 40"
threshold = 25
filtered_numbers = filter_numbers(numbers_to_filter, threshold)
print(filtered_numbers)  # Output: [30, 40]

numbers_to_square = "1, 2, 3, 4, 5"
squared_numbers = map_to_squares(numbers_to_square)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

strings_to_reverse = "apple, banana, orange, PEAR, kiwi"
reversed_strings = reverse_strings(strings_to_reverse)
print(reversed_strings)  # Output: ['elppa', 'ananab', 'egnaro', 'RAEP', 'iwik']

```

**Висновки:** У цій лабораторній роботі було розглянуто імплементацію функцій для роботи зі строками даних, електронними адресами, числовими значеннями, словами та текстом. Кожна функція була реалізована з використанням вбудованих методів Python,таких як map(), filter(), split(), join() та регулярних виразів для досягнення потрібного функціоналу.

**Інструкції з запуску:**
> Вимоги до середовища: Python 3.<br>
> Необхідні бібліотеки: всі необхідні бібліотеки є стандартними для Python 3.
