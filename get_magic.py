import create_magic
import random

seen_words_file = 'seen_magic.txt'

def reset():
    try:
        f = open(seen_words_file, 'w')
        f.close()
    except FileNotFoundError:
        f = open(seen_words_file, 'x')
        f.close()

    print("List of seen words has been reset!")

def get_magic(ignore_seen=False):
    try:
        with open(create_magic.product_file_name, 'r') as magic_words:  
            magic_words = [m.strip() for m in magic_words]
    except FileNotFoundError:
        print("Uh oh, you haven't made magic yet!")
        print("Run with the `-c` option to make magic!")
        return

    words_seen = set()
    try:
        if not ignore_seen:
            with open(seen_words_file, 'r') as seen:
                words_seen.update(line.strip() for line in seen)
    except FileNotFoundError:
        f = open(seen_words_file, 'x')
        f.close()

    shuffled = random.sample(magic_words, len(magic_words))

    num_left = len(magic_words) - len(words_seen)
    print(f"Total magic words left: {num_left}\n")
    with open(seen_words_file, 'a') as seen:
        for word in shuffled:
            if word in words_seen:
                continue
            else:
                print("Press `q` to quit")
                user_in = input("Enter something to receive next magic: ")
                
                if user_in.strip() == 'q':
                    print('quitting...')
                    return

                seen.write(f"{word}\n")
                words_seen.add(word)
                print(f"MAGIC WORD: `{word}`")

                num_left -= 1
                uwu = '\nNice' if num_left == 69 else ''
                print(f"num_left: {num_left}{uwu}\n")

        print("Exhausted all magic words")
        print(f"Delete {seen_words_file} or use the `-r` option if you want to continue magicking")