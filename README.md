# elemental
A simple command line tool to encode text as a series of element symbols.

For example the word *satire* may be written *SAtIRe* where *S*, *At*, *I* and *Re* are the chemical symbols for *Sulfur*, *Astatine*, *Iodine* and *Rhenium*, respectively.  The tool will avoid reusing elements as much as possible to give a more varied output, so "*noses noses*" encodes as "*NOsEs NoSeS*", using six different elements.

## Usage
To convert short snippets, you can pass the text using the flag `-s`:

    element_code.py -s/--string "some text"

As most words in the english language (around 80%) are not writable using the standard element symbols, by omitting flags the tool can be run in interactive mode for faster testing:

    element_code.py

The tool can also be run on an entire text file and will maintain formatting (the f):

    element_code.py -f/--file somefilepath.txt

If the file can be fully encoded, the tool will create two new files for its output:

* `somefilepath_encoded.txt`: contains the encoded result.
* `somefilepath_elements.txt`: contains the list of elements used, in order.

Due to the high failure rate, it is strongly suggested to run on short snippets of a text before attempting an entire file.

## Common words
The file `common_encodable_words.txt` contains a list of a thousand common words (according to the Google Trillion Word Corpus) which can be encoded by the tool. This might be helpful for anyone searching for sentences.

## Configuration
The encoder uses the symbols listed in `elements.csv`, so a different set of symbols can be used by editing this file. Symbol matching is case-insensitive and later copies of the same symbol will overwrite earlier ones.
