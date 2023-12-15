import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(0, 585, 1)
y1 = np.random.randint(1, 10, size=585)
y2 = np.random.randint(1, 10, size=585)
y3 = np.random.randint(1, 10, size=585)
y4 = np.random.randint(1, 10, size=585)


# Creating the stacked area chart
plt.stackplot(x, y1, y2, y3, y4, labels=['Series 1', 'Series 2', 'Series 3', 'Series 4'])

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Stacked Area Chart')
plt.legend(loc='upper left')

# Display the plot
plt.show()