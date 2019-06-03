def getShift():
    """Gets the shift value from the user and validates it"""
    while True:
        try:
            shift = int(input(
                "\nEnter the shift value(integer between -26 and 26): "
                    ))
            if shift not in range(-26, 27):
                continue
            else:
                break
        except ValueError:
            print("Enter an integer between -26 and 26.")
    return shift


def shiftText(text, shift):
    """Shifts each word in the provided text and returns the result
    """
    old_text = text.upper()
    lyst = old_text.split()
    new_list = []
    for word in lyst:
        new_word = shiftWord(word, shift)
        new_list.append(new_word)
    new_text = " ".join(new_list)
    return new_text


def shiftWord(word, shift):
    """Shifts each alphabetical character the desired value, wraps text from z
    to a as well
    """
    new_word = ""
    for i in range(len(word)):
        if word[i].isalpha() is False:
            continue
        if ord(word[i]) + shift in range(65, 91):
            new_word += chr(ord(word[i]) + shift)
        elif ord(word[i]) + shift > 91:
            new_word += chr(ord(word[i]) + shift - 26)
        else:
            new_word += chr(ord(word[i]) + shift + 26)
    return new_word


def fileInp():
    """Takes input text from a user supplied .txt file, returns text from file
    """
    text = ""
    while True:
        filename = input("Enter the path to the .txt file you wish to use, or "
                         "c to cancel:\n")
        if filename not in ["c", "C"]:
            while filename[-4:] != ".txt":
                filename = input("File must end in .txt\nPlease enter the path"
                                 "to a .txt file, or c to cancel:\n")
                if filename in ["c", "C"]:
                    return
                else:
                    continue
            try:
                f = open(filename, "r")
            except FileNotFoundError:
                print("Wrong file or file path.")
            else:
                text = f.read()
                break
        else:
            return
    f.close()
    return text


def askFile():
    """Asks user if they want to manually or from a file, then takes the input
    or passes control to fileInp()"""
    while True:
        choice = input(
            "Would you like to enter the text manually(1) or from a .txt "
            "file(2)?\n")
        if choice == "1":
            text = input("\nEnter your text:\n")
        elif choice == "2":
            text = fileInp()
        if text is None or text == "":
            print("Please enter some text or provide a non-empty file.\n")
            continue
        else:
            break
    return text


def encrypt():
    """Encrypts the text with a caesar cipher of user input shift value"""
    text = askFile()
    shift = getShift()
    enc_text = shiftText(text, shift)
    print("\nHere is your encrypted text:\n\n" + enc_text)
    # Allows user to save the text to a file locally called caesarEncrypted.txt
    while True:
        inp = input("\nWould you like to save to file? (y/n)\n")
        if inp not in ["y", "Y", "n", "N"]:
            print("Invalid input.")
            continue
        if inp in ["y", "Y"]:
            print("Writing encrypted text to caesarEncrypted.txt...")
            f = open("caesarEncrypted.txt", "w+")
            f.write(enc_text)
            f.close()
            break
        if inp in ["n", "N"]:
            break


def decrypt():
    """Decrypts input text with a given cipher value or passes to guessShift
    to attempt to guess the shift value"""
    text = askFile()
    while True:
        choice = input("Do you know the shift value?(y/n)\n")
        if choice in ["Y", "y"]:
            shift = getShift()
            break
        elif choice in ["N", "n"]:
            shift = guessShift(text)
            print("I guess the shift value is: ", shift)
            break
        else:
            continue
    dec_text = shiftText(text, -shift)
    print("\nHere is your decrypted text:\n\n" + dec_text)
    # Allows user to save text in a file locally named caesarDecrypted.txt
    while True:
        inp = input("\nWould you like to save to file? (y/n)\n")
        if inp not in ["y", "Y", "n", "N"]:
            print("Invalid input.")
            continue
        if inp in ["y", "Y"]:
            print("Writing decrypted text to caesarDecrypted.txt...")
            f = open("caesarDecrypted.txt", "w+")
            f.write(dec_text)
            f.close()
            break
        if inp in ["n", "N"]:
            break


def checkGoodness(text, shift):
    """Returns sum of letter frequency values from each word in the text"""
    total_goodness = 0.0
    old_text = text.split()
    for word in old_text:
        total_goodness += wordGoodness(word, shift)
    return total_goodness


def wordGoodness(word, shift):
    """Evaluates the goodness value of a word from the letter frequency value
    in English"""
    letter_goodness = [
        0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697,
        0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599,
        0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007
        ]
    shift_goodness = 0.0
    word = word.upper()
    new_word = shiftWord(word, -shift)
    for i in range(len(new_word)):
        position = ord(new_word[i]) - 65
        shift_goodness += letter_goodness[position]
    return shift_goodness


def guessShift(text):
    """Compares the goodness values of the text for each possible shift value
    and returns the shift value with the highest likelihood according to
    letter frequency"""
    goodness_values = []
    for i in range(26):
        goodness_values.append(checkGoodness(text, i))
    best_guess = goodness_values.index(max(goodness_values))
    return best_guess
