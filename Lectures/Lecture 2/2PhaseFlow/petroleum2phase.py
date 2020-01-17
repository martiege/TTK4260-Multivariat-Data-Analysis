import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Petroleum2phasedata.csv',sep=';')


plt.plot(data['Vsg'])
plt.show()
