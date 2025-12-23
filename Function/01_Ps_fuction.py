'''Qno 1'''

def calc_sum(a , b):
    sum = a + b
    print(sum)
    return sum

calc_sum(5 , 3) 


'''Qno 2'''

def average():
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    c = int(input("Enter number: "))
    average = (a + b + c) /3
    print(average)

average()


'''Qno 3'''

cities = ["Lahore", "Karachi", "Islamabad", "Faisalabad", "RawalPindi"]
heroes = ["Marvel", "Spiderman", "Joker", "Superman"]
color = ["Black", "White", "Blue", "Purple", "Orange", "Red", "Green"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item)

print_list(color)

print_len(cities)

'''Qno 3(b)'''

def list(text):
    total = 0
    for word in text:
        total += len(word)
    return total

user_input = input("Enter a text with spacing: ")
text = user_input.split()

print(text)


'''Qno 4'''

n = int(input("Enter number: "))

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(n)


'''Qno 5'''

usd = int(input("Enter USD: "))

def converter(usd):
    pkr = usd * 280
    print(pkr)

converter(usd)

'''Qno 6'''

num = int(input("Enter number: "))

def find(num):
    if num % 2 == 0:
        return("Even")
    else:
        return("Odd")

result = find(num)
print(result)

'''Qno 7'''

def find(num):
    print("Even" if num%2 == 0 else "Odd")

num = int(input("Enter number: "))

find(num)


def calc_sum(a,b):
    sum = (a+b)
    print(sum)

calc_sum(5,6)
