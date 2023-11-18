"""
Part A
Pseudocode
for i in range(0, 110, 10)
    display i (side by side)
end for
"""
# for i in range(0, 110, 10):
#     print(i, end=' ')
# print()

"""
Part B
Pseudocode
for i in range(20, 0, -1)
    display i (side by side)
end for
"""
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

"""
Part C
Pseudocode
get number of star
for i in range(0, number_of_star, 1):
    print the number of "*" according top the user
print()
"""
# number_of_star = int(input("Number of stars: "))
# for i in range(0, number_of_star, 1):
#     print("*", end='')
# print()

"""
Part D
Pseudocode
get number of star
for i in range(1, number_of_star + 1)
    print lines of increasing stars by 1
print()
"""
number_of_star = int(input("Number of stars: "))
for i in range(1, number_of_star + 1):
    print("*" * i)
print()
