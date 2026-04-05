# A special decoding problem:

## Problem:
The input will contain only alphabets. If any letters are in lowercase, convert them to uppercase. The final output should always be in all caps. <br/>
        Sample Input:'NCUW' <br/>
'N' was shifted by 1, so original = 'M' <br/>
'C' was shifted by 2, so original = 'A'<br/>
'U' was shifted by 3, so original = 'R' <br/>
'W' was shifted by 4, so original = 'S'<br/>
Sample Output:'MARS'

## input:
A string preferrable in uppercase and no whitespaces.

## output:
A decoded string in understandable format

## Implementation:

- First obtain inputs from the user and clean it by removing white spaces, convert all lower case to upper case letters
- for each character and its index in the input, locate the character in the alaphabets listing.
- once located, backtrack by the index number of characters to locate the original letter used there
- append the character and return the decoded string

## What has been learnt?
- Character indexing.
- Encoding and decoding methods.
