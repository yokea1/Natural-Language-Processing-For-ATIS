# tokenizer.py
def tokenize_sentences(input_file, output_file):
    # Open the input file and read all lines
    with open(input_file, 'r') as f:
        lines = f.readlines()

    tokenized = []
    for line in lines:
        # Simple tokenization: strip whitespace, convert to lowercase, split by spaces
        words = line.strip().lower().split()
        tokenized.append(words)

    # Write the tokenized sentences as lists to the output file
    with open(output_file, 'w') as f:
        for sentence in tokenized:
            f.write(str(sentence) + '\n')

# Call the function
tokenize_sentences('ATIS.txt', 'ATIS_list.txt')
