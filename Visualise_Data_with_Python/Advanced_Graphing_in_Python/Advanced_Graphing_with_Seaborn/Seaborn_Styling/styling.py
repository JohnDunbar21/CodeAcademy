import seaborn as sns

# THEMES
# seaborn has five built-in themes to style its plots: darkgrid, whitegrid, dark, white, and ticks. The default is darkgrid. 

sns.set_style("darkgrid")

# DESPINE
# spines are the borders that contain the visualisation: by default, an image has four spines. 
# you can remove all spines by calling:

sns.despine()

# you can keep certain spines by adding a True value to the spine you wish to keep, such as:

sns.despine(left=True,bottom=True)

# SCALING
# you can set the visual format, or context, using:

sns.set_context() 

# this takes a minimum of 1 and a maximum of 3 parameters. 
# In order of relative size, the different scales are: paper, notebook, and poster. Notebook is the default. 

sns.set_context("paper") 

# you can also add font_scale and linewidth:

sns.set_context("poster", font_scale=0.5, rc={"grid.linewidth": 0.6})

# the linewidth determines how 'chunky' the grid lines are. 

# rc stands for return command, and can take the following parameters:

rc={'axes.labelsize': 17.6,
 'axes.titlesize': 19.200000000000003,
 'font.size': 19.200000000000003,
 'grid.linewidth': 1.6,
 'legend.fontsize': 16.0,
 'lines.linewidth': 2.8000000000000003,
 'lines.markeredgewidth': 0.0,
 'lines.markersize': 11.200000000000001,
 'patch.linewidth': 0.48,
 'xtick.labelsize': 16.0,
 'xtick.major.pad': 11.200000000000001,
 'xtick.major.width': 1.6,
 'xtick.minor.width': 0.8,
 'ytick.labelsize': 16.0,
 'ytick.major.pad': 11.200000000000001,
 'ytick.major.width': 1.6,
 'ytick.minor.width': 0.8}


# Save a palette to a variable:
palette = sns.color_palette("bright")
 
# Use palplot and pass in the variable:
sns.palplot(palette)

# Set the palette using the name of a palette:
sns.set_palette("Paired")

# Call the sns.set() function 
sns.set()
for col in 'xy':
  plt.hist(data[col], normed=True, alpha=0.5)

# seaborn has six default colour palettes: deep, muted, pastel, bright, dark, and colorblind. 

# Set the palette to the "pastel" default palette:
sns.set_palette("pastel")

# check color brewer schemes(http://colorbrewer2.org)

