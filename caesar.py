

def encrypt():
    plain_text = input("\nEnter the text to encrypt:\n")
    while True:
        try:
            shift = int(input("\nEnter a shift value between -26 and 26: "))
            if shift not in range(-26, 27):
                continue
            else:
                break
        except ValueError:
            print("Enter an integer.")

    plain_text = plain_text.upper()
    lyst = plain_text.split()
    cipher_list = []
    for word in lyst:
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
        cipher_list.append(new_word)
    cipher_text = " ".join(cipher_list)

    print(cipher_text)
    while True:
        inp = input("\nWould you like to save to file? (y/n)\n")
        if inp not in ["y", "Y", "n", "N"]:
            print("Invalid input.")
            continue
        if inp == "y" or inp == "Y":
            f = open("caesarEncrypt.txt", "w+")
            f.write(cipher_text)
            f.close()
            break
        if inp == "n" or inp == "N":
            break


def decrypt():
    coded_text = input("\nEnter the text to decrypt:\n")

    while True:
        try:
            shift = int(input("\nEnter the shift value to use: "))
            break
        except ValueError:
            print("Enter an integer.")

    coded_text = coded_text.upper()
    lyst = coded_text.split()
    plain_list = []
    for word in lyst:
        new_word = ""
        for i in range(len(word)):
            if word[i].isalpha() is False:
                continue
            if ord(word[i]) - shift in range(65, 91):
                new_word += chr(ord(word[i]) - shift)
            elif ord(word[i]) - shift < 65:
                new_word += chr(ord(word[i]) - shift + 26)
            else:
                new_word += chr(ord(word[i]) - shift - 26)
        plain_list.append(new_word)
    plain_text = " ".join(plain_list)

    print("\n" + plain_text)
    while True:
        inp = input("\nWould you like to save to file? (y/n)\n")
        if inp not in ["y", "Y", "n", "N"]:
            print("Invalid input.")
            continue
        if inp == "y" or inp == "Y":
            f = open("caesarDecrypt.txt", "w+")
            f.write(plain_text)
            f.close()
            break
        if inp == "n" or inp == "N":
            break
