#!/usr/bin/env python


import random, argparse

from base64 import b64decode

q_blob = b'WydTMHBodGx5IHMwcGh0bHkgY2F0Y2h5IG1vbmtleScsICdTMHBodGx5IGRvZXMgaXQnLCAnUzBwaHQgZmFyIHMwcGh0IGdvb2QnLCAnTGlmZSBpcyBzMHBodCcsICdNbW0uLiBTMHBodCBib2lsZWQgY29kZScsICdTMHBodCBhbmQgc3F1aXNoeScsICJJJ20gczBwaHQgb24gdGhlIGluc2lkZSIsICdTMHBodCBjb3JlIGhhY2tpbmcgaW5pdGlhdGVkJywgJ1ByZXNzIGFueSBrZXkgdG8gczBwaHQnLCAnRW50ZXIgeW91ciBzMHBodCBub3cnLCAnSXRzIG5vdCBtdWNoIGJ1dCBpdHMgczBwaHQgd29yaydd'
a_blob = b'WydTMHBodGNyYXRlcycsICdHaGFuZGksIFMwcGh0IGNvLWZvdW5kZXInLCAnTGlhbSBOZWVzMHBodCcsICdFbGl6YWJldGggV2luZHMwcGh0IElJJywgJ1NjYXJmYWNlJywgJ0VtaWx5IFMwcGh0aHVyc3QnXQ=='

ITALICS="[3m"
ENDC="[0m"


def quote(wisdom='wisdom.yml', escape_codes=True):
    quotes = eval(b64decode(q_blob))
    authors = eval(b64decode(a_blob))

    # Now pick the content
    quote = random.choice(quotes)
    author = random.choice(authors)
    # Now print it
    if not escape_codes:
        fmt_str = "{}\n\t- {}" 
    else:
        fmt_str = ITALICS + "{}" + ENDC + "\n\t- {}" 
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

