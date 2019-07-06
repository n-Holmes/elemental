"""
Converts a plaintext message into a string of element symbols.
Can be repurposed for a different set of symbols by replacing elements_dict.txt
"""

import string

# Preassemble symbol dictionary
SYMBOLS = {}
with open("elements.csv", "r") as file:
    for line in file.readlines():
        symbol, full = line.rstrip().split(",")
        SYMBOLS[symbol.lower()] = full


def encode(message: str):
    """Encode a message using the symbol dictionary.
    Preference is given to minimizing repetitions of symbols.
    """

    n = len(message)

    # Working list of partial encodings
    # Current encoding, symbols used in order, number of repetitions
    queue = [("", [], 0)]

    # Full encodings found
    encodings = []

    for partial, symlist, score in queue:
        plen = len(partial)
        if plen == n:
            encodings.append((partial, symlist, score))

        # Deal with non-alphabetical characters
        elif message[plen].lower() not in string.ascii_lowercase:
            queue.append((partial + message[plen], symlist, score))

        else:
            # Possible next symbols
            options = [message[plen].lower()]
            if n - plen >= 2:
                options.append(message[plen : plen + 2].lower())

            # Check if each option is actually a symbol
            for option in options:
                if option in SYMBOLS:
                    queue.append(
                        (
                            partial + option.capitalize(),  # Proper element format
                            symlist + [option],
                            score + symlist.count(option),
                        )
                    )

    try:
        sortkey = lambda x: (x[2], len(x[1]))
        bestencode = min(encodings, key=sortkey)
        return bestencode[0], [SYMBOLS[s] for s in bestencode[1]]

    except ValueError:
        raise SymbolError(
            f"The symbols dictionary is insufficient to encode the string `{message}`"
        )


class SymbolError(Exception):
    pass
