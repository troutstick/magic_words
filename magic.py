import sys
import create_magic as create
import get_magic as get


helpstring = f"""Usage:
    python magic.py
    python magic.py -h
        Print this helpstring
    
    python magic.py --create
    python magic.py -c
        Generate magic words based on input file {create.input_file_name}
    
    python magic.py --get
    python magic.py -g
        Print out the magic words in {create.product_file_name}, avoiding those already printed (stored in {get.seen_words_file})

    python magic.py --force
    python magic.py -f
        Print out ALL magic words. Will print out words blacklisted in {get.seen_words_file}

    python magic.py --reset
    python magic.py -r
        Reset the seen words file at {get.seen_words_file}.
"""

def print_help():
    print("Failed to decode arguments")
    print(helpstring)

def main():
    args = sys.argv
    if len(args) == 2:
        option = args[1]
        if option == '--create' or option == '-c':
            create.create_magic()
        elif option == '--get' or option == '-g':
            get.get_magic()
        elif option == '--force' or option == '-f':
            get.get_magic(True)
        elif option == '--reset' or option == '-r':
            get.reset()
        elif option == '-h':
            print(helpstring)
        else:
            print_help()
    elif len(args) == 1:
        print(helpstring)
    else:
        print_help()

if __name__ == "__main__":
    main()