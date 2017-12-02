def swapOddEvenBits(x):
    return ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1)


print(swapOddEvenBits(23))