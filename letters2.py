def count_vowels(word: str) -> int:
    vowels = 'aeiouy'
    vowels += vowels.upper()
    return sum(1 for c in word if c in vowels)

def process_file(filename: str) -> None:
    """Process input file and print words with 2+ vowels reversed"""
    try:
        with open(filename, 'r') as f:
            for line in f:
                words = line.strip().split()
                processed = [w  for w in words if count_vowels(w) >= 2]
                print(' '.join(processed))
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == '__main__':
    process_file('input.txt')
