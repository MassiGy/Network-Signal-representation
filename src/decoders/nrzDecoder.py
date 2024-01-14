import matplotlib.pyplot as mplot
from decoders.utils import draw_extras 
from decoders.config import *

def nrzDecoderUsingPloting(binary_code: str, binary_encoding: str) -> None:

    binary_code_len = len(binary_code)
    for i in range(binary_code_len):
        draw_extras(i, binary_encoding)

        if binary_code[i] == str(POSITIVE_SPIKE) : 
            mplot.plot([i, i +1], [1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)
        elif binary_code[i] == str(NEGATIVE_SPIKE): 
            mplot.plot([i, i +1], [-1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

        # if the following spike is not the same as the current one, then draw a 
        # vertical line between the two clock phases
        if i + 1 < binary_code_len and binary_code[i] != binary_code[i+1]: 
            mplot.plot([i+1, i+1+EPSILON], [1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

    mplot.show()


