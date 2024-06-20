
# Лабораторна робота №17: Generators and Data Structures<br>
**Мета роботи:** Розробити генератори для різних задач, таких як обхід списків, генерація чисел, обхід графів і дерев.

**Завдання:**<br>
> Task 1: Create a generator to iterate over a list of numbers.
Create a generator function named number_generator that takes a list of numbers and yields each number one by one.

> Task 2: Develop a generator that yields even numbers from a given range.
Create a generator function named even_number_generator that takes two integers, start and end, and yields even numbers within that range.

> Task 3: Implement a generator to yield odd numbers within a specified range.
Create a generator function named odd_number_generator that takes two integers, start and end, and yields odd numbers within that range.

> Task 4: Write a generator that produces Fibonacci numbers.
Create a generator function named fibonacci_generator that produces Fibonacci numbers indefinitely.

> Task 5: Create a generator that yields prime numbers up to a given limit.
Create a generator function named prime_number_generator that takes an integer limit and yields prime numbers up to that limit.

> Task 6: Develop a generator to traverse a binary tree in pre-order.
Create a generator function named pre_order_traversal that takes the root of a binary tree and yields its nodes in pre-order.

> Task 7: Implement a generator for in-order traversal of a binary tree.
Create a generator function named in_order_traversal that takes the root of a binary tree and yields its nodes in in-order.

> Task 8: Write a generator for post-order traversal of a binary tree.
Create a generator function named post_order_traversal that takes the root of a binary tree and yields its nodes in post-order.

> Task 9: Create a generator to traverse a graph using depth-first search (DFS).
Create a generator function named dfs_traversal that takes an adjacency list representation of a graph and a starting node, and yields nodes in DFS order.

> Task 10: Develop a generator for breadth-first search (BFS) traversal of a graph.
Create a generator function named bfs_traversal that takes an adjacency list representation of a graph and a starting node, and yields nodes in BFS order.

> Task 11: Implement a generator that yields the keys of a dictionary.
Create a generator function named dict_keys_generator that takes a dictionary and yields its keys one by one.

> Task 12: Write a generator that yields the values of a dictionary.
Create a generator function named dict_values_generator that takes a dictionary and yields its values one by one.

> Task 13: Create a generator to iterate over key-value pairs of a dictionary.
Create a generator function named dict_items_generator that takes a dictionary and yields its key-value pairs as tuples one by one.

> Task 14: Develop a generator that yields lines from a file one by one.
Create a generator function named file_lines_generator that takes a file path and yields its lines one by one.

> Task 15: Implement a generator to iterate over words in a text file.
Create a generator function named file_words_generator that takes a file path and yields its words one by one.

> Task 16: Write a generator that yields characters from a string one by one.
Create a generator function named string_chars_generator that takes a string and yields its characters one by one.

> Task 17: Create a generator to yield unique elements from a list.
Create a generator function named unique_elements_generator that takes a list and yields its unique elements one by one.

> Task 18: Develop a generator that yields elements of a list in reverse order.
Create a generator function named reverse_list_generator that takes a list and yields its elements in reverse order.

> Task 19: Implement a generator to yield the Cartesian product of two lists.
Create a generator function named cartesian_product_generator that takes two lists and yields the Cartesian product of the two lists as tuples.

> Task 20: Write a generator that yields permutations of a list.
Create a generator function named permutations_generator that takes a list and yields all possible permutations of the list.

> Task 21: Create a generator to yield combinations of a list of elements.
Create a generator function named combinations_generator that takes a list of elements and yields all possible combinations of the elements.

> Task 22: Develop a generator to iterate over a list of tuples.
Create a generator function named tuple_list_generator that takes a list of tuples and yields each tuple one by one.

> Task 23: Implement a generator that yields elements from multiple lists in parallel.
Create a generator function named parallel_lists_generator that takes multiple lists and yields elements from each list in parallel.

> Task 24: Write a generator that yields elements from a nested list (flattening the list).
Create a generator function named flatten_list_generator that takes a nested list and yields each element in a flat sequence.

> Task 25: Create a generator to yield elements from a nested dictionary.
Create a generator function named nested_dict_generator that takes a nested dictionary and yields its elements.

> Task 26: Develop a generator to yield powers of 2 up to a given number.
Create a generator function named powers_of_two_generator that takes an integer n and yields powers of 2 up to 2n.

> Task 27: Implement a generator that yields powers of a given base up to a specified limit.
Create a generator function named powers_of_base_generator that takes a base and a limit, and yields powers of the base up to the specified limit.

> Task 28: Write a generator to yield the squares of numbers in a given range.
Create a generator function named squares_generator that takes a range of numbers and yields their squares.

> Task 29: Create a generator to yield cubes of numbers in a specified range.
Create a generator function named cubes_generator that takes a range of numbers and yields their cubes.

> Task 30: Develop a generator that yields factorials of numbers up to a given limit.
Create a generator function named factorials_generator that takes an integer n and yields factorials of numbers from 0 up to n.

> Task 31: Implement a generator to yield numbers in the Collatz sequence.
Create a generator function named collatz_sequence_generator that takes an integer and yields numbers in the Collatz sequence.

