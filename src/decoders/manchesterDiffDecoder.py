import matplotlib.pyplot as mplot
from decoders.utils import draw_extras 
from decoders.config import *

def manchesterDiffDecoderUsingPloting(binary_code: str, binary_encoding: str) -> None:
    """
        @author Massiles GHERNAOUT

        @description manchesterDiffDecoderUsingPloting 

        This function will take the binary code and use ploting lib to draw its
        signal signature to the end user's screen

        This signal will be drawn following the differential manchester schema,
        where a 1 is represented by a change in the signal voltage (go from one
        pole to the other) during the following clock cycle, and a 0 is
        represented by a former change of voltage at the start of the next
        clock cycle followed by a second volatage change during the next clock
        cycle.

    """

    binary_code_len:int= len(binary_code)
    prevPoint = NOSIGNAL_SPIKE

    for i in range(binary_code_len):
        draw_extras(i, binary_encoding)

        if binary_code[i] == str(POSITIVE_SPIKE):

            if prevPoint == NOSIGNAL_SPIKE:
                # first entrence
                # just go from a pole to another

                # draw a line at the buttom from the start to the middle
                mplot.plot([i, i+0.5],[-1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a line from the buttom to the top at the middle
                mplot.plot([i+0.5, i+0.5+EPSILON],[-1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a line from the middle to the end at the top 
                mplot.plot([i+0.5+EPSILON, i+1],[1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # update the previous point
                prevPoint = POSITIVE_SPIKE

            elif prevPoint == POSITIVE_SPIKE: 
                # switch from pole to another

                # draw a line at the top from the start to the middle
                mplot.plot([i, i+0.5], [1,1], color=FG_LINES_COLOR,linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a line from the top to the buttom at the middle
                mplot.plot([i+0.5, i+0.5+EPSILON], [1,-1], color=FG_LINES_COLOR,linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a line from the middle to the end at the buttom
                mplot.plot([i+0.5+EPSILON, i+1], [-1,-1], color=FG_LINES_COLOR,linestyle="-", linewidth=FG_LINES_WIDTH)

                # update the previous point
                prevPoint = NEGATIVE_SPIKE


            elif prevPoint == NEGATIVE_SPIKE:
                # switch from pole to another

                # draw a line from the start to the middle at the buttom
                mplot.plot([i,i+0.5], [-1,-1], color=FG_LINES_COLOR,linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a line from the buttom to the top at the middle
                mplot.plot([i+0.5, i+0.5+EPSILON], [-1,1], color=FG_LINES_COLOR,linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a line at the top from the middle to the end
                mplot.plot([i+0.5+EPSILON, i+1], [1,1], color=FG_LINES_COLOR,linestyle="-", linewidth=FG_LINES_WIDTH)

                # update the previous point
                prevPoint = POSITIVE_SPIKE


            else: 
                # illegal state
                raise Exception("illegal state")

        elif binary_code[i] == str(NEGATIVE_SPIKE):
            # we need a former voltage change before the clock cycle then
            # another following voltage change during the clock cycle

            # draw the line for the former voltage change
            mplot.plot([i,i+EPSILON], [1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

            # update the previous point to the opposite of what it was
            if prevPoint == POSITIVE_SPIKE: 
                prevPoint = NEGATIVE_SPIKE
            elif prevPoint == NEGATIVE_SPIKE: 
                prevPoint = POSITIVE_SPIKE



            # change the voltage pole according to the previous point
            if prevPoint == POSITIVE_SPIKE:

                # draw a horizental line at the top from the start to the middle
                mplot.plot([i,i+0.5], [1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a vertical line from the top the buttom at the middle
                mplot.plot([i+0.5, i+0.5+EPSILON], [1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a horizental line at the buttom from the middle to the end  
                mplot.plot([i+0.5+ EPSILON, i+1], [-1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # update the previous point
                prevPoint = NEGATIVE_SPIKE

            elif prevPoint == NEGATIVE_SPIKE:

                # draw a horizental line at the buttom from the start to the middle  
                mplot.plot([i,i+0.5], [-1,-1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a vertical line from the buttom the top at the middle
                mplot.plot([i+0.5, i+0.5+EPSILON], [-1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # draw a horizental line at the top from the middle to the end
                mplot.plot([i+0.5+EPSILON,i+1], [1,1], color=FG_LINES_COLOR, linestyle="-", linewidth=FG_LINES_WIDTH)

                # update the previous point
                prevPoint = POSITIVE_SPIKE


    mplot.show()





