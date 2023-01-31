def cels_to_fahr(cels):
    fahr = (1.8 * cels) + 32
    return fahr
    
    
def fahr_to_cels(fahr):
    cels = (fahr - 32) /1.8
    return cels

try:
    celsius = float(input("Enter a temperature in celsius and I will comvert it into fahrenheit for you: "))
    converted = cels_to_fahr(celsius)
    print(str(celsius) + "C is equal to " + str(converted) + "F")
except ValueError:
    print("That was not a working decimal number")
    
    
try:
    fahrenheit = float(input("Enter a temperature in celsius and I will comvert it into celsius for you: "))
    converted = cels_to_fahr(fahrenheit)
    print(str(fahrenheit) + "C is equal to " + str(converted) + "F")
except ValueError:
    print("That was not a working decimal number")