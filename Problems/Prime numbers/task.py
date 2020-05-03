prime_numbers = [n for n in range(2, 1001) if all([n % x for x in range(2, n)])]
# prime_numbers = [n for n in range(2, 1001) if not any([n % x == 0 for x in range(2, n)])]

# prime_numbers = []
# for i in range(2, 1000):
#     if not any(i % prime == 0 for prime in prime_numbers):
#         prime_numbers.append(i)

# prime_numbers = []
# for num in range(2, 1001):
#     if all(num % i != 0 for i in range(2, num)):
#         prime_numbers.append(num)

# prime_numbers = []
# for num in range(2, 1001):
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#     if prime:
#         prime_numbers.append(num)

# prime_numbers = []
# first_thousand_list = range(1, 1001)
# for number in first_thousand_list:
#     if number > 1:
#         if any(number % i == 0 for i in range(2, number)):
#             continue
#         prime_numbers.append(number)

