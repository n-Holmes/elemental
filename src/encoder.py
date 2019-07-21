"""
Converts a plaintext message into a string of element symbols.
Can be repurposed for a different set of symbols by replacing elements_dict.txt
"""

import string


def load_symbols(path="elements.csv"):
    """Puts together a symbol dictionary from a .csv file."""
    symbols = {}
    with open(path, "r") as file:
        for line in file.readlines():
            symbol, full = line.rstrip().split(",")
            symbols[symbol.lower()] = full

    return symbols


def encode(message: str, symbols: dict):
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
            continue

        # Find the next letter
        for i, char in enumerate(message[plen:]):
            if char.isalpha():
                break
        else:
            encodings.append((partial + message[plen:], symlist, score))
            continue
        
        partial += message[plen:plen + i]
        plen += i

        # Possible next symbols
        options = [message[plen].lower()]
        if n - plen >= 2:
            options.append(message[plen : plen + 2].lower())

        # Check if each option is actually a symbol
        for option in options:
            if option in symbols:
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
        return bestencode[0], [symbols[s] for s in bestencode[1]]

    except ValueError:
        raise SymbolError(
            f"The symbols dictionary is insufficient to encode the string `{message}`"
        )


class SymbolError(Exception):
    pass
