'''Qno 1'''

# def cal_sum():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     sum = (a+b)
#     print(f"Sum of {a} and {b} is: {a+b}")

# cal_sum()

'''Qno 2'''

# def is_even():
#     a = int(input("Enter a number: "))
#     if a % 2 == 0:
#         print(True)
#     else:
#         print(False)

# is_even()

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

print(factorial(5))

