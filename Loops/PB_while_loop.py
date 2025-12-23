'''Qno 1'''

num = 10

while num <= 15:
    print(num)
    num += 1


'''Qno 2'''

num = int(input("Enter a number: "))

while num <= 5:
    print(num ** 3, end=" ")
    num += 1


'''Qno 3'''

num = 1

while num <= 10:
    if num % 2 != 0:
        print(num, end=" ")
    num += 1


'''Qno 4'''

num = 1
product = 1

while num <= 5:
    product *= num
    num += 1
print(product)

'''Qno 5'''

sentence = input("Enter a word: ")
words = sentence.split()

for word in words:
    i = len(word) -1
    while i >= 0:
        print(word[i], end="")
        i -= 1
    print(end=" ")

'''Qno 6'''

word = input("Enter a word: ").lower()
vowels = "aeiou"
count = 0
index = 0

while index < len(word):
    if word[index] not in vowels and word[index].isalpha():
        count += 1
    index += 1
print(count)



num = 1 

while num <= 100:
    print(num)
    num += 1