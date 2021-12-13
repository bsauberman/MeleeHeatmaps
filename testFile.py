
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
uniform_data = np.random.rand(10, 12)
uniform_data[0][1] = 1
print(uniform_data)
ax = sns.heatmap(uniform_data)
plt.show()
