#Promt user to enter the number for which they want the multiplication table
number = int(input("Enter the number for which you want the multiplication table: "))

#prompt user to enter the limit up to which the multiplication to be generated
limit = int(input("Enter the limit up to which you want the table generated: "))

print(f"Multiplication table for the number {number} is: ")
for i in range(1, limit + 1):       # 'i' is the limit
     print(f"{number} * {i} = {number * i}")


