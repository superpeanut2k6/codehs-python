numerator = int(input("Enter a numerator: "))

# Use a while loop here to repeatedly ask the user for
# a denominator for as long as the denominator is 0
# (or, put another way, until the denominator is not
# equal to 0).

divides_evenly=False
while(not divides_evenly):
    denominator = int(input("Enter denominator: "))
    divides_evenly=(int(numerator / denominator) * denominator == numerator)
    if divides_evenly:
        print("Divides evenly!")
    else:
        print("Doesn't divide evenly.")