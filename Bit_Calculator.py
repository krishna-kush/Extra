# Understanding how computers work with binary currents with bitwise operations AND how arthematic operations work on that, by developing a calculator that can do the same.


# What is binary numbers? => 0 and 1, they are simply like a switch, either on or off, 1 or 0.

# What is a bit? => A bit is a single binary digit, 0 or 1.

# What is a byte? => A byte is a group of 8 bits, 8 binary digits, 8 switches, 8 0s and 1s.


# ---------------------------------------------------------------------------------------------------------------------------------------


# Converting a decimal number to binary number


def decimal_to_binary(decimal_number):
    # Brute Code First Try:

    # counting how many bits will be needed to form string or you can say allocating space
    count = 1
    while True:
        meserable = ((2**count)-1)
        if decimal_number > meserable:
            count += 1
        else:
            break
    
    # allocating space
    bin = [] # How can I overwrite bin, because bin is python builtin function not a opersator neither keyword...
    for i in range(count):
        bin.append("0")
    
    # not playing with main argument, a good habbit, maybe I'll need in future
    temp = decimal_number

    # real algorithem
    def biggest(num):
        return 2**num

    for i in range(len(bin)):
        j = len(bin) - 1 - i # just to get number of positing in reverse order, because in binary integer data left hand side has grater value

        if temp >= biggest(j):
            bin[i] = "1" # i is not disturbed here to asign bits in right order, otherwise I have to reverse the list afterwards
            temp = temp - biggest(j) # what I'm doing is iterating through every bit and finding it's turned on value, if grater than value remained from decimal value will turn that bit on and subtract that value from decimal value and loop it further until reached zero
    
    return ''.join(bin) # str is immutable so i had to convert str into list and then vise versa


    # ------------------------------------------------------------------------------------------------------------------------------------------


    # Better Version


    # Best from copilot or reasearch



print(decimal_to_binary(741), bin(741))