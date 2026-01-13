'''
Try handling empty files, missing files, or invalid numeric lines.

Add logging for skipped lines.

'''

def parse_numbers(filename):
    numbers = []
    try:
        with open(filename, "r") as f:
            for line in f:
                try:
                    num = int(line.strip())
                    numbers.append(num)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print("File not found!")
    finally:
        print("Parsing complete.")
    return numbers

data = parse_numbers("numbers.txt")
print("Parsed numbers:", data)