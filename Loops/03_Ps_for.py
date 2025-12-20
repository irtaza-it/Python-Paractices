# #  qs1
# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for el in num:
#     print(el)


# # qs2
# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = 16
# idx = 0

# for el in num:
#     if(el == x):
#         print("Number Found! at", idx)
#     idx += 1

# # qs3
# for num in range(1, 101):
#     print(num)

# # qs4
# for num in range(100, 0, -1):
#     print(num)

# # qs5
# n = int(input('Enter the number: '))
# i = 1
# for x in range(1, 11):
#     print(f"{n} x {i} = {n * i}")
#     i += 1

# # qs6
# n = int(input("Enter the number: "))
# sum = 0

# for i in range(1, n+1):
#     sum += i
# print(f"Total sum of {sum}")

# # qs7
# n = int(input("Enter the number: "))
# factorial = 1

# for i in range(1, n+1):
#     factorial *= i
# print("Factorial = ", factorial)


'''Start'''

# for i in range(1,11):
#     print(i)


# for n in range(2,51,2):
#     print(n)

# n = int(input("Enter number: "))
# total = 0

# for i in range(1, n+1):
#     total += i

# print(total)


# num = int(input("Enter number: "))

# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")


# for i in range(10,0,-1):
#     print(i)


# for i in range(1,6):
#     print("*"* i)

# count = 0
# for i in range(1,51):
#     if i % 5 == 0:
#         count += 1

# print(count)


# count = 0

# for f in range(1, 101):
#     if f % 10 == 0:
#         count += 1
# print(count)


# count = 0
# for i  in range(1,31):
#     if i % 3 == 0:
#         count += 1
# print(count)


count = 0
for i in range(1,51):
    if i % 2 == 0:
        count += 1

print(count)

