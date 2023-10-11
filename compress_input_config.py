import zlib
import csv

original_output_csv = "run_data.csv"
new_output_csv = "run_data_compressed_input.csv"

# binary encoding... so we can read back in nibbles
custom_encoding = {
    'M': '0000', 'T': '0001', 'R': '0010', '0': '0011', '1': '0100',
    '2': '0101', '3': '0110', '4': '0111', '5': '1000', '6': '1001',
    '7': '1010', '8': '1011', '9': '1100'
}

with open(new_output_csv, "w", newline="") as output_file:
    writer = csv.writer(output_file)

    with open(original_output_csv, "r") as input_file:
        reader = csv.reader(input_file)

        # update header row
        header = next(reader)
        header.extend(["encoded_input", "num_characters_binary_encoded", "num_bits_compressed", "compressed_data"])
        writer.writerow(header)

        for row in reader:
            brief_representation = row[7]
            binary_encoded_input = ''.join(custom_encoding[char] for char in brief_representation)
            num_characters = len(binary_encoded_input)
            num_bits = len(binary_encoded_input) // 8

            # not sure what encoding i should use, but it's consistently applied so
            # i think it shouldn't matter.
            compressed_data = zlib.compress(binary_encoded_input.encode("utf-8"))
            num_bits_compressed = len(compressed_data) * 8

            row.extend([binary_encoded_input, num_characters, num_bits_compressed, compressed_data])
            writer.writerow(row)