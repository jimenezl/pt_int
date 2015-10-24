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
    
    split_subnets = address.split(".")
    if len(split_subnets) != 4:
        return False

    split_port = split_subnets[3].split(":")
    if len(split_port) != 2:
        return False

    port = split_port[1]
    subnets = split_subnets[:3] + [split_port[0]]

    for number in subnets:
        if number.isdigit():
            if (int(number) > 255):
                return False
        else:
            return False

    if port.isdigit():
        if int(port) > 65535:
            return False
    else:
        return False

    return True


# This tests your code with the examples given in the question, 
# and is provided only for your convenience.
if __name__ == '__main__':
    for address in ["127.12.23.43:5000",
                   "255.255.255.255:65535",
                   "0.0.0.0:0",
                   "01.02.03.04:05"]:
        print is_valid_socket_address(address)

    for address in ["-127.12.23.43:5000",
                   "127.A:-12",
                   "%.0.0.0:0",
                   "test",
                   "",
                   "!@#$%^&*....:",
                   "1.2.3.4",
                   ".1.2.3.4:5",
                   "4.4.4.4:-4"]:
        print not is_valid_socket_address(address)


