#import modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon

#import csv as df and select columns
#include filename
df=pd.read_csv('FILENAME.csv', index_col=False)
df=df[['PitchNo','Pitcher','TaggedPitchType','RelSpeed','SpinRate','Tilt','InducedVertBreak',
       'HorzBreak','PitchCall','PlateLocHeight','PlateLocSide']]

#initialize plot axis
fig, (ax1, ax2) = plt.subplots(1,2)

#plotting
command_plot = sns.scatterplot(ax=ax1,x=df['PlateLocSide'],y=df['PlateLocHeight'],hue=df['TaggedPitchType'],s=25)
break_plot = sns.scatterplot(ax=ax2,x=df['HorzBreak'],y=df['InducedVertBreak'], hue=df['TaggedPitchType'],s=25)

#plot formatting
ax1.set_xlim(-2,2)
ax1.set_ylim(-0.5,5.5)
ax2.set_xlim(-30,30)
ax2.set_ylim(-30,30)
ax1.set_aspect('equal', adjustable='box')
ax2.set_aspect('equal', adjustable='box')
ax1.legend(bbox_to_anchor=(1.05,1), loc='upper left', ncol=len(df.columns), prop={'size': 8})
ax2.get_legend().remove()
ax1.set_xlabel('',fontsize=1)
ax1.set_ylabel('',fontsize=1)
ax2.set_xlabel('',fontsize=1)
ax2.set_ylabel('',fontsize=1)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)

#add patches
ax1.add_patch(Rectangle((-0.708, 1.5), 1.416, 2.1, fill=False, edgecolor='black', lw=1))
ax1.add_patch(Polygon([[-0.708, 0.01], [-0.608, 0.21], [0, 0.41], [0.608, 0.21], [0.708, 0.01]],closed=True,fill=False))
ax2.plot((-30,30),(0,0), color='black', linewidth=1)
ax2.plot((0,0),(-30,30), color='black', linewidth=1)

#save fig as png
#include name
plt.savefig('NAME.png')
