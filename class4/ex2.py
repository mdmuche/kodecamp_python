# create a program that converts units (e.g kilometers to miles, celcius to fehrenheit) based on user input

# Algorithm

# display section for conversion(vol, mass, temp)
# display appropriate available conversion for each section
# get the value to be converted
# carry out the conversion
# display the message

print("choose from the section below:")
print("1. length")
print("2. mass")
print("3. temperature")
print()
option = int(input("enter an option: "))

if option == 1:
    print()
    print("below is the available conversions for length:")
    print("1. inches to centimeters")
    print("2. millimeters to inches")
    print()
    length_option = int(input("enter your length option: "))

    if length_option == 1:
        inches_value = int(input("enter your inches value: "))
        #  1 inch = 2.540 centimeters
        centimeters_value = 2.540 * inches_value
        print("value in centimeters is " + centimeters_value)
    elif length_option == 2:
        milli_value = int(input("enter your millimeters value: "))
        #  1 millimeter = 0.03937 inches
        inches_value = 2.540 * milli_value
        print("value in centimeters is " + inches_value)

elif option == 2:
    print()
    print("below is the available conversions for mass:")
    print("1. kilograms to pounds")
    print("2. grams to ounces")
    print()
    mass_option = int(input("enter your mass option: "))

elif option == 3:
    print()
    print("below is the available conversions for temperature:")
    print("1. fehrenheit to celcius")
    print("2. celcius to fehrenheit")
    print()
    temp_option = int(input("enter your temperature option: "))

else:
    print("you have selected an invalid option")