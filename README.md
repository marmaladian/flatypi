# Flatypi
A simple investigation into compression as a means of identifying _interesting_ computational behaviour.

---

`interesting.py` will run batches of 1000 random platypus games using `platypatterns.py`.
The output is written as an image to the `run_imgs` directory. The images are compressed using zlib and compared with the original. The data for each run is written to `run_data.csv`.

`compress_input_config.py` will convert the input configuration for each run (machine transition rules, starting positions, board state) into a binary encoded string. This is then compressed with zlib and the resulting string lengths in bits are compared. The results are written to a new output file `run_data_compressed_input.csv`