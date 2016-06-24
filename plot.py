import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot()


def graph(formula, x_range, style='k', label=''):
    x = np.array(x_range)
    y = eval(formula)
    ax.plot(x, y, style, label=label)

graph('x', range(0, 250), 'r--', 'f(x)=x')
graph('255 - x', range(0, 250), 'k','f(x)=255-x')
graph('(100.0/255) * x + 100', range(0, 250), 'k', 'f(x)=100*x/255 + 100')
graph('255.0 * (x/255.0)**2', range(0, 250), 'k','f(x)=255 * (x/255)^2')

# Now add the legend with some customizations.
legend = ax.legend(loc='upper center', shadow=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.90')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width


plt.show()
