
def reverseBits( n: int):
    """This code coverts the LSB to MSB and it reversed it one by one"""
    result = 0
    for _ in range(32):
        result <<= 1  # Make space for next bit
        result |= n & 1  # Add least significant bit of n
        n >>= 1
    return result
print(reverseBits(5))