name = str(input('Your name:'))
x = '''1.Addition 
2.Subtraction
3.Multiplication
4.Division'''
print(x)
choose = (input('choose 1 to 4:'))

if choose == '1':
    a = float(input('a:'))
    b = float(input('b:'))
    sum = a + b
    print(f"sum = {sum}")

elif choose == '2':
    a = float(input('a:'))
    b = float(input('b:'))
    difference = a - b
    print(f"difference = {difference}")

elif choose == '3':
    a = float(input('a:'))
    b = float(input('b:'))
    product = a * b
    print(f"product = {product}")

elif choose == '4':
    a = float(input('a:'))
    b = float(input('b:'))
    dividant = a / b
    print(f"dividant = {dividant}")

else:
    print("Sorry!! Invalid option selected for the missing value choice.Try again")