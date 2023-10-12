import matplotlib.pyplot as plt
import csv
import numpy as np

min_tape_width = 25
max_tape_width = 25

with open('analysis.csv', 'r') as file:
    reader = csv.DictReader(file)

    steps = []
    output_compressions = []
    tape_widths = []

    for row in reader:
        step = int(row['img_height_and_steps'])
        output_compression = 1 - float(row['output_compression'])
        tape_size = int(row['img_and_tape_width'])

        # if min_tape_width <= tape_size <= max_tape_width:
        tape_widths.append(tape_size)
        steps.append(step)
        output_compressions.append(output_compression)

colormap = plt.get_cmap('viridis')
# normalised_step_compressions = (steps - np.min(steps)) / (np.max(steps) - np.min(steps))

# c='#00C894'
plt.scatter(tape_widths, output_compressions, c=steps, cmap=colormap, s=0.1, label='Data Points')
plt.xlabel('Tape width')
plt.ylabel('Output compression ratio')
# plt.title('Scatterplot of tape width vs. compression ratio')
plt.tight_layout()

cbar = plt.colorbar()
cbar.set_label('Steps')

plt.title('')
plt.suptitle('')
plt.tight_layout()

# Display the plot
plt.show()
