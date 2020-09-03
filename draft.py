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

def save_images(file, num):
    data = np.load(file)[0:num]
    for i in range(0,data.shape[0]):
        scipy.misc.imsave('E:\\Lab\\images\\augs\\img_0_'+str(i)+'.jpg', data[i,0])
        scipy.misc.imsave('E:\\Lab\\images\\augs\\img_1_'+str(i)+'.jpg', data[i,1])
        scipy.misc.imsave('E:\\Lab\\images\\augs\\img_2_'+str(i)+'.jpg', data[i,2])
        scipy.misc.imsave('E:\\Lab\\images\\augs\\img_3_'+str(i)+'.jpg', data[i,3])


#
# train_imgs = np.load("E:\\Lab\\resources\\dataset_healthy.npy", allow_pickle=True)
#
# train_imgs_ids = list(range(len(train_imgs)))
# train_data_ids, test_vald_ids = train_test_split(train_imgs_ids, test_size=0.20, random_state=100, shuffle=True)
# vald_data_ids, test_data_ids = train_test_split(test_vald_ids, test_size=0.30, random_state=100, shuffle=True)
#
# data = np.array((train_imgs[train_imgs_ids],
#         train_imgs[vald_data_ids],
#         train_imgs[test_data_ids]))
#
# np.save("E:\\Lab\\resources\\dataset_split.npy", data)
#
# data ,_,_ = np.load("E:\\Lab\\resources\\dataset_split.npy", allow_pickle=True)
# try:
#     hdf5_dataset = h5py.File("./dataset_healthy.h5", "w")
#     dset = hdf5_dataset.create_dataset('train_imgs', data=data)
#     dset = hdf5_dataset.create_dataset('valid_imgs', data=data)
#     dset = hdf5_dataset.create_dataset('test_imgs', data=data)
# except:
#     hdf5_dataset = h5py.File("./dataset_healthy.h5", "a")
#     del hdf5_dataset['train_imgs']
#     del hdf5_dataset['valid_imgs']
#     del hdf5_dataset['test_imgs']
#     dset = hdf5_dataset.create_dataset('train_imgs', data=data)
#     dset = hdf5_dataset.create_dataset('valid_imgs', data=data)
#     dset = hdf5_dataset.create_dataset('test_imgs', data=data)
#     print('File already exists. Overwriting...')


# hdf5_dataset.close()
#
#
# data_aug = utils.PreProcessor.augment(data, count=2)
# np.save("E:\\Lab\\resources\\dataset_healthy_aug_new.npy", data_aug)
#
#
# try:
#     hdf5_dataset = h5py.File("./dataset_healthy_aug.h5", "w")
#     dset = hdf5_dataset.create_dataset('train_imgs', data=data_aug)
# except:
#     hdf5_dataset = h5py.File("./dataset_healthy.h5", "a")
#     del hdf5_dataset['train_imgs']
#     hdf5_dataset.create_dataset("train_imgs", data=data_aug)
#     print('File already exists. Overwriting...')
# hdf5_dataset.close()




# roots = (['E:\\Lab\\resources\\MICCAI_BraTS_2019_Data_Training\\MICCAI_BraTS_2019_Data_Training\\HGG\\',
#               'E:\\Lab\\resources\\MICCAI_BraTS_2019_Data_Training\\MICCAI_BraTS_2019_Data_Training\\LGG\\'])
#
# patient_folders = [os.path.join(roots[0], p) for p in os.listdir(roots[0])] + \
#                       [os.path.join(roots[1], p) for p in os.listdir(roots[1])]
#
# utils.DataLoader.download_data(patient_folders,data = "mask")



sums = np.load("sums.npy")

a = 1















