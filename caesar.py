def getShift():
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
    old_text = text.upper()
    lyst = old_text.split()
    new_list = []
    for word in lyst:
        new_word = shiftWord(word, shift)
        new_list.append(new_word)
    new_text = " ".join(new_list)
    return new_text


def shiftWord(word, shift):
    new_word = ""
    for i in range(len(word)):
        if word[i].isalpha() is False:
            continue
        if ord(word[i]) + shift in range(65, 91):
            new_word += chr(ord(word[i]) + shift)
        elif ord(word[i]) + shift > 90:
            new_word += chr(ord(word[i]) + shift - 26)
        else:
            new_word += chr(ord(word[i]) + shift + 26)
    return new_word


def encrypt():
    plain_text = input("\nEnter the text to encrypt:\n")
    shift = getShift()
    enc_text = shiftText(plain_text, shift)
    print("\n" + enc_text)
    while True:
        inp = input("\nWould you like to save to file? (y/n)\n")
        if inp not in ["y", "Y", "n", "N"]:
            print("Invalid input.")
            continue
        if inp in ["y", "Y"]:
            f = open("caesarEncrypted.txt", "w+")
            f.write(enc_text)
            f.close()
            break
        if inp in ["n", "N"]:
            break


def decrypt():
    text = input("\nEnter the text to decrypt:\n")
    while True:
        choice = input("Do you know the shift value?(y/n)")
        if choice in ["Y", "y"]:
            shift = getShift()
            break
        elif choice in ["N", "n"]:
            shift = guessShift(text)
            print("I guess the shift value is: " + shift)
            break
        else:
            continue
    dec_text = shiftText(text, shift)
    print("\n" + dec_text)
    while True:
        inp = input("\nWould you like to save to file? (y/n)\n")
        if inp not in ["y", "Y", "n", "N"]:
            print("Invalid input.")
            continue
        if inp in ["y", "Y"]:
            f = open("caesarDecrypted.txt", "w+")
            f.write(dec_text)
            f.close()
            break
        if inp in ["n", "N"]:
            break


def checkGoodness(text, shift):
    total_goodness = 0.0
    old_text = text.split()
    for word in old_text:
        total_goodness += wordGoodness(word, shift)
    return total_goodness


def wordGoodness(word, shift):
    letter_goodness = [
        0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697,
        0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599,
        0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007
        ]
    shift_goodness = 0.0
    new_word = shiftWord(word, -shift)
    for i in range(len(new_word)):
        position = ord(new_word[i]) - 65
        shift_goodness += letter_goodness[position]
    return shift_goodness


def guessShift(text):
    goodness_values = []
    for i in range(27):
        goodness_values.append(checkGoodness(text, i))
    best_guess = goodness_values.index(max(goodness_values))
    return best_guess
