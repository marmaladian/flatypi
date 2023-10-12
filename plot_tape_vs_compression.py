import matplotlib.pyplot as plt
import csv

with open('analysis.csv', 'r') as file:
    reader = csv.DictReader(file)

    tape_sizes = []
    output_compressions = []

    for row in reader:
        tape_size = int(row['img_and_tape_width'])
        output_compression = 1 - float(row['output_compression'])

        tape_sizes.append(tape_size)
        output_compressions.append(output_compression)

plt.scatter(tape_sizes, output_compressions, c='#00C894', s=0.1, label='Data Points')
plt.xlabel('Tape width')
plt.ylabel('Compression ratio')
# plt.title('Scatterplot of tape width vs. compression ratio')
plt.tight_layout()

plt.show()
