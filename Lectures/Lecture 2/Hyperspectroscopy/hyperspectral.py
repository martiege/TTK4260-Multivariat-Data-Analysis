import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from dataloader import Dataloader
from preprocess import create_table, create_test_set
from preprocess import data_preprocess, remove_class
from preprocess import resample_dataset, hotellings_t2, inspect_outliers, normalize
from preprocess import remove_outliers

# Load data
dir_path = 'Hyperspectral'
data_file = 'indian_pines.mat'
cali_file = 'calibration.mat'
labels_file = 'indian_pines_gt.mat'
dataloader = Dataloader(dir_path, data_file, cali_file, labels_file)

# Create tables, resample and create test set
X = dataloader.get_calibrated_samples()
Y = dataloader.get_labels()
W = dataloader.get_wave_lengths()
X = create_table(X)
Y = create_table(Y)
X, Y = resample_dataset(X, Y, 4.0)
X_train, Y_train, X_test, Y_test = create_test_set(X, Y, test_frac=0.30)

m,n=X.shape
print(m,n)

plt.figure(figsize=(15,10))
for i in range(m-1):
    plt.plot(W,X[i,:])
plt.show()