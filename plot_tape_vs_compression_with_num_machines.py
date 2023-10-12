import matplotlib.pyplot as plt
import csv

machine_columns = ['m0_start_position', 'm1_start_position', 'm2_start_position', 'm3_start_position', 'm4_start_position']

with open('analysis.csv', 'r') as file:
    reader = csv.DictReader(file)

    tape_sizes = []
    output_compressions = []
    machine_counts = []  # List to store the number of machines for each data point

    for row in reader:
        tape_size = int(row['img_and_tape_width'])
        output_compression = 1 - float(row['output_compression'])

        # Determine the number of machines based on the 'mX_start_position' columns
        machine_count = sum(1 for col in machine_columns if row[col] != '')
        machine_counts.append(machine_count)

        tape_sizes.append(tape_size)
        output_compressions.append(output_compression)

# Define a colormap based on the number of machines
colormap = plt.get_cmap('viridis')  # You can choose a different colormap

# Create a scatterplot with color mapping based on the number of machines
plt.scatter(tape_sizes, output_compressions, c=machine_counts, cmap=colormap, s=0.25, label='Data Points')
plt.xlabel('Tape width')
plt.ylabel('Compression ratio')

# Add a color bar to indicate the number of machines
cbar = plt.colorbar()
cbar.set_label('Number of machines')

# Remove the title
plt.title('')
plt.tight_layout()

plt.show()
