import os
import sys
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import pearsonr
from scipy.signal import chirp, find_peaks, peak_widths

import warnings
warnings.filterwarnings('ignore')


class ER_AM():


    def __init__(self, df, age):
        self.name = name
        self.age = age