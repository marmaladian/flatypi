import random
import uuid

from PIL import Image
import zlib
import os
import platypatterns
import csv

max_steps = 2048

for _ in range(100):
    run_id = uuid.uuid1()
    num_machines = random.choice([1, 2, 3, 4, 5])
    tape_width = random.choice([11, 25, 51, 101, 251])
    random_tape = bool(random.getrandbits(1))
    random_start_positions = bool(random.getrandbits(1))

    (machines, tape) = platypatterns.random_run(run_id,
                                                num_machines,
                                                tape_width,
                                                random_tape,
                                                random_start_positions,
                                                max_steps)

    input_file = f"run_imgs/{run_id}.png"
    image = Image.open(input_file)

    # Get image dimensions
    width, height = image.size

    # Report the original file size and image dimensions
    original_file_size = os.path.getsize(input_file)

    # Convert the image to bytes
    image_bytes = image.tobytes()

    # Compress the image using zlib
    compressed_data = zlib.compress(image_bytes, level=zlib.Z_BEST_COMPRESSION)

    # Create a new image from the compressed data (optional)
    compressed_image = Image.frombytes("RGB", (width, height),
                                       zlib.decompress(compressed_data))

    # Save the compressed data to a new file
    compressed_file = "compressed_output.dat"
    with open(compressed_file, "wb") as f:
        f.write(compressed_data)

    # Report the compressed file size
    compressed_file_size = os.path.getsize(compressed_file)
    compression = compressed_file_size/original_file_size

    # Report to CSV
    with open('run_data.csv', mode='a', newline='') as file:
        row_data = [run_id, max_steps, width, height, original_file_size, compressed_file_size, compression, tape]
        for machine in machines:
            machine_data = [
                machine["position"],
                *machine["rules"]
            ]
            row_data.extend(machine_data)
        writer = csv.writer(file)
        writer.writerow(row_data)

    print(f"Run: {run_id}")
    print(f"Original dimensions: {width}x{height}")
    print(f"Original size: {original_file_size} bytes")
    print(f"Compressed size: {compressed_file_size} bytes")
    print(f"Compression: {compression*100:.2f}%")

    # Close the images
    image.close()
    if 'compressed_image' in locals():
        compressed_image.close()
