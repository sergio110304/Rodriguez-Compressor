import sys

def verify(original_file, decompressed_file):
    with open(original_file, 'r') as f1, open(decompressed_file, 'r') as f2:
        original_data = f1.read()
        decompressed_data = f2.read()

    if original_data == decompressed_data:
        return "ok"
    else:
        return "nok"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verificador.py <original_file>")
        sys.exit(1)

    original_file = sys.argv[1]
    decompressed_file = "archivos/descomprimido-ec2.txt"

    result = verify(original_file, decompressed_file)
    print(result)