# 1. Write a python script to convert a number into str type.
num = 123
st = str(num)
print(st, type(st))
print()
# 2. Write a python script to print Unicode of the character ‘m’
char = 'm'
print("unicode of", char, "is", ord(char))
print()
# 3. Write a python script to print character representation of a given unicode 100.
num = 100
print("character representation of a given unicode", num, "is", chr(num))
print()
# 4. Write a python script to print any number and its binary equivalent
num1 = 10896
print("binary of", num1, "is", bin(10896))
print()
# 5. Write a python script to print any number and its octal equivalent.
num2 = 8496
print("Octal number of", num2, "is", oct(num2))
print()
# 6. Write a python script to print any number and its hexadecimal equivalent.
num3 = 456789
print("Hexadecimal number of", num3, "is", hex(num3))
print()
# 7. Write a python script to store binary number 1100101 in a variable and print it in decimal format.
binary_num = 0b1100101
print("decimal number of 1100101", "is", int(binary_num))
print()
# 8. Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
hexa = 0x2F
print("octal number of 2F", "is", oct(hexa))
print()
# 9. Write a python script to store an octal number 125 in a variable and print it in binary format.
octa = 0o125
print("Binary number of 125 ", "is", bin(octa))
print()
'''10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format.'''
num1 = 0o25
num2 = 0x39
sum = num1+num2
print("add two numbers 25 (in octal) and 39 (in hexadecimal) and the result in binary format is ", bin(sum))
