import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wh2015 = pd.read_csv("world-happiness-index-dataset/2015.csv", ",")
wh2016 = pd.read_csv("world-happiness-index-dataset/2016.csv", ",")
wh2017 = pd.read_csv("world-happiness-index-dataset/2017.csv", ",")
wh2018 = pd.read_csv("world-happiness-index-dataset/2018.csv", ",")
wh2019 = pd.read_csv("world-happiness-index-dataset/2019.csv", ",")

print(wh2015.head())

plt.plot(wh2015['Trust (Government Corruption)'])
plt.plot(wh2016['Trust (Government Corruption)'])
# plt.plot(wh2017['Trust (Government Corruption)'])
# plt.plot(wh2018['Trust (Government Corruption)'])
# plt.plot(wh2019['Trust (Government Corruption)'])
plt.show()
