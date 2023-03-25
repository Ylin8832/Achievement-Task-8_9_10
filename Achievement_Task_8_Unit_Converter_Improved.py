# Name:                     Task 8: Unit Converter-Improved
# Author:                   Yunfeng Lin (Ylin8832)
# Date Created:             March 21, 2023
# Date Last Modified:       March 22, 2023

'''
Improvement 1: Defined a wlcomeMessage function and return the welcome message to the function when calling it in string format.
Improvement 2: Used "try/except" block to handle any exceptions that will be potentially thrown by invalid user inputs. 
Improvement 3: Applied while loop in case any of the values provided is invalid, will keep asking the user to enter a valid value.
Improvement 4: In the speed conversion section, added negative number checking in the loop, so that the program will keep asking 
               the user to enter a value that is greater than 0.
'''

def welcomeMessage():
    message = "Welcome to Unit Converter Program".upper()
    return message
print("\n{0:-^64s}".format(welcomeMessage()), "\n\n{0:^40s}{1:s}".format("1. Temperature","2. Speed"))

while True:
    try:
        conversion = int(input("\nPlease Enter [1] For temperature conversion, [2] for speed conversion: "))    
    except ValueError as valErr:
        print(valErr)
    else:
        if conversion < 1 or conversion > 2:
            print("Invalid number! Please enter number 1 or 2.")
        elif conversion == 1 or conversion == 2:
            break
            
def tempConver(number1): # Define a function called [tempConver] that accepts on parameter called [number1].
    
    if number1 == 1:
        while True: # Loop to keep asking the user to enter a valid value until they do.
            try:
                temperature = float(input("Enter the temperature: ").strip()) # Ask the user to enter the temperature (number) they want to convert. Remove whitespace.
            except ValueError as tempErr:
                print(tempErr)
            else:
                break
        while True: # Loop to keep asking the user to enter a valid value until they do.
            tempU_errMessage = "Invalid input!"
            tempUnit = input("Enter the current temperature unit C(Celsius) or F(Fahrenheit): ") # Ask the user to enter the current unit used for the temperature.
            if not (tempUnit.strip().upper() == "C" or tempUnit.strip().upper() == "F"):
                print(tempU_errMessage)
            elif tempUnit.strip().upper() == "C": # remove whitespace and ignore letter-case differences "C", "c".
                print("{0:.1f}°C = {1:.1f}°F".format(temperature , temperature * 9/5 + 32)) # Display result using substitution (format() method) for the output.
                break
            elif tempUnit.strip().upper() == "F": # remove whitespace and ignore letter-case differences "F", "f".
                print("{0:.1f}°F = {1:.1f}°C".format(temperature , (temperature - 32) * 5/9))
                break

def speedConver(number2): # Define a function called [speedConver] that accepts on parameter called [number2].

    if number2 == 2:
        while True: # Loop it to keep asking the user to enter a valid value until they do.
            try:
                speed = float(input("Enter the speed: ").strip())
            except ValueError as speedErr:
                print(speedErr)
            if speed < 0:
                print("Speed can't be negative, try again.")
            else:
                break
        while True: # Loop it to keep asking the user to enter a valid value until they do.
            speedU_errMessage = "Invalid input!"
            speedUnit = input("Enter the current speed unit KMH(Kilometer per hour) or MPH(Miles per hour): ") # Ask the user to enter the current unit used for the speed.
            if not (speedUnit.strip().upper() == "KMH" or speedUnit.strip().upper() == "MPH"):
                print(speedU_errMessage)
            elif speedUnit.strip().upper() == "KMH": # remove whitespace and ignore letter-case differences "KMH", "kmh".
                print("{0:.2f}k/h = {1:.2f}m/h".format(speed , speed/1.609)) # Display result using substitution (format() method) for the output.
                break
            elif speedUnit.strip().upper() == "MPH": # remove whitespace and ignore letter-case differences "MPH", "mph".
                print("{0:.2f}m/h = {1:.2f}k/h".format(speed , speed * 1.609))
                break

tempConver(conversion) # call to the function and pass the input data (argument) for the function to execute the temperature conversion. 
speedConver(conversion) # Call to the function and pass the input data (argument) for the function to execute the speed conversion. 