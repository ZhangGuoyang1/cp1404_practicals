FILENAME = "name.txt"
name = input("Enter name: ")
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file.close()



FILENAME = "name.txt"
in_file = open(FILENAME)
text = in_file.read()
print("Your names is " + "" + text)
in_file.close()


total = 0
FILENAME = "name.txt"
in_file = open(FILENAME, "r")
for i in range(0,2):
    number = in_file.readline()
    total = total + int(number)
print(total)
in_file.close()



total = 0
FILENAME = "name.txt"
in_file = open(FILENAME)
numbers = in_file.readline()
for number in numbers:
    total += int(number)
print(total)
in_file.close()




