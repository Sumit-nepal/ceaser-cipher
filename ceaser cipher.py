# python program for encryption and decryption using ceaser cipher

# defining the function for welcome message
def welcome():
    print("Welcome to the Ceaser Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")

# defining enter message function to prompt user for message and mode
def enter_message():
    # prompt user for mode
    while True:
        mode = str(input("Would you like to encrypt (e) or decrypt (d): "))

        # prompt user for mode again if user does not inputs correct mode
        if mode != "e" and mode != "d":
            print("Invalid Mode")
        else:
            break
    
    # prompt user to ask where they want to read file
    while True:
        console_or_file = str(input("Would you like to read from a file (f) or the console (c)?"))
        if console_or_file != "f" and console_or_file != "c":
            continue
        else:
            break

    # prompt user for message to encrypt or decrypt according to mode selected by user 
    if mode == "e" and console_or_file == "c":
        while True:
            message = input("What message would you like to encrypt: ").upper() # prompt user for input
            if all(char.isalpha() or char.isspace() for char in message): # check if user input contains any non alphabet
                break  # break the loop if all character is alphabet

    elif mode == "d" and console_or_file == "c":
        while True:
            message = input("What message would you like to decrypt: ").upper() # prompt user for input
            if all(char.isalpha() or char.isspace() for char in message): # check if user input contains any non alphabet
                break  # break the loop if all character is alphabet
    
   
    
    valid = False # set initial value of valid to false
    while not valid:
        try:
            while True:
                shift_number = int (input("What is shift number: "))
                if shift_number > 0 and shift_number <= 25:
                    break
                else:
                    print("Invalid Shift")
            valid = True  # break the loop is shift number is valid
        except ValueError:
            print("Invalid Shift")
    
    # return mode, message and shift number
    return mode, message, shift_number, console_or_file
    
# defining function for encrypting the message
def encrypt(message, shift_number):
    # import string module and define alphabets
    import string
    alphabets = string.ascii_uppercase

    # convert message to list
    message = list(message)

    # iterate through each character
    for i in range (len(message)):
        if message[i] == " ": # if space is found keep it as a space
            message[i] = " "
        else:
            new_index = (alphabets.index(message[i]) + shift_number) % 26 # shift character to right by the given shift number
            message[i] = alphabets[new_index] # append new charcter of shiffted position
    
    encrypted_message ="".join(message)  # join the message in single line
    return encrypted_message

# defining function for decrypting the message
def decrypt(message, shift_number):
    # import string module and define alphabets
    import string
    alphabets = string.ascii_uppercase

    # convert message to list
    message = list(message)

    # iterate through each character
    for i in range (len(message)):
        if message[i] == " ": # if space is found keep it as a space
            message[i] = " "
        else:
            new_index = (alphabets.index(message[i]) - shift_number) % 26 # shift character to left by the given shift number
            message[i] = alphabets[new_index] # append new charcter of shiffted position

    decrypted_message ="".join(message) # join the message in single line
    return decrypted_message

# defining function for reading text from text file
def process_file(filename, mode):
    # prompt user for shift number
    valid = False # set initial value of valid to false
    while not valid:
        try:
            while True:
                shift_number = int (input("What is shift number: "))
                if shift_number > 0 and shift_number <= 25:
                    break
                else:
                    print("Invalid Shift")
            valid = True  # break the loop is shift number is valid
        except ValueError:
            print("Invalid Shift")

    with open(filename,"r") as file:  # open text file as file
        message = file.readlines()  # read lines from the file and store in message

    if mode == "e":
        encrypted_message = "" # initialize encrypted message

        # iterate through each line in message    
        for line in message:
            line = line.upper() 

            # iterate through each character in the line
            for char in line:
                 # if character is alphabet encrypt it by calling encrypt function
                if char.isalpha():
                    encrypted_character = encrypt(char, shift_number)
                    encrypted_message += encrypted_character # add encrypted character in encrypted message
                else:
                    # if character is non alphabet add as it is
                    encrypted_message += char
        return encrypted_message
    
    # decrypt the text file if decrypt mode is selected
    else:
        decrypted_message = "" # initialize decrypted message

        # iterate through each line in message    
        for line in message:
            line = line.upper() 

            # iterate through each character in the line
            for char in line:
                 # if character is alphabet encrypt it by calling decrypt function
                if char.isalpha():
                    decrypted_character = decrypt(char, shift_number)
                    decrypted_message += decrypted_character # add decrypted character in decrypted message
                else:
                    # if character is non alphabet add as it is
                    decrypted_message += char
        return decrypted_message
encrypted = process_file("message.txt","d")
print(encrypted)

# defining function to check file existence
def is_file(filename):
    File_found = True # initialize file found as True
    try:
        with open(filename,"r"):
            File_found = File_found  # if file is found retrun true

    except FileNotFoundError:
        File_found = not File_found  # return false if file not found

    # return File_found
    return File_found   

# defining function to write strings in text file
def write_message(string_list):

    # open result text file in write mode
    with open("result.txt","w") as file:
          for line in string_list:  # iterate through each line
              file.write(line)  # write the line in result text file

# defining function to prompt console or file 
def message_or_file():
    while True:
        mode = str(input("Would you like to encrypt (e) or decrypt (d): "))

        # prompt user for mode again if user does not inputs correct mode
        if mode != "e" and mode != "d":
            print("Invalid Mode")
        else:
            break
    
    # prompt user to ask where they want to read the file from console or not
    while True:
        console_or_none = str(input("Would you like to read from the console (c) or (not)?"))
        if console_or_none != "f" and console_or_none != "c": # check if the mode is valid
            # if not prompt again for input
            console_or_none = str(input("Would you like to read from the console (c) or (not)?"))
        else:
            break  # break the loop if mode is valid

    # return console or none according to user input
    if console_or_none == "c":
        return console_or_none
    else:
        return None
    

# define main function 
def main():
    # call the welcome function
    welcome()
    while True:
         # call the enter_message function and store its returned value
        mode, message, shift_number, console_or_file= enter_message()

    # if mode is e call encrypt function and pass the arguments
        if mode == "e":
            encrypted_message= encrypt(message, shift_number)
            if console_or_file == "c":  # if user input is console print encrypted message in cosole
                print(encrypted_message)
            else:
                break
        else:  # else call the decrypted function and pass the argument
            decrypted_message = decrypt(message, shift_number)
            if console_or_file == "c":  # if user input is console print decrypted message in console
                print(decrypted_message)
            else:
               break
        
     
        while True:
            # ask user if they want to encrypt or decrypt another message
            user = str(input("Would you like to encrypt or decrypt another message? (y/n): "))
            if user == "y" or user == "n":  # check if user input is valid
                break
            else:  # if user input is not valid prompt again for input
                user = str(input("Would you like to encrypt or decrypt another message? (y/n): "))
        
        if user == "n":  # terminate the program if user input is n
            print("Thanks for using the program, goodbye!")
            break 

# call the main function
# main()
