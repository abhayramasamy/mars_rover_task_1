#A special encoding decoding problem
"""
MEDIUM PROBLEM CHALLENGE 3:
The input will contain only alphabets. If any letters are in lowercase, convert them to uppercase. 
The final output should always be in all caps.
EXAMPLE
Sample Input:'NCUW'
'N' was shifted by 1, so original = 'M'
'C' was shifted by 2, so original = 'A'
'U' was shifted by 3, so original = 'R'
'W' was shifted by 4, so original = 'S'
Sample Output:'MARS'
"""

#a function to decode the given message
def decode(s: str):
    decoded = ''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i, char in enumerate(s):
        decoded += letters[letters.index(char) - i-1] #shift the letter back by its position in the string
    return decoded 
s = input("Enter the encoded message: ").upper().replace(" ", "").strip()
print("Decoded message:", decode(s))