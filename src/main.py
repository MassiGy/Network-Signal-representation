
# imports 
from decoders.config import BINARY_CODE_EMPTY, NON_SUPPORTED_ENCODING, SUPPORTED_ENCODING
from decoders.decoder import decoder


# get usr input
binary_code = str(input("Please enter your binary code: "))
binary_encoding = str(input("Please enter encoding format (respect case) [NRZ, NRZI, Manchester, Manchester Diff, Muller]: "))


if binary_encoding not in SUPPORTED_ENCODING:
    print("Unsupported encoding (ABORT)")
    print("Supported encoding are: ", )
    exit(NON_SUPPORTED_ENCODING)

if len(binary_code) == 0 : 
    print("Binary code should not be empty (ABORT)")
    exit(BINARY_CODE_EMPTY)



file = open("./signal.out.txt", "a")
# if everything is ok, decode and write the output file.

# write the encoding into the accumulator
accumulator = ""
decoder(binary_code, binary_encoding, accumulator)

file.write(accumulator)

file.close()



