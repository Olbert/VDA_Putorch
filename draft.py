# -*- coding: utf-8 -*-
"""lab_original.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zPEiXOQCj8RywxhNJxoUrXOU0nw12Kb2
"""

import nibabel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tqdm import tqdm_notebook
import seaborn as sns
import os
import random
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import os
import h5py

import utils
import os
import scipy.misc
roots = (['E:\\Lab\\resources\\MICCAI_BraTS_2019_Data_Training\\MICCAI_BraTS_2019_Data_Training\\HGG\\',
          'E:\\Lab\\resources\\MICCAI_BraTS_2019_Data_Training\\MICCAI_BraTS_2019_Data_Training\\LGG\\'])

patient_folders = [os.path.join(roots[0], p) for p in os.listdir(roots[0])] + \
                  [os.path.join(roots[1], p) for p in os.listdir(roots[1])]

def save100_images():
    train_data, valid_data, test_data = np.load("E:\Lab\Lab_VDA_Local\dataset_split.npy", allow_pickle=True)


    for i in range(0,100):
        scipy.misc.imsave('E:\Lab\images\img_0_'+str(i)+'.jpg', train_data[i,0])
        scipy.misc.imsave('E:\Lab\images\img_1_'+str(i)+'.jpg', train_data[i,1])
        scipy.misc.imsave('E:\Lab\images\img_2_'+str(i)+'.jpg', train_data[i,2])
        scipy.misc.imsave('E:\Lab\images\img_3_'+str(i)+'.jpg', train_data[i,3])

def save_images(file):
    data = np.load(file)
    for i in range(0,data.shape[0]):
        scipy.misc.imsave('E:\\Lab\\images\\aug\\img_0_'+str(i)+'.jpg', data[i,0])
        scipy.misc.imsave('E:\\Lab\\images\\aug\\img_1_'+str(i)+'.jpg', data[i,1])
        scipy.misc.imsave('E:\\Lab\\images\\aug\\img_2_'+str(i)+'.jpg', data[i,2])
        scipy.misc.imsave('E:\\Lab\\images\\aug\\img_3_'+str(i)+'.jpg', data[i,3])



data ,_,_ = np.load("E:\\Lab\\resources\\dataset_split.npy",allow_pickle=True)
data = utils.PreProcessor.augment(data[0:10])
np.save("E:\\Lab\\resources\\dataset_healthy_aug_smaa.npy", data)
save_images("E:\\Lab\\resources\\dataset_healthy_aug_smaa.npy")