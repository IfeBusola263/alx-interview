#!/usr/bin/python3
"""
This is a UTF-8 encoding validator
Using specific criteria to validate like:
- invalid bytes
- an unexpected continuation byte
- a non-continuation byte before the end of the character
- the string ending before the end of the character
 (which can happen in simple string truncation)
- an overlong encoding
- a sequence that decodes to an invalid code point
"""


def validUTF8(data):
    """
    This function tests for a valid UTF-8 sequence.
    """
    # Step 1: Iterate through the data
    i = 0
    while i < len(data):
        # Step 2: Check the number of bytes for the current character
        num_bytes = 0
        leading_byte = data[i]

        # Check the number of set bits in the leading byte
        # to determine the number of bytes
        while leading_byte & (0b10000000 >> num_bytes):
            num_bytes += 1

        # Step 3: Check if the number of bytes matches the expected count
        if num_bytes == 1 or num_bytes > 4 or i + num_bytes > len(data):
            return False

        # Step 4: Check if the following bytes are valid continuation bytes
        for j in range(1, num_bytes):
            if (data[i + j] & 0b11000000) != 0b10000000:
                return False

        # Step 5: Move to the next character
        i += 1

    # Step 6: All characters are valid
    return True
