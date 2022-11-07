# Task01
def is_sort_by_increasing(number):
    result = True
    for index in range(len(number)-1):
        if number[index] > number[index+1]:
            result = False
            return result
    return result

def is_sort_by_decreasing(number):
    result = True
    for index in range(len(number)-1):
        if number[index] < number[index+1]:
            result = False
            return result
    return result

def is_sort(number):
    if is_sort_by_increasing(number) or is_sort_by_decreasing(number):
        result = True
    else:
        result = False
    return result

lst = [1,2,3,4,55]
print(is_sort(lst))

# Task03
def elements_different(num):
    result = True
    x = []
    for i in num:
        if i in x:
            result = False
            return result
        x.append(i)
    return result

lst = [5,6,7,2,8, 8, ]
print(elements_different(lst))

def is_equal(number):
    result = True
    for index in range(len(number)-1):
        if number[index] != number[index+1]:
            result = False
            return result
    return result

lst = [8,8,6,8,8, 8, ]
print(is_equal(lst))

# Task04
def quantity2(numbers):
    even = 0
    uneven = 0
    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            uneven += 1

    print(f"even: {even}")
    print(f"uneven: {uneven}")

lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
quantity2(lst)