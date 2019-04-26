# Speech-Denoise-With-Feature-Loss
## Introductions
此项目为中兴众星捧月比赛中，KUNLIN所采用的去噪方法的一部分（并非全部），分享出来给各位学习使用，不当之处还望指正！  

本项目使用中文人声的数据集，在Speech Denoising with Deep Feature Losses网络的基础上fine-tune，得到对中文音频有更好去噪效果的结果。
## Guides for ZTE challenge(Sound Siganal Denoising Competetion)

1.在./data中新建四个文件夹，分别名为trainset_clean，trainset_noisy，valset_clean，valset_noisy，在./dataset中新建两个文件夹分别为valset_noisy,valset_noisy_denoised。

2.下载清华大学的中文语料库[THCHS-30](http://www.openslr.org/18/)中的数据集，或者使用自己的语料数据集。并将其中的音频部分放在./data/trainset_clean文件夹中（注意数据集音频需要wav格式）。

3.运行./data/extract.py来从测试样本中提取你所需的噪声，并保存为xxx.npy格式。

4.运行./data/sox.py，将训练数据集中的音频调整为网络适用的32bit。

5.运行./data/noise.py，创建训练数据集的副本并将提取出的噪声添加到你的副本中作为噪声集。

6.将噪声集的音频全部放入./data/trainset_noisy文件夹中。

7.运行`python senet_train.py -d /data  -o out_folder`，训练模型将会被保存在out_folder文件夹中.

8.将你要去噪的音频文件放入./dataset/valset_noisy中，并运行`python senet_infer.py  -m out_folder`，去噪后的文件将保存在./dataset/valset_noisy_denoised中。（注意去噪所用音频文件需要是32bit的格式）
## Models
out_folder文件夹中已有使用THCHS-30数据集，学习率为1e-4，运行10个epoch微调后得到的10个网络模型，可以直接使用其中一个。

## Contact us
e-mail:852268806@qq.com / lkl6949@mail.ustc.edu.cn

