"""Command Line script to encode text as a sequence of element symbols.
author: Nathan Holmes
"""

import argparse
import pathlib
from src import encoder


def main():
    """Main body of the script, runs the CLI."""
    parser = argparse.ArgumentParser(
        description="Rewrites strings as combinations of element symbols."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("-f", "--file", help="Specify a file to encode the contents of.")
    mode.add_argument("-s", "--string", help="Specify a string to encode.")
    args = parser.parse_args()

    symbols = encoder.load_symbols()

    def encode_and_print(data):
        try:
            output, elements = encoder.encode(data, symbols)
            elem_string = str(elements)[1:-1]
            print(f"Result: {output}")
            print(f"Elements used:\n{elem_string}\n")
        except encoder.SymbolError:
            print("The requested string could not be encoded to elements.\n")

    if args.file:
        path = pathlib.Path(args.file)
        with path.open("r") as file:
            text = file.read()
        try:
            output, elements = encoder.encode(text, symbols)
        except encoder.SymbolError:
            print("File could not be encoded with the given symbols.")
            return

        # Create files and save
        name = path.stem
        encode_path = path.with_name(name + "_encoded.txt")
        elements_path = path.with_name(name + "_elements.txt")
        with encode_path.open("w") as file:
            file.write(output)
        with elements_path.open("w") as file:
            file.write(", ".join(elements))

        print("File successfully encoded.")

    elif args.string:
        encode_and_print(args.string)

    else:
        print("Starting in interactive mode...")
        while True:
            data = input("Please enter a string to be encoded (or `quit`): ")
            if data == "quit":
                break
            encode_and_print(data)


if __name__ == "__main__":
    main()
