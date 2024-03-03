age = int(input( "what is your age ?: "))
status = str(input("Are you a student? (Yes/No): "))

if age <= 12:
    print("You are eligible for a discount on the movie ticket.")

elif (13 <= age <= 18) and status == "Yes":
    print("You are eligible for a discount on the movie ticket.")

else:
    print("You are not eligible for a discount on the movie ticket.")