import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
path=("C:\\Users\\subhu\\OneDrive\\Desktop\\input.xlsx")
file = pd.read_excel(path)
length = file['Length'].tolist()
print(max(length))
breadth = file['Breadth'].tolist()
print(breadth)
quant = file['Quantity'].tolist()
xlims = (0,max(length))
ylims = (0,max(breadth))
fig1 = plt.figure()
color=['r','b','g','m','k']
ax1 = fig1.add_subplot(111, aspect='equal')
for i,j,t,color in zip(length,breadth,quant,color):
        for y in range(t):
            ax1.add_patch(
                patches.Rectangle((np.random.randint(0,30),np.random.randint(0,30) ),i,j,linewidth=1,edgecolor= color,facecolor='none'))
plt.ylim(0,50)
plt.xlim(0,50)
plt.show()