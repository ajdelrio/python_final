import caesar


while True:
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
