'''Q1'''

for num in range(1,6):
    print(num,end=" ")


'''Q2'''

for i in range(1,6):
    print(i ** 2, end=" ")



'''Q3'''

for e in range(1,11):
    if e % 2 == 0:
        print(e, end=" ")


'''Q4'''

sum = 0
for i in range(1,11):
    sum += i
    print(f"Sum is {sum}")


'''Q5'''

word = "Python"

for i in range(len(word) -1, -1, -1):
    print(word[i], end=" ")

'''Effecience Way!'''
letter = "Jhon smith"
print(letter[::-1])


'''Q6'''

vowels = "aeiou"
word = "assigement"
count = 0

for chr in word.lower():
    if chr in vowels:
        count += 1 
print(count)


'''Q7'''

a = 0
b = 1
print(a,b, end=" ")

for i in range(1):
    next_value = a + b
    a,b = b,next_value
    print(next_value, end=" ")


'''Q8'''

n = int(input("Enter number:"))
factorial = 1

for i in range(1, n+1):
    factorial *= i 
    print(factorial, end=" ")

