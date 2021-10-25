import sys
import getopt

from . import htmlstripper


HELP = '''Python HTML Tag Stripper

Command line interface for stripping HTML tags from a file to get its raw text.

OPTIONS:
    -h
        Help. Print this message and exit.
        
    <filename> 
        The name of the file in the current directory to strip HTML tags from.
        The output will be printed to the terminal and stored in a file called
        "rawtxt.txt"
        
AUTHOR:
    Written by Marco Grimaldi
    
SOURCE:
    https://github.com/Mgrimaldi20/HTML-Tag-Stripper

'''

opts, args = getopt.getopt(sys.argv[1:], 'h')
for opt, arg in opts:
    if opt == '-h':
        print(HELP)
        exit(0)
    else:
        print("Not a valid option, exiting...")
        exit(0)

html_file = open(sys.argv[1])
html_txt = html_file.read()
html_file.close()

tag_stripper = HTMLStripper()

raw_txt = tag_stripper.strip_tags(html_txt)
txt_file = open("rawtxt.txt", "w")
print(raw_txt)
txt_file.write(raw_txt)  
txt_file.close()  
