'''Qno 1 Count Vowels'''

vowels = "aeiou"
words = input("Enter your word :")
count = 0

for chr in words:
    if chr in vowels:
        count += 1
print(count)

'''Qno 2(a) Sum of Even Numbers'''

n = int(input("Enter your number: "))
total = 0

for i in range(2,n+1,2):
    if n % 2 == 0:
        total += i
print(total)

'''Qno 2(b) Sum of Number'''

n = int(input("Enter your number: "))
total = 0

for i in range(1,n+1):
    total += i
print(total)

'''Qno 4 Reverse a String'''

word = input("Enter a word: ")

for i in range(len(word)-1,-1,-1):
    print(word[i])


'''Qno 5 Multiplication Table'''

n = int(input("Enter your number: "))

for i in range(1,11):
    print(f"{n} x {i} = {n * i}")