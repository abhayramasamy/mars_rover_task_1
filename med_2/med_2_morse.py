"""
MEDIUM PROBLEM NO 2:

The Morse code message will consist of dots (.) and dashes (-) representing letters, 
with spaces separating individual Morse code characters. 
The function should return the decoded English text.
"""


msg=str(input("Enter the Morse code message: "))
spacer = input("Enter the spacer used in the Morse code message (default is space): ")  #spacer can be| / or space
if not spacer:    spacer = ' '
#recieve the coded input from the user
#morse code mapping for letters A-Z
morse_map = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
def morse_code_reader(msg, spacer=' '):  
    words = msg.split(spacer)    #split based on the spacer issued
    decoded_msg = ''
    for word in words:           #for every word in the message, check if it exists in the morse map and decode it
        if word in morse_map.values():
            decoded_msg += list(morse_map.keys())[list(morse_map.values()).index(word)]
        else:
            decoded_msg += '?'
    return decoded_msg 
print("Decoded Morse code message:", morse_code_reader(msg))