magic_number = 3.3312
guess = 0

while(magic_number != guess):
    guess = round(float(input("Enter a number: ")), 2)
    if(guess < round(magic_number, 2)):
        print("Too low!")
    elif(guess > round(magic_number, 2)):
        print("Too high!")
    else:
        print("Correct!")
        break;