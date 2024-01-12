import matplotlib.pyplot as mplot
import numpy as np
from decoders.utils import draw_extras 
from decoders.config import *

def nrzDecoderUsingPloting(binary_code: str, binary_encoding: str) -> None:

    binary_code_len = len(binary_code)
    for i in range(binary_code_len):
        draw_extras(i)


    mplot.show()




