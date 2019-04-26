# -*- coding:utf-8 -*-

import array
import os
import numpy as np
from matplotlib import pyplot as plt
import librosa
import tqdm


filelist=os.listdir('/home/xlh/下载/lkl/SpeechDenoisingWithDeepFeatureLosses/dataset/data/trainset_clean')
for file in filelist:
    if(file.endswith('wav')):
        filename=file
        noise_left=np.load('noise.npy')
        filename=os.path.join('trainset_clean',filename)
        print(filename)
        data,fs=librosa.core.load(filename,sr=16000)
        x=len(data)//len(noise_left)
        print(x)
        noise=np.zeros(len(data))
        for i in range(x):
            noise[i*5000:(i+1)*5000]=noise_left
        data_noise=(data.astype('float32')+0.0001*noise).astype(np.float32)
        librosa.output.write_wav('111/{}'.format(file),data_noise,fs)

