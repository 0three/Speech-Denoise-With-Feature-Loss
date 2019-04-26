# -*- coding:utf-8 -*-

import array
import os
from matplotlib import pyplot
import numpy as np
fileName = '/home/xlh/下载/lkl/Algorithm/fft.pcm' 
file = open(fileName, 'rb')
base = 1 / (1<<15)

shortArray = array.array('h') # int16
size = int(os.path.getsize(fileName) / shortArray.itemsize)
count = int(size / 2)
shortArray.fromfile(file, size) # faster than struct.unpack
file.close()
leftChannel = shortArray[::2]

start=40000
end=45000
noise_left=leftChannel[start:end]
noise_left=noise_left.tolist()
noise_left=np.array(noise_left)
np.save('noise.npy',noise_left )

