'''Qno 1'''

def cal_sum():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    sum = (a+b)
    print(f"Sum of {a} and {b} is: {a+b}")

# cal_sum()

'''Qno 2'''

def is_even():
    a = int(input("Enter a number: "))
    if a % 2 == 0:
        print(True)
    else:
        print(False)

is_even()

'''Qno 3'''

def square_list(lst):
    return[a ** 2 for a in lst]

num = [ 3, 5, 6, 9,]
print(square_list(num))


'''Qno 4'''

def factorial(n):
    if n < 0:
        return"Factorial is not defined for negaitive number"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(6))


'''Qno 5'''

def gerater_number():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    if num1 > num2:
        return f"Greater number is {num1}"
    elif num2 > num1:
        return f"Greater number is {num2}"
    else:
        return "Both number are equal"

print(gerater_number())


'''Qno 6'''

def count_vowels():
    vowels = "aeiou"
    count = 0
    word = input("Enter a word: ").lower()
    for chr in word:
        if chr in vowels:
            count += 1
    return count
print(count_vowels())


'''Qno 7'''

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

user_input = input("Enter a number with spacing: ")

numbers = list(map(int, user_input.split()))

print(numbers)


'''Qno 8'''

def reverse_string():
    text = input("Enter a text: ")
    return text[:: -1]

print(reverse_string()) 


'''Qno 9'''

def great_num():
    if num1 > num2:
        return f"Greater number is {num1}"
    elif num2 > num1:
        return f"Greater number is {num2}"
    
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

print(great_num())

'''Qno 10'''

def reverse_string():
    return text[:: -1]

text = input("Enter a word: ")

print(reverse_string())


'''Qno 11'''

def sum_list(lst):
    total = 0
    for chr in lst:
        total += chr
    return total

user_input = input("Enter a word with spacing: ")

lst = input(user_input.split())

print(sum_list)