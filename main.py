import caesar
import pad

while True:
    """Offers user choices of cipher and encrypting or decrypting"""
    choice = input("Would you like to use a Caesar(1) or One-Time Pad(2)"
                   "cipher?\n")
    if choice == "1":
        choice = input("Would you like to Encrypt(1) or Decrypt(2) text? "
                       "(q to Quit)\n")
        if choice == "q" or choice == "Q":
            break
        if choice == "1":
            caesar.encrypt()
        elif choice == "2":
            caesar.decrypt()
        else:
            print("\nInvalid choice.\n")
    elif choice == "2":
        choice = input("Would you like to Encrypt(1) or Decrypt(2) text? "
                       "(q to Quit)\n")
        if choice == "q" or choice == "Q":
            break
        if choice == "1":
            pad.encrypt()
        elif choice == "2":
            pad.decrypt()
        else:
            print("\nInvalid choice.\n")
    elif choice == "1":
        choice = input("Would you like to Encrypt(1) or Decrypt(2) text?\n"
                       "(Select 1 or 2 or q to Quit)\n")
        if choice == "q" or choice == "Q":
            break
        if choice == "1":
            caesar.encrypt()
        elif choice == "2":
            caesar.decrypt()
        else:
            print("\nInvalid choice.\n")
