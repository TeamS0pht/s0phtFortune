#!/usr/bin/env python

import yaml, random, argparse

from base64 import b64encode
from sys import argv
from os import chmod

ITALICS="\033[3m"
ENDC="\033[0m"

def get_wisdom(wisdom='wisdom.yml'):
    """Read in the wisdom file and return quotes and authors"""

    with open(wisdom ,'r') as w:
        content = yaml.load(w, Loader=yaml.FullLoader)

    return content['quotes'], content['authors']
    
def quote(wisdom='wisdom.yml', escape_codes=True):
    """Open wisdom file, parse for content and randomly select a quote
            and author, before printing to screen"""

    quotes, authors = get_wisdom()

    # Now pick the content
    
    quote = random.choice(quotes)
    author = random.choice(authors)

    # Now print it
    if not escape_codes:
        fmt_str = "{}\n\t- {}" 
    else:
        fmt_str = ITALICS + "{}" + ENDC + "\n\t- {}" 
    return fmt_str.format(quote, author)

def make_sandwich(quotes, authors, out_file='sandwich.py'):
    "Write portable version out -  all wisdom is embedded as base64 blob"""

    imports = """
import random, argparse

from base64 import b64decode

"""
    quotes_global = "q_blob = {}".format(b64encode(str(quotes).encode()))
    authors_global = "a_blob = {}".format(b64encode(str(authors).encode()))
    italics_global = """
ITALICS="\033[3m"
ENDC="\033[0m"
"""
    main = '''
def quote(wisdom='wisdom.yml', escape_codes=True):
    quotes = eval(b64decode(q_blob))
    authors = eval(b64decode(a_blob))

    # Now pick the content
    quote = random.choice(quotes)
    author = random.choice(authors)
    # Now print it
    if not escape_codes:
        fmt_str = "{}\\n\\t- {}" 
    else:
        fmt_str = ITALICS + "{}" + ENDC + "\\n\\t- {}" 
    return fmt_str.format(quote, author)

def main(wisdom, escape):
    print(quote(wisdom, escape))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sandwich", action="store_true", 
            help="Make a portable version of the script to take with you.")
    parser.add_argument("-n", "--no-escape",default = False, action="store_true",
            help="Do not use ANSI escape codes to print in italics. Sad times.")
    parser.add_argument("-w", "--wisdom", type=str, default="wisdom.yml",
            help="Optional custom Wisdom file. Default is wisdom.yml")
    parser.add_argument("-o", "--out_file", type=str, default="sandwich.py",
            help="Optional custom out file name for sandwich mode, else sandwich.py")
    args = parser.parse_args()

    if args.sandwich:
        #The only option for now is to make a sandwich
        quotes, authors = get_wisdom(args.wisdom)
        make_sandwich(quotes, authors, args.out_file)
    else:
        main(args.wisdom, not args.no_escape)
'''

    with open(out_file, 'w') as o:
        o.write("#!/usr/bin/env python\n\n{}".format(imports))
        o.write("{}\n".format(quotes_global))
        o.write("{}\n".format(authors_global))
        o.write("{}\n".format(italics_global))
        o.write("{}\n".format(main))

    chmod(out_file, 0o755)

def main(wisdom, escape):
    print(quote(wisdom, escape))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sandwich", action="store_true", 
            help="Make a portable version of the script to take with you.")
    parser.add_argument("-n", "--no-escape",default = False, action="store_true",
            help="Do not use ANSI escape codes to print in italics. Sad times.")
    parser.add_argument("-w", "--wisdom", type=str, default="wisdom.yml",
            help="Optional custom Wisdom file. Default is wisdom.yml")
    parser.add_argument("-o", "--out_file", type=str, default="sandwich.py",
            help="Optional custom out file name for sandwich mode, else sandwich.py")
    args = parser.parse_args()

    if args.sandwich:
        #The only option for now is to make a sandwich
        quotes, authors = get_wisdom(args.wisdom)
        make_sandwich(quotes, authors, args.out_file)
    else:
        main(args.wisdom, not args.no_escape)

