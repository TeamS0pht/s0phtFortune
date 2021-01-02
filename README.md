# TeamPhrases

This is a near pointless project, but I got a bit bored on new years, not sorry. It's a little python method and yml file to create random team related nonsense, I intend to import it into other tools over time, under some ASCII art because this is roughly 'on my level'. Use sadnwich mode to freeze the config by creating a portable, config-less version if you like. 

It's in Git so that anyone can add their pointless phrases if they want. No pressure.

	- Blackfell

## Usage

Run pearls for your daily wisdom; turn off ANSI italics with `n` and create portable sandwich with `-s`.

```
❯ ./pearls.py -h                                                                                       ─╯
usage: pearls.py [-h] [-s] [-n] [-w WISDOM] [-o OUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -s, --sandwich        Make a portable version of the script to take with you.
  -n, --no-escape       Do not use ANSI escape codes to print in italics. Sad times.
  -w WISDOM, --wisdom WISDOM
                        Optional custom Wisdom file. Default is wisdom.yml
  -o OUT_FILE, --out_file OUT_FILE
                        Optional custom out file name for sandwich mode, else sandwich.py
```
