# Medium Problem 2 


## Problem Overview
**Morse code Decoder**

Implement a system to convert text into Morse code and/or decode Morse code back into text using standard mappings.

---

## Approach

* Define a mapping between characters and their Morse representations
  * Split Morse input using spacers given / or | or space.
  * Map each code back to its character

---

## Morse Code Representation

* Dot (.) → short signal
* Dash (-) → long signal
---

## Example
Input:

```
.... . .-.. .-.. ---
```

---
Output:

```
HELLO
```

## Assumptions

* Input contains valid characters (A–Z, 0–9)
* Case-insensitive processing
* Standard Morse mappings are used

---

## Limitations

* Does not handle ambiguous or malformed Morse input
* Limited to predefined character set

---

## Conclusion

The implementation provides a simple and efficient way to encode and decode Morse code using dictionary-based mapping.

## Morse Code Table

**A reference table has been given below which can be used to transalate messages**

| Character | Morse Code | Character | Morse Code |
| --------- | ---------- | --------- | ---------- |
| A         | .-         | N         | -.         |
| B         | -...       | O         | ---        |
| C         | -.-.       | P         | .--.       |
| D         | -..        | Q         | --.-       |
| E         | .          | R         | .-.        |
| F         | ..-.       | S         | ...        |
| G         | --.        | T         | -          |
| H         | ....       | U         | ..-        |
| I         | ..         | V         | ...-       |
| J         | .---       | W         | .--        |
| K         | -.-        | X         | -..-       |
| L         | .-..       | Y         | -.--       |
| M         | --         | Z         | --..       |

### Numbers

| Digit | Morse Code |
| ----- | ---------- |
| 0     | -----      |
| 1     | .----      |
| 2     | ..---      |
| 3     | ...--      |
| 4     | ....-      |
| 5     | .....      |
| 6     | -....      |
| 7     | --...      |
| 8     | ---..      |
| 9     | ----.      |

## Spacers:
Since Morse code is non prefixable code or two or more letters may have same prefix the words needs spacers or gaps 
to separate two or more words in a single string of morse code example: '/' or '|' or simple ' '
