import matplotlib.pyplot as mplot
import numpy as np

def nrzDecoderUsingPloting(binary_code: str, binary_encoding: str) -> None:

    mplot.plot([1, len(binary_code)], [-1, 1], color="black", linestyle="-", linewidth=1)
    mplot.show()


