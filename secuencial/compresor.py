import sys
import time
import numpy as np

def compress(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()

    compressed_data = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        compressed_data.append((data[i], count))
        i += 1

    with open(output_file, 'wb') as f:
        np.save(f, np.array(compressed_data, dtype=object))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compresor.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "archivos/comprimido.ec2"

    start_time = time.time()
    compress(input_file, output_file)
    end_time = time.time()

    print(f"{end_time - start_time:.2f}")