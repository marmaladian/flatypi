import matplotlib.pyplot as plt
import csv
import numpy as np

min_tape_width = 10
max_tape_width = 25

with open('analysis.csv', 'r') as file:
    reader = csv.DictReader(file)

    input_compressions = []
    output_compressions = []

    for row in reader:
        input_compression = 1 - float(row['input_compression'])
        output_compression = 1 - float(row['output_compression'])

        tape_size = int(row['img_and_tape_width'])

        if min_tape_width <= tape_size <= max_tape_width:
            input_compressions.append(input_compression)
            output_compressions.append(output_compression)

# c='#00C894'
plt.scatter(input_compressions, output_compressions, c='#00C894', s=0.1, label='Data Points')
plt.xlabel('Input compression ratio')
plt.ylabel('Output compression ratio')
# plt.title('Scatterplot of tape width vs. compression ratio')
plt.tight_layout()

plt.title('')
plt.suptitle('')
plt.tight_layout()

# Display the plot
plt.show()
