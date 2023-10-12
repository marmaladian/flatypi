import matplotlib.pyplot as plt
import csv
import numpy as np

min_tape_width = 25
max_tape_width = 25

with open('analysis.csv', 'r') as file:
    reader = csv.DictReader(file)

    input_compressions = []
    output_compressions = []
    tape_widths = []

    for row in reader:
        input_compression = 1 - float(row['input_compression'])
        output_compression = 1 - float(row['output_compression'])

        tape_size = int(row['img_and_tape_width'])

        if min_tape_width <= tape_size <= max_tape_width:
            tape_widths.append(tape_size)
            input_compressions.append(input_compression)
            output_compressions.append(output_compression)

colormap = plt.get_cmap('viridis')
normalised_input_compressions = (input_compressions - np.min(input_compressions)) / (np.max(input_compressions) - np.min(input_compressions))

# c='#00C894'
plt.scatter(tape_widths, output_compressions, c=normalised_input_compressions, cmap=colormap, s=0.1, label='Data Points')
plt.xlabel('Tape width')
plt.ylabel('Output compression ratio')
# plt.title('Scatterplot of tape width vs. compression ratio')
plt.tight_layout()

cbar = plt.colorbar()
cbar.set_label('Input compression ratio')

plt.title('')
plt.suptitle('')
plt.tight_layout()

# Display the plot
plt.show()
