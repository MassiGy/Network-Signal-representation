from decoders.config import NON_IMPLEMENTED, NON_SUPPORTED_ENCODING, OUTPUTING_TO_FILE
from decoders.manchesterDiffDecoder import manchesterDiffDecoderUsingPloting
from decoders.millerDecoder import millerDecoderUsingPloting
from decoders.nrzDecoder import nrzDecoderUsingPloting
from decoders.manchesterDecoder import manchesterDecoderUsingPloting



# SUPPORTED_ENCODING = ["NRZ", "Manchester", "Manchester Diff", "Miller"]
def decoder(binary_code: str, binary_encoding: str, accumulator: str) -> None:

    if OUTPUTING_TO_FILE == False : 
        # use ploting lib
        accumulator += "USING PLOTING LIB, NO OUTPUT FILE USED."

        # swith on the supported encodings and call the right method
        if binary_encoding == "NRZ": 
            nrzDecoderUsingPloting(binary_code, binary_encoding)

        elif binary_encoding == "Manchester":
            manchesterDecoderUsingPloting(binary_code, binary_encoding)

        elif binary_encoding == "Manchester Diff":
            manchesterDiffDecoderUsingPloting(binary_code, binary_encoding)

        elif binary_encoding == "Miller": 
            millerDecoderUsingPloting(binary_code, binary_encoding)

        else :
           print("Unsupported encoding (ABORT)")
           exit(NON_SUPPORTED_ENCODING)
    else: 
        # plot to file
        accumulator += "USING AN OUTPUT FILE, NO PLOTING LIB USED."
        accumulator += "Not implemented yet (ABORT)"
        exit(NON_IMPLEMENTED)
        





