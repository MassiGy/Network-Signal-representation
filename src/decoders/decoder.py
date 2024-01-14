from decoders.config import OUTPUTING_TO_FILE
from decoders.manchesterDiffDecoder import manchesterDiffDecoderUsingPloting
from decoders.nrzDecoder import nrzDecoderUsingPloting
from decoders.manchesterDecoder import manchesterDecoderUsingPloting


# SUPPORTED_ENCODING = ["NRZ", "NRZI", "Manchester", "Manchester Diff", "Miller"]
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
            # TODO 
            manchesterDiffDecoderUsingPloting(binary_code, binary_encoding)
        elif binary_encoding == "Miller": 
            # TODO 
            print("todo")
        else :
            # TODO
            print("todo")




