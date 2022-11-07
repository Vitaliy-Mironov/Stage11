# Task01
def max(numbers):
    result = numbers[0]
    for i in numbers:
        if i > result:
            result = i

    return result

list = [12, 45, 56, 74, 5, 102, 33, -450, 222.15]

print(max(list))

# # Task02
def min(numbers):
    result = numbers[0]
    for i in numbers:
        if i < result:
            result = i

    return result

list = [12, 45, 56, 74, 5, 102, 33, -450, 222.15]

print(min(list))


# Task03
def sa(numbers):
    sum = 0
    for i in numbers:
        sum += i
    result = sum/len(numbers)
    return result

list = [10, -20, 30.5]

print(sa(list))


# Task04
def quantity(numbers):
    positive = 0
    negative = 0
    zoro = 0
    for i in numbers:
        if i > 0:
            positive += 1
        if i < 0:
            negative += 1
        if i == 0:
            zoro += 1
    print(f"positive: {positive}")
    print(f"negative: {negative}")
    print(f"zero: {zoro}")

list = [12, 45, -56, 74, 0, 0, 5, 102, 33, -450, 222.15]

quantity(list)

# Task05
def elements(numbers):
    count = 0
    min = numbers[0]
    max = numbers[0]
    index_min = 0
    index_max = 0
    for i in numbers:
        if i < min:
            min = i
            index_min = count
        if i > max:
            max = i
            index_max = count
        count += 1
    numbers[index_min], numbers[index_max] = numbers[index_max], numbers[index_min]
    return numbers

list = [10, -20, 30.5, 30.5, 0, 5, -20]
print(list)
print(elements(list))