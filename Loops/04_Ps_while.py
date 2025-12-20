# # qs1
# num = 1
# while num < 101:
#     print(num)
#     num += 1

# # qs2
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# # qs3
# n = int(input("Enter the numer: "))
# x = 1
# while x <= 10:
#     print(n * x)
#     x += 1

# # qs4
# l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# color = ["red", "blue", "green", "white", "black"]
# idx = 0

# while idx < len(color):
#     print(color[idx])
#     idx += 1

# while idx < len(l):
#     print(l[idx])
#     idx += 1

# # qs5
# num = (1, 22, 33, 9, 54, 14, 67, 69)
# find = 9

# idx = 0
# while idx < len(num):
#     if (num[idx] == find):
#         print("Found at idx:", idx)
#         break
#     else:
#         print("Finding...")
#     idx += 1

# print("Loop Ended")

# # qs6
# i = 1
# while i <= 20:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# i = 1
# while i <= 20:
#     if(i == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# # qs 7
# n = int(input("Enter the number: "))
# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1
# print(sum)

# # qs8

# n = int(input("Enter the number: "))
# fact = 1
# i = 1

# while i <= n:
#     fact *= i
#     i += 1
# print(f"Factorial{fact}")


'''Start'''

n = int(input("Enter the number: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print(sum) 