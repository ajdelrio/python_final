import random


def encrypt():
    """encrypts the text using the one-time pad method and saves the key and text
    locally
    """
    text = askFile().upper()
    key = genKey(len(text))
    new_text = ""
    for i in range(len(text)):
        new_text += shift(text[i], key[i])
    print("\nWriting key as pad_key.txt...")
    f = open("pad_key.txt", "w+")
    f.write(' '.join(str(x) for x in key))
    f.close()
    print("Writing encrypted text as pad_encrypted.txt...\n")
    f = open("pad_encrypted.txt", "w+")
    f.write(new_text)
    f.close()
    return


def decrypt():
    """Decrypts the given text file with the given key file"""
    text = askFile().upper()
    key = getKey().split()
    # One-time pad only works with a key of length => length of the text
    if len(key) < len(text):
        print("Key was too small for this text.")
        return
    new_text = ""
    for i in range(len(text)):
        new_text += shift(text[i], -int(key[i]))
    print(new_text)
    print("\nWriting decrypted text as pad_decrypted.txt...")
    f = open("pad_decrypted.txt", "w+")
    f.write(new_text)
    f.close()
    return


def genKey(length):
    """Generates a key of random integers for shifting"""
    key = []
    for i in range(length):
        key.append(random.randint(1, 25))
    return key


def shift(letter, value):
    """Shifts the given letter the given value, wrapping aroudn the ends"""
    if letter == " ":
        return letter
    elif letter.isalpha() is False:
        return
    else:
        new_ord = ord(letter) + value
        if new_ord in range(65, 91):
            new_char = chr(new_ord)
        elif new_ord > 91:
            new_char = chr(new_ord - 26)
        else:
            new_char = chr(new_ord + 26)
        return new_char


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
            text = getFile()
        if text is None or text == "":
            print("Please enter some text or provide a non-empty file.\n")
            continue
        else:
            break
    return text


def getFile():
    """Gets filename from user, validates it's a .txt, and returns its
    contents"""
    while True:
        filename = input("\nEnter the path to the .txt file you wish to use, "
                         "or c to cancel:\n")
        if filename not in ["c", "C"]:
            while filename[-4:] != ".txt":
                filename = input("\nFile must end in .txt\nPlease enter the "
                                 "path to a .txt file, or c to cancel:\n")
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


def getKey():
    """Gets the key from a .txt file from the user"""
    while True:
        filename = input("Enter the path to the .txt file you wish to use as "
                         "the key, or c to cancel:\n")
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
                key = f.read()
                break
        else:
            return
    f.close()
    return key
