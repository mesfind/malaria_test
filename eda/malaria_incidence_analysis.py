import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def load_malaria_data(filepath):
    data = pd.read_csv(filepath)
    return data

def cal_incidence(cases, pop):
    incidence = (cases / pop) * 1000
    return incidence
 
x = np.array([1,2,3,4])
y = x*x
plt.plot(x,y)
