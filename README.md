# Caesar Cipher and Decrypter
Final Project for Python Class

This program will implement a caesar, or shift, cipher to text input by the user, and will do the opposite to decrypt the text when provided the shift value.

## Using
The user will be prompted to either encrypt or decrypt text, once the option is chosen the user is prompted to enter the text, after which the user is then prompted to enter the shift value desired to use (when encrypting), or the shift value that was used to encrypt (when decrypting).

There is input validation for the prompts, so it should not be possible to feed the program incorrect inputs.

The encrypted/decrypted text will be displayed and the user will be asked if they would like to save the result locally.

## Future
### Shift value unknown when decrypting
Next iteration will have the ability to have the program attempt to guess the shift value, when it is not known for encrypted text, through brute force, comparing all 26 shift values and ranking them based on "letter goodness" values, giving the user the best guess it has available.

### Read from file
Next iteration will have the ability to read the text from a text file rather than require the user to input text manually. This will make it much easier for large amounts of text.

#### Improved formatting
Code will be more properly modularized in accordance to style guides (sorry!)

#### One-Time Pad
One-time pad will be implemented as a more robust option for encryption that cannot, to my knowledge, be brute-forced.
