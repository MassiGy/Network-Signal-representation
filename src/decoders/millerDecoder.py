import matplotlib.pyplot as mplot
from decoders.utils import draw_extras 
from decoders.config import *

def millerDecoderUsingPloting(binary_code: str, binary_encoding: str) -> None:
    """
        @author Massiles GHERNAOUT

        @description millerDecoderUsingPloting 

        This function will take the binary code and use ploting lib to draw its
        signal signature to the end user's screen

        This signal will be drawn following the miller schema, where a 1 is
        represented by a change in the signal voltage (go from one pole to the
        other) during the following clock cycle, and a 0 is represented by an
        absence of transition. If the previous spike was also a 0 then we
        change the voltage before the next clock cycle.

    """

    binary_code_len = len(binary_code)
    # assume that the signal starts at a negative voltage
    prevPoint = NEGATIVE_SPIKE

    for i in range(binary_code_len):
        draw_extras(i, binary_encoding)

        if binary_code[i] == str(POSITIVE_SPIKE):

            # change the voltage according to the previous point
            if prevPoint == POSITIVE_SPIKE:

                # switch the voltage polo

                # draw a horizental line from the start to the middle at the top 
                mplot.plot([i, i+0.5], [1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a vertial line from top to buttom at the middle
                mplot.plot([i+0.5, i+0.5+EPSILON], [1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a horizental line from the middle to the end at the buttom
                mplot.plot([i+0.5+EPSILON, i+1], [-1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # update the previous point
                prevPoint = NEGATIVE_SPIKE

            elif prevPoint == NEGATIVE_SPIKE: 

                # draw a horizental line from the start to the middle at the buttom
                mplot.plot([i, i+0.5], [-1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a vertial line from buttom to top at the middle
                mplot.plot([i+0.5, i+0.5+EPSILON], [-1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a horizental line from the middle to the end at the top 
                mplot.plot([i+0.5+EPSILON, i+1], [1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # update the previous point
                prevPoint = POSITIVE_SPIKE

        elif binary_code[i] == str(NEGATIVE_SPIKE):
                # draw a vertical line from prevPoint to prevPoint +1
                # this will illustrate the absence of a transition 
                if prevPoint == POSITIVE_SPIKE:
                    mplot.plot([i,i+1], [1, 1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)
                elif prevPoint == NEGATIVE_SPIKE:
                    mplot.plot([i,i+1], [-1, -1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)
                
                # previous point remains the same

        if i < binary_code_len -1 and binary_code[i] == binary_code[i+1]  and binary_code[i] == str(NEGATIVE_SPIKE):
            # draw a vertical line before the next clock cycle
            mplot.plot([i+1, i+1+EPSILON], [1,-1],color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)


            # update the previous point to the opposite of what it was
            if prevPoint == POSITIVE_SPIKE: 
                prevPoint = NEGATIVE_SPIKE
            elif prevPoint == NEGATIVE_SPIKE: 
                prevPoint = POSITIVE_SPIKE

    mplot.show()





