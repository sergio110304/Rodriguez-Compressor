import sys
import time
import numpy as np

def decompress(input_file, output_file):
    with open(input_file, 'rb') as f:
        compressed_data = np.load(f, allow_pickle=True)

    decompressed_data = []
    for char, count in compressed_data:
        decompressed_data.append(char * count)

    with open(output_file, 'w') as f:
        f.write(''.join(decompressed_data))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 secuencial/descompresor.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "archivos/descomprimido-ec2.txt"

    start_time = time.time()
    decompress(input_file, output_file)
    end_time = time.time()

    print(f"Decompression took {end_time - start_time:.2f} seconds")