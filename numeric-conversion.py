
# defines a function which prints the menu
def menu():
    print("\nDecoding Menu\n"
          "-------------\n"
          "1. Decode hexadecimal\n"
          "2. Decode binary\n"
          "3. Convert binary to hexadecimal\n"
          "4. Quit\n")

# defines a function to convert the hex characters in their numerical values
def hex_char_decode(digit):

    if digit == 'A' or digit == 'a':
        value = 10

    elif digit == 'B' or digit == 'b':
        value = 11

    elif digit == 'C' or digit == 'c':
        value = 12

    elif digit == 'D' or digit == 'd':
        value = 13

    elif digit == 'E' or digit == 'e':
        value = 14

    elif digit == 'F' or digit == 'f':
        value = 15

    # if a numerical value bellow 10 is inserted then it will keep its value
    else:
        value = digit

    return value

# defines a function that decodes a hex into a decimal
def hex_string_decode(hex):

    # sets up variables used for conversion
    hex_convert = 0
    expo_val = 0

    # iterates through every character in the string but in reverse
    for i in reversed(hex):

        # if 0x is used at the beginning of the hex and the loop will be broken out of so these values are not counted
        if i == 'x':
            break

        # numerically converts the character into a hex value
        hex_convert += 16 ** expo_val * int(hex_char_decode(i))
        expo_val += 1

    return hex_convert

# defines a function that converts a binary into a decimal
def binary_string_decode(binary):

    # sets up variables used for conversion
    bin_convert = 0
    expo_val = 0

    # iterates through every character in the string but in reverse
    for i in reversed(binary):

        # if 0b is used at the beginning of the binary the loop will be broken out of so these values are not counted
        if i == 'b':
            break

        # numerically converts the character into a hex value
        bin_convert += 2 ** expo_val * int(i)
        expo_val += 1

    return bin_convert

# defines a function to convert a binary to hex
def binary_to_hex(binary):

    # sets a variable equal to the integer decimal value returned from the function binary_string_decode
    new_bin = int(binary_string_decode(binary))
    conversion = ''

    # if the value received from the decoded binary is 0 print 0 for hex value
    if new_bin == 0:
        print(new_bin)

    # iterates while variable value is greater than 0
    while new_bin > 0:

        # gets the remainder of new_bin when divided by 16 and assigns it to hex_value
        hex_value = new_bin % 16

        # the following if statements take the value and revert it to its corresponding hex character

        if hex_value == 10:
            hex_value = 'A'

        elif hex_value == 11:
            hex_value = 'B'

        elif hex_value == 12:
            hex_value = 'C'

        elif hex_value == 13:
            hex_value = 'D'

        elif hex_value == 14:
            hex_value = 'E'

        elif hex_value == 15:
            hex_value = 'F'

        # stores hex-value in reverse order to output the hex
        conversion = str(hex_value) + conversion

        # before the loop iterates again new_bin is set equal to the result of the division
        new_bin = new_bin // 16

    return conversion

# sets the loops variable to true
start = True

if __name__ == '__main__':

    # loops until start is equal to false
    while start == True:

        # calls menu function to print menu
        menu()
        # prompts the user for an integer input and saves that value in user_choice
        user_choice = int(input("Please enter an option:"))

        # runs if user_choice is between the numbers 0 and 4 exclusive
        if 0 < user_choice < 4:

            # prompts the user for the string the want to convert only for menu options 1-3
            convert_num = input("Please enter the numeric string to convert:")

            # if user-choice is equal to 1 then function to decode hex is called and result is printed
            if user_choice == 1:

                print(f"Result: {hex_string_decode(convert_num)}")

            # if user-choice is equal to 2 then function to decode binary is called and result is printed
            elif user_choice == 2:

                print(f"Result: {binary_string_decode(convert_num)}")

            # if user-choice is equal to 3 then function to convert a binary to hex is called and result is printed
            else:

                print(f"Result: {binary_to_hex(convert_num)}")

        # user option is equal to 4 and the user quits the program
        else:
            print("\nGoodbye!")

            # start is equal to false so the loop is broken out of
            start = False