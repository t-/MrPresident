import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc

mpl.rcParams['figure.figsize'] = [3.622,2.323]
mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.size'] = 8.
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.weight'] = 200
mpl.rcParams['legend.fontsize'] = 8
mpl.rcParams['axes.labelweight'] = 200
mpl.rcParams['axes.labelsize'] = 8.
mpl.rcParams['xtick.labelsize'] = 8
mpl.rcParams['ytick.labelsize'] = 8
mpl.rcParams['xtick.major.size'] = 1.5
mpl.rcParams['ytick.major.size'] = 1.5
mpl.rcParams['axes.linewidth'] = 0.0

def simpleaxes(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

colors=['#e2431e',  '#e57368',   '#e7711b',  '#cddc39',  '#5f9654',  '#1a8763',  '#15a0c8',  '#3f5ca9',  '#9e69af',  '#5c3292',  '#a61d4c',  '#871b47',  '#795548',  '#572a1a',  '#808080',  '#1a1a1a']
