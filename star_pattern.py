#Prompt user to enterthe height of the triangle made by the stars
height = int(input("Enter the height of the triangle (number of rows): "))

for i in range(1, height + 1): # 'i' is the height 
        print('*' * i)