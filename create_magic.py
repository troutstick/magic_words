import itertools
import re

product_file_name = "magic_words.txt"
input_file_name = 'input.txt'

a_pattern = re.compile(r'.*a$') # words that end with a
b_pattern = re.compile(r'.*b.*') # words that contain b
comment_pattern = re.compile(r'#.*|^$')

def create_magic():
    with open(input_file_name, 'r') as input_file:
        a_words = set()
        b_words = set()
        for word in input_file:
            if comment_pattern.match(word):
                continue

            word = word.strip()
            assert len(word.split()) == 1, f"`{word}` should not contain whitespace"

            if a_pattern.match(word):
                a_words.add(word)

            if b_pattern.match(word):
                b_words.add(word)
        
        
    num_words = 0
    with open(product_file_name, 'w') as output_file:
        for a,b in itertools.product(a_words, b_words):
            output_file.write(f"{a} {b}\n")
            num_words += 1

    print(f"Found {len(a_words)} A words and {len(b_words)} B words")
    print(f"Created {num_words} magic words in {product_file_name}!")