numbers = []
for i in range(1,6):
    number = int(input(f"Enter a number {i}: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[1]}")
print(f"The smallest numbers is {min(numbers)}")
print(f"The largest numbers is {max(numbers)}")
print(f"The average numbers is {sum(numbers) / len(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("Enter your name: ")

if name in usernames:
    print("Access granted")
else:
    print("Access denied")