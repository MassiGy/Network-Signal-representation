import matplotlib.pyplot as mplot
from decoders.config import *

# just to extract away the bg lines drawing and 
# all the signal none related stuff dowings
def draw_extras(index: int, binary_encoding: str): 
    mplot.axvline(x=index, color=BG_VIRTICAL_LINES_COLOR, linestyle='--', linewidth=BG_LINES_WIDTH)
    mplot.axhline(y=NOSIGNAL_SPIKE, color=BG_HORIZENTAL_LINES_COLOR, linestyle='--', linewidth=BG_LINES_WIDTH)
    mplot.axhline(y=NEGATIVE_SPIKE, color=BG_HORIZENTAL_LINES_COLOR, linestyle='--', linewidth=BG_LINES_WIDTH)
    mplot.axhline(y=POSITIVE_SPIKE, color=BG_HORIZENTAL_LINES_COLOR, linestyle='--', linewidth=BG_LINES_WIDTH)

    mplot.xlabel('time')
    mplot.ylabel('Volts')
    mplot.title(binary_encoding)



