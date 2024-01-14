from decoders.config import *
from decoders.decoder import decoder


# get usr input
binary_code = str(input("Please enter your binary code: "))
binary_encoding = str(input("Please enter encoding format (respect case) " + str(SUPPORTED_ENCODING) + ": "))


if binary_encoding not in SUPPORTED_ENCODING:
    print("Unsupported encoding (ABORT)")
    exit(NON_SUPPORTED_ENCODING)

if len(binary_code) == 0 : 
    print("Binary code should not be empty (ABORT)")
    exit(BINARY_CODE_EMPTY)




# write the encoding/signal into the accumulator
accumulator = ""
decoder(binary_code, binary_encoding, accumulator)


if OUTPUTING_TO_FILE: 
    file = open("./signal.out.txt", "a")
    file.write(accumulator)
    file.close()

