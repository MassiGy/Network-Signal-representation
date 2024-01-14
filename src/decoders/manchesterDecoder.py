import matplotlib.pyplot as mplot
from decoders.utils import draw_extras 
from decoders.config import *

def manchesterDecoderUsingPloting(binary_code: str, binary_encoding: str) -> None:

    binary_code_len = len(binary_code)
    for i in range(binary_code_len):
        draw_extras(i, binary_encoding)

        if binary_code[i] == str(POSITIVE_SPIKE):

            # draw a horizental line to the middel at the top
            mplot.plot([i, i+0.5], [1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

            # draw a vertical line from top to buttom + Epsilon, since plot
            # can't draw a line from top to buttom with out deviating the x axis
            mplot.plot([i+0.5, i+0.5 + EPSILON], [1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

            # draw a horizental line to from the middel to the end at the buttom
            mplot.plot([i+0.5+EPSILON, i+1], [-1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

        elif binary_code[i] == str(NEGATIVE_SPIKE):
            
            # draw a horizental line to the middel at the buttom
            mplot.plot([i, i+0.5], [-1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

            # draw a vertical line from the buttom to the top
            mplot.plot([i+0.5, i+0.5+EPSILON], [-1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

            # draw a horizental line to the middel at the top
            mplot.plot([i+0.5+EPSILON, i+1], [1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)




        # if the following spike is the same as the current one, then draw a 
        # vertical line between the two clock phases
        if i + 1 < binary_code_len and binary_code[i] == binary_code[i+1]: 
            mplot.plot([i+1, i+1+EPSILON], [-1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

    mplot.show()





