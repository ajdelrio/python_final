# Encrypter and Decrypter
Final Project for Python Class

This program will implement a Caesar or one-time pad cipher to the provided text.
It will decrypt a Caesar cipher with a given shift value or guess the shift value and decrypt the text using that.
It will also decrypt one-time pad encrypted text, however, only with the correct key.  This is due to the way the one-time pad encryption works, explained in brief below, making it hypothetically immune to brute-force attacks.

## Using
The user will be prompted with a choice of ciphers, between Caesar and One-Time Pad, and then between encrypting or decrypting.  Once the user is done with encrypting or decrypting, the user will be allowed to continue encrypting or decrypting text with a cipher of their choice.

### Caesar
A Caesar cipher is also known as a shift cipher, it shifts all positions in the alphabet of a text by a given amount.  This is a simple cipher and is not recommended for any real use.  This is demonstrated by the simple brute force method included to try to guess the cipher and decode the text without being given it, discussed more below.

The user will be prompted to either encrypt or decrypt text, once the option is chosen the user is prompted to enter the text manually or from a local .txt file, after which the user is prompted to enter the shift value they desire to use (when encrypting), or the shift value that was used to encrypt (when decrypting).

After encrypting or decrypting, the user is offered to save the files locally.

#### Shift value unknown
If the shift value is not known, the program will attempt to guess what the value is.  It accomplishes this by iterating through each possible shift value, during which it calculates and accumulates the "goodness"  of each word, then compares the "goodness" of each shift value, choosing the "best" guess.

"Goodness" here is a measure of how common a letter appears in the English language, using a list of frequency values for each letter respectively.

This method is, of course, not perfect.  It requires the user to be using normal English words and works poorly for short messages.  It does increase it's accuracy the longer a message is, as the more words it has, the closer to the average letter frequency it should become.

There is input validation for the prompts, so it should not be possible to feed the program incorrect inputs.

The encrypted/decrypted text will be displayed and the user will be asked if they would like to save the result locally.


## One-Time Pad
### This method will write files without prompting the user to do so
### These include pad_encrypted.txt, pad_decrypted.txt, and pad_key.txt
One-Time Pad encryption is similar to a Caesar cipher in that it shifts the characters of it's text, but it shifts each character by a different value, which is defined by the key.  This is why the key must be of at least equal length as the character count in the text being encrypted.

Normally for one-time pad, the key is a list of characters, however, for this program, the key is a randomly generated list of integers from 1 to 25, to represent each possible shift value excluding those that would result in the same character.

Because of the reliance and restrictions on the key, this method will automatically write the encrypted text and key to .txt files when encrypting and the decrypted text when decrypting text.

The key MUST be written in the form of integers between 1 and 25 and delimited with whitespace, so it is recommended to use the one-time pad encryption to write the key file.
