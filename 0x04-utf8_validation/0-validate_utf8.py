#!/usr/bin/python3
"""
- Description: UTF-8 Validation
- method that determines if a given data set represents a valid UTF-8 encoding.
- Prototype: def validUTF8(data)
- Return: True if data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle
        the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes in the UTF-8
        encoded data.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    expected_following_bytes = 0
    leading_bit_mask = 1 << 7
    following_bit_mask = 1 << 6

    for byte in data:
        leading_bit = 1 << 7

        if expected_following_bytes == 0:
            """
            Determine the number of expected following bytes for the current
            character
            """
            while leading_bit & byte:
                expected_following_bytes += 1
                leading_bit = leading_bit >> 1

            # Handle single-byte characters (ASCII)
            if expected_following_bytes == 0:
                continue

            # Invalid number of following bytes
            if expected_following_bytes == 1 or expected_following_bytes > 4:
                return False
        else:
            # Verify that the current byte is a following byte
            if not (byte & leading_bit_mask and not
                    (byte & following_bit_mask)):
                return False

        expected_following_bytes -= 1

    # Check if all expected following bytes have been consumed
    return expected_following_bytes == 0
