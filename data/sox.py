# -*- coding:utf-8 -*-
import os

filelist=os.listdir('/home/xlh/下载/lkl/SpeechDenoisingWithDeepFeatureLosses/dataset/data/trainset_clean')
for file in filelist:
    if(file.endswith('wav')):
        filename=file
        filename=filename[:-4]
        x='sox {}.wav -b 32 {}_sox.wav'.format(filename,filename)
        os.system(r'{}'.format(x))
