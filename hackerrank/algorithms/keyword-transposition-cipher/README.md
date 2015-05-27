Keyword Transposition Cipher
============================

A keyword transposition cipher is a method of choosing a monoalphabetic substitution with which to encode a message. The substitution alphabet is determined by choosing a keyword, arranging the remaining letters of the alphabet in columns below the letters of the keyword, and then reading back the columns in the alphabetical order of the letters of the keyword.

For instance, if one chose the keyword <code>SECRET</code>, the columns generated would look like the following diagram. Note how the letters in the keyword are skipped when laying out the columns, and duplicate letters are removed from the keyword:

    SECRT
    ABDFG
    HIJKL
    MNOPQ
    UVWXY
    Z

Since the alphabetical order of the characters in the keyword is <code>CERST</code>, the columns are then read back in that order to get the substitution alphabet.

    Original:     ABCDE FGHIJ KLMNO PQRSTU VWXYZ
    Substitution: CDJOW EBINV RFKPX SAHMUZ TGLQY

### Task:

Given a piece of ciphertext and the keyword used to encipher it with the keyword transposition cipher described above, write an algorithm to output the original message.

### Input:

The first line of input will be an integer *N* indicating the number of test cases that will follow. For each test case in *N*, two additional lines will follow, one containing the keyword, and one containing the ciphertext. The keyword will be at most 7 characters long, and the ciphertext will be at most 255 characters in length.

### Output:

Your output should be the decoded version of the cipher text for each test case, one per line.

### Sample Input:

    2
    SPORT
    LDXTW KXDTL NBSFX BFOII LNBHG ODDWN BWK
    SECRET
    JHQSU XFXBQ

### Sample Output:

    ILOVE SOLVI NGPRO GRAMM INGCH ALLEN GES
    CRYPT OLOGY
