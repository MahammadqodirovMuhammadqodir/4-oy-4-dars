# 1-misol
# def count(k, numbers):
#     count = sum(1 for num in numbers if num < k)
#     return count

# k = 10
# numbers = [1, 4, 7, 10, 12]
# print(count(k, numbers))  


# 2-misol
# def first(k, numbers):
#     for i, num in enumerate(numbers):
#         if num > k:
#             return i
#     return 0

# k = 10
# numbers = [1, 4, 7, 10, 12]
# print(first(k, numbers))  

# 3-misol
# def last(k, numbers):
#     for i in range(len(numbers) - 1, -1, -1):
#         if numbers[i] > k:
#             return i
#     return 0

# k = 10
# numbers = [1, 4, 7, 10, 12]
# print(last(k, numbers))  

# 4-misol
# def repeat(b, n):
#     return [b] * n

# b = 2.5
# n = 3
# print(repeat(b, n))  

# 5-misol
# def unique(numbers):
#     unique = []
#     for num in numbers:
#         if numbers.count(num) == 1:
#             unique.append(num)
#     return unique


# numbers = [1, 2, 2, 3, 4, 4, 5]
# print(unique(numbers))  

# 6-misol
# def count(numbers):
#     count = 0
#     for i in range(1, len(numbers)):
#         if numbers[i] < numbers[i - 1]:
#             count += 1
#     return count

# numbers = [3, 2, 5, 4, 6, 1]
# print(count(numbers))  