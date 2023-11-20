# Task 1
out_file = open("name.txt", "w")
user_name = input("Enter your name: ")
print(user_name, file=out_file)
out_file.close()

# Task 2
in_file = open("name.txt", "r")
user_name = in_file.read().strip()
in_file.close()
print(f"Your name is {user_name}")

# Task 3
in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)

# Task 4
in_file = open("numbers.txt", 'r')
all_numbers = in_file.readlines()
total_all = sum(int(number) for number in all_numbers)
print(f"The total for all numbers is: {total_all}")