> Task 32: Write a generator that yields numbers in a geometric progression.
Create a generator function named geometric_progression_generator that takes an initial term, a common ratio, and a limit, and yields numbers in the geometric progression.

> Task 33: Create a generator to yield numbers in an arithmetic progression.
Create a generator function named arithmetic_progression_generator that takes an initial term, a common difference, and a limit, and yields numbers in the arithmetic progression.

> Task 34: Develop a generator that yields the running sum of a list of numbers.
Create a generator function named running_sum_generator that takes a list of numbers and yields their running sum.

> Task 35: Implement a generator to yield the running product of a list of numbers.
Create a generator function named running_product_generator that takes a list of numbers and yields their running product.

**Виконання роботи:**
Кожне завдання було реалізовано окремою функцією. Для перевірки правильності роботи функцій використовувалися тестові випадки.

**Використання:**<br>

``` Python
gen = file_lines_generator('example.txt')
for line in gen:
    print(line)

gen = file_words_generator('example.txt')
for word in gen:
    print(word)

gen = string_chars_generator('Hello')
for char in gen:
    print(char)

gen = unique_elements_generator([1, 2, 2, 3, 3, 3])
for unique in gen:
    print(unique)

gen = reverse_list_generator([1, 2, 3, 4, 5])
for reversed in gen:
    print(reversed)

gen = cartesian_product_generator([1, 2], ['a', 'b'])
for product in gen:
    print(product)

gen = permutations_generator([1, 2, 3])
for perm in gen:
    print(perm)

gen = combinations_generator([1, 2, 3])
for comb in gen:
    print(comb)

gen = tuple_list_generator([(1, 2), (3, 4), (5, 6)])
for tup in gen:
    print(tup)

gen = parallel_lists_generator([1, 2, 3], ['a', 'b', 'c'])
for pair in gen:
    print(pair)

gen = flatten_list_generator([1, [2, [3, 4], 5], 6])
for flattened in gen:
    print(flattened)

gen = nested_dict_generator({'a': {'b': 1, 'c': 2}, 'd': 3})
for item in gen:
    print(item)

gen = powers_of_two_generator(4)
for power in gen:
    print(power)

gen = powers_of_base_generator(3, 81)
for power in gen:
    print(power)

gen = squares_generator(1, 5)
for square in gen:
    print(square)

gen = cubes_generator(1, 4)
for cube in gen:
    print(cube)

gen = factorials_generator(4)
for factorial in gen:
    print(factorial)

gen = collatz_sequence_generator(6)
for number in gen:
    print(number)

gen = geometric_progression_generator(2, 3, 20)
for number in gen:
    print(number)

gen = arithmetic_progression_generator(2, 3, 20)
for number in gen:
    print(number)

gen = running_sum_generator([1, 2, 3, 4])
for sum_value in gen:
    print(sum_value)

gen = running_product_generator([1, 2, 3, 4])
for product_value in gen:
    print(product_value)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = pre_order_traversal(root)
for node in gen:
    print(node.val)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = in_order_traversal(root)
for node in gen:
    print(node.val)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = post_order_traversal(root)
for node in gen:
    print(node.val)

graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}
gen = dfs_traversal(graph, 1)
for node in gen:
    print(node)

graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}
gen = bfs_traversal(graph, 1)
for node in gen:
    print(node)

gen = dict_keys_generator({'a': 1, 'b': 2, 'c': 3})
for key in gen:
    print(key)

gen = dict_values_generator({'a': 1, 'b': 2, 'c': 3})
for value in gen:
    print(value)

gen = dict_items_generator({'a': 1, 'b': 2, 'c': 3})
for item in gen:
    print(item)

gen = powers_of_two_generator(4)
for power in gen:
    print(power)

gen = powers_of_base_generator(3, 81)
for power in gen:
    print(power)

gen = squares_generator(1, 5)
for square in gen:
    print(square)

gen = cubes_generator(1, 4)
for cube in gen:
    print(cube)

gen = factorials_generator(4)
for factorial in gen:
    print(factorial)

gen = collatz_sequence_generator(6)
for number in gen:
    print(number)

gen = geometric_progression_generator(2, 3, 20)
for number in gen:
    print(number)

gen = arithmetic_progression_generator(2, 3, 20)
for number in gen:
    print(number)

gen = running_sum_generator([1, 2, 3, 4])
for sum_value in gen:
    print(sum_value)

gen = running_product_generator([1, 2, 3, 4])
for product_value in gen:
    print(product_value)
```
**Результати:** В ході роботи були розроблені генератори для різноманітних завдань, що охоплюють багато аспектів програмування. Кожен генератор було імплементовано з урахуванням специфіки його функціональності, що дозволяє ефективно створювати послідовності значень або обробляти структури даних.

**Висновки:** Виконання цієї роботи було успішним і задовольнило вихідні цілі. Під час розробки були ідентифіковані й виправлені деякі потенційні проблеми з методами генераторів, що підтверджується результатами тестування. Кожен з генераторів працює стабільно та з високою точністю відповідно до очікувань.

**Інструкції з запуску:**
> Вимоги до середовища: Python 3.<br>
> Необхідні бібліотеки: всі необхідні бібліотеки є стандартними для Python 3.
