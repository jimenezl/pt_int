"""
This is the file with your answer, do not rename or move it.
Write your code in it, and save it before submitting your answer.
"""

def is_valid_socket_address(address):
    """Determine if the provided string is a valid socket address.
    This function declaration must be kept unmodified.

    Args:
        address: A string with a socket address, eg, 
            '127.12.23.43:5000', to be checked for validity.
    Returns:
        A boolean indicating whether the provided string is a valid 
        socket address.
    """
    # write your implementation here
    return 'not implemented'


# This tests your code with the examples given in the question, 
# and is provided only for your convenience.
if __name__ == '__main__':
    for address in ["127.12.23.43:5000",
                   "127.A:-12"]:
        print is_valid_socket_address(address)


