
import re as re
# def reverse_seq(n):
#     return range(n, 0, -1)

# def even_or_odd(number):
#     return "Odd" if number % 2 else "Even"

# def DNA_to_RNA(dna):
#     return dna.replace("T", "U")

# def paperwork(n, m):
    # Happy Coding! ^_^
#     if n<0 or m<0:
#         return 0
#     else: return n*m

# def paperwork(n, m):
#     return n * m if n > 0 and m > 0 else 0

# # import math
# def grow(arr):
#     return math.prod(arr)

# def grow(arr):
#     product=1
#     for i in arr:
#         product*= i
#         return product

# def get_grade(s1, s2, s3):
#     # Code here
#     avg=(s1+s2+s3)/3
#     if 90<=avg<=100:
#         return 'A'
#     elif 80<=avg<=90:
#         return 'B'
#     elif 70<=avg<=80:
#         return 'C'
#     elif 60<=avg<=70:
#         return 'D'
#     elif 0<=avg<=60:
#         return 'F'

# def basic_op(operator, value1, value2):
#     #your code here
#     if operator == "+":
#         return value1 + value2
#     elif operator == "-":
#         return value1 - value2
#     elif operator == "*":
#         return value1 * value2
#     elif operator == "/":
#         return value1 / value2
    
# def basic_op(operator, value1, value2):
#     return eval("{}{}{}".format(value1, operator, value2))

# def abbrev_name(name):
#     return ".".join(word[0].upper() for word in name.split())

# def abbrevName(name):
#     return '.'.join(w[0] for w in name.split()).upper()

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     #Happy Coding! ;)
#     if distance_to_pump<=(mpg*fuel_left):
#         return True
#     else: return False

# def zeroFuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump <= mpg * fuel_left

# def century(year):
#     # Finish this :)
#     return (year-1)//100 +1

# def century(year):
#     return (year + 99) // 100

# def number_to_string(num):
#     return str(num)

# def square_digits(num):
#     output = "".join(str(int(digit) ** 2) for digit in str(num))
#     result = int(output)
#     return result,

# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)

# def add_binary(a,b):
#     sum = a+b
#     binary=bin(sum)[2:]
#     return binary

# def add_binary(a,b):
#     return bin(a+b)[2:]

# def rgb(r, g, b):
#     return f'{min(255,max(0,r)):02X}{min(255,max(0,g)):02X}{min(255,max(0,b)):02X}' 

# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))

# def solution(s):
#     return re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', s)

# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)

