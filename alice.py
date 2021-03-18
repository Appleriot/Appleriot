filename = 'alice.txt'
try:
    with open(filename, encoding= 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry {filename} don't exist.")
else:
    # The number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"This is the number of words in {filename}: {num_words}")
