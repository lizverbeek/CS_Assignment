import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with open('istherecorrelation.csv') as file:
	df = pd.read_csv(file, delimiter=';', decimal=',')
	df.columns = ['Year', 'WO', 'NL Beer consumption']

plt.rcParams["figure.dpi"] = 300
df.plot(x = 'WO', y = 'NL Beer consumption', kind = 'scatter')
plt.xlabel('WO [x1000]')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')
plt.show()