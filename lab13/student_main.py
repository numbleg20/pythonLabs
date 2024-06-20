import re

def interpolate_missing(numb):
    interpolated = []
    for i, num in enumerate(numb):
        if num is None:
            left = next((numb[j] for j in range(i - 1, -1, -1) if numb[j] is not None), None)
            right = next((numb[j] for j in range(i + 1, len(numb)) if numb[j] is not None), None)
            if left is not None and right is not None:
                interpolatedval = left + ((right - left) / (numb.index(right) - numb.index(left))) * (i - numb.index(left))
                interpolated.append(round(interpolatedval))
            else:
                interpolated.append(left if left is not None else right)
        else:
            interpolated.append(num)
    return interpolated


def fibonacci(n):
    num1, num2 = 0, 1
    count = 0
    nums = []
    while count < n:
        nums.append(num1)
        num1, num2 = num2, num1 + num2
        count += 1
    return nums

def process_batches(list, step):
    list2 = []
    for index in range(1, len(list), step):
        list2.append(list[index])
    return list2
    
def encode_string(string):
    finally_string = ""
    counter = 1
    
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            counter += 1
        else:
            finally_string += str(counter) + string[i - 1]
            counter = 1
    finally_string += str(counter) + string[-1]

    return finally_string
    
def decode_string(string):
    decoded_string = ""
    counter = ""

    for char in string:
        if char.isdigit():
            counter += char
        else:
            decoded_string += int(counter) * char
            counter = ""

    return decoded_string

def rotate_matrix(matrix):
    length = len(matrix)
    rotated = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            rotated[j][length-1-i] = matrix[i][j]
    return rotated

def regex_search(list, regex):
    matched = []
    for x in list:
        if re.search(regex, x):
            matched.append(x)
    return matched

def merge_sorted_arrays(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def group_by_key(data, key):
    grouped_data = {}
    for d in data:
        k = d[key]
        if k in grouped_data:
            grouped_data[k].append(d['value'])
        else:
            grouped_data[k] = [d['value']]
    return grouped_data

def remove_outliers(lst):
    z = sum(lst) / len(lst)
    variance = sum((x - x) ** 2 for x in lst) / len(lst)
    std_dev = variance ** 0.5
    outliers_removed = [x for x in lst if z - 2 * std_dev <= z <= x + 2 * std_dev]
    return outliers_removed