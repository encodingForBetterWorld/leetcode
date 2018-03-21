# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
# Related problem: Reverse Integer

def reverseBits(n):
    if n > 2**32 or n < 0:
        return
    s = "{:0>32}".format(bin(n)[2:])[::-1]
    return int(s,2)

print reverseBits(43261596)
print "{0:032b}".format(123)

