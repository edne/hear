import numpy as np
from hear import hear


def callback(data):
    mean = abs(np.mean(data[0]))
    dB = 10*np.log(mean)  # negative number
    bar = int(60 + dB)    # 60dB as thresold
    print("-"*bar + "|")

hear(callback)
